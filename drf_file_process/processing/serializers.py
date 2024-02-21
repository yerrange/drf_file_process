from rest_framework.serializers import ModelSerializer

from .models import File


class FileUploadSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'file', 'uploaded_at')


class FileListSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'file', 'uploaded_at', 'processed')
