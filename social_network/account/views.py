from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import get_object_or_404
from django.contrib.auth.models import User


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


class LoginGenericAPIView(generics.GenericAPIView):
    """Login for users"""
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = get_object_or_404(User, email=request.data['email'])
        token = str(RefreshToken.for_user(user).access_token)
        return Response({'token': token}, status=status.HTTP_200_OK)


class LogoutGenericAPIView(generics.GenericAPIView):
    """Logout for users"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
