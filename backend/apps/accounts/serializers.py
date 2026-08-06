from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password],
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        # Omitting first_name and last_name until UI requirements confirm they are needed
        fields = ('id', 'username', 'email', 'password', 'phone_number', 'profile_image')
        extra_kwargs = {
            'username': {
                'error_messages': {
                    'unique': 'Username already exists.'
                }
            },
            'email': {'required': True}
        }
        
    def validate_email(self, value):
        # AbstractUser's email field is not unique=True by default. 
        # We manually enforce uniqueness here to prevent duplicate registrations.
        if value and User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def create(self, validated_data):
        # Passing validated_data cleanly into create_user handles all defaults 
        # (like profile_image's blank=True) automatically at the model level
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'}, required=True)

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username and not email:
            raise serializers.ValidationError({"username": ["Must include 'username' or 'email'."]})

        user = None
        if username:
            # First try authenticate by username
            user = authenticate(username=username, password=password)
            if not user:
                # Also check if the user entered an email address in the username field
                try:
                    user_obj = User.objects.get(email=username)
                    user = authenticate(username=user_obj.username, password=password)
                except (User.DoesNotExist, User.MultipleObjectsReturned):
                    user = None
        elif email:
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(username=user_obj.username, password=password)
            except (User.DoesNotExist, User.MultipleObjectsReturned):
                user = None

        if not user:
            # Identical error message for wrong password and non-existent user
            raise serializers.ValidationError("Invalid credentials.")

        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")

        data['user'] = user
        return data


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True)

    def validate(self, data):
        try:
            self.token = RefreshToken(data['refresh'])
        except TokenError:
            raise serializers.ValidationError({"refresh": ["Invalid or expired refresh token."]})
        return data

    def save(self, **kwargs):
        self.token.blacklist()
