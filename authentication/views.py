from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
from django.conf import settings

import jwt

from .serializers import RegisterSerializer
from .token_generator import Token
from .email_sender import EmailContent, Email

User = get_user_model()

class RegisterView(GenericAPIView):
    permission_classes = (AllowAny, )
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        
        user.is_active = False
        user.save()
        
        token = Token(user, request).generate_token()
        
        email_content = EmailContent(request, user, token).set_up_content()
        
        Email.send_email(email_content)
        
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(GenericAPIView):
    permission_classes = (AllowAny, )
    
    def get(self, request):
        token = request.GET.get("token")
        
        try:
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms='HS256')
            
            user = User.objects.get(id=payload["user_id"])
            user.is_active = True
            user.save()
            
            return Response({"Done": "Successfully activated, log in please"}, status=status.HTTP_200_OK)
            
        except jwt.ExpiredSignatureError:
            return Response({"Error": "Activation link expired"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError:
            return Response({"Error": "Activation link has been tampered"}, status=status.HTTP_400_BAD_REQUEST)
