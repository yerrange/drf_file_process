from django.conf.urls.static import static
from django.urls import path

from core import settings

from .views import FileListAPIView, FileUploadAPIView

app_name = 'processing'

urlpatterns = [
    path('upload/', FileUploadAPIView.as_view(), name='upload'),
    path('files/', FileListAPIView.as_view(), name='files')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
