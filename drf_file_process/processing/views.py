from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import File
from .serializers import FileListSerializer, FileUploadSerializer
from .tasks import process_file_task


class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser,)
    serializer_class = FileUploadSerializer

    def get(self, request):
        return Response('Upload files here')

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            file_instance = serializer.save()
            process_file_task.delay(file_instance.id)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class FileListAPIView(APIView):
    def get(self, request):
        files = File.objects.all()
        serializer = FileListSerializer(files, many=True)
        return Response(serializer.data)
