from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, \
    UserChangePasswordSerializer, SendPasswordResetEmailSerializer, UserPasswordResetSerializer, UserProfileSerializer
from django.contrib.auth import authenticate
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from .models import Profile
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin



# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



# User Registration View
class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token': token, 'msg': "Registration success"}, status=status.HTTP_201_CREATED)


# User Login View
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': "Login success"}, status=status.HTTP_200_OK)

        else:
            return Response({'errors': 'Email or Password is not Valid'}, status=status.HTTP_400_BAD_REQUEST)


# User Profile View
class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Password Change View
class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data,                           context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': "Password Changed successfully"}, status=status.HTTP_200_OK)


# Send password reset email view
class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Reset Link sent, Please Check Your Mail!'}, status=status.HTTP_200_OK)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={
            'uid': uid, 'token': token
        })
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Reset Successfully'}, status=status.HTTP_200_OK)


class UserProfileListView(GenericAPIView, ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    
    def get(self, request ,*args,**kwargs):
        return self.list(request ,*args,**kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)