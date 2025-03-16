from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    UploadEncryptedFolderView,
    DownloadEncryptedFolderView,
    ChangeEncryptionPasswordView,
)

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login'),
    path('api/upload/', UploadEncryptedFolderView.as_view(), name='upload'),
    path('api/download/', DownloadEncryptedFolderView.as_view(), name='download'),
    path('api/change-password/', ChangeEncryptionPasswordView.as_view(), name='change-password'),
]
