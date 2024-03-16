from rest_framework import serializers

from django.contrib.auth import get_user_model


User = get_user_model() # built in user model


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    # custom exceptions
    username_error_message = {
        'username': 'Username should contain alphanumeric characters only (numbers and like alphapatical letters)',
        }
    
    email_error_message = {
        'username': 'This email already registered',
        }

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                self.username_error_message
                )
        
        repeted_email = User.objects.filter(email=email)
        if repeted_email.exists():
            raise serializers.ValidationError(
                self.email_error_message
                )
        
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
