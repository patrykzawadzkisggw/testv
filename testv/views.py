from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserActivity, TrustedDevice
from .serializers import UserSerializer, TrustedDeviceSerializer, UserActivitySerializer
from .encryption import encrypt_file, decrypt_file, encrypt_with_rsa, decrypt_with_rsa
import os

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UploadEncryptedFolderView(APIView):
    def post(self, request):
        user = request.user
        folder = request.FILES.get('folder')
        encryption_password = request.data.get('encryption_password')
        encrypted_folder_path = encrypt_file(folder, encryption_password)
        user.folder = encrypted_folder_path
        user.save()
        return Response({"message": "Folder uploaded and encrypted successfully"}, status=status.HTTP_200_OK)

class DownloadEncryptedFolderView(APIView):
    def get(self, request):
        user = request.user
        encrypted_folder_path = user.folder
        decryption_password = request.data.get('decryption_password')
        decrypted_folder_path = decrypt_file(encrypted_folder_path, decryption_password)
        return Response({"folder": decrypted_folder_path}, status=status.HTTP_200_OK)

class ChangeEncryptionPasswordView(APIView):
    def post(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        encrypted_folder_path = user.folder
        decrypted_folder_path = decrypt_file(encrypted_folder_path, old_password)
        new_encrypted_folder_path = encrypt_file(decrypted_folder_path, new_password)
        user.folder = new_encrypted_folder_path
        user.save()
        return Response({"message": "Encryption password changed successfully"}, status=status.HTTP_200_OK)
