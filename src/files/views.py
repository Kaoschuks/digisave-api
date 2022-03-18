from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework import status, viewsets
from .models import File
from core.mixin import LoggingMixin

class FileView(LoggingMixin, viewsets.ViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    queryset = File.objects.all()
    serializer_class = FileSerializer

    @action(detail=False, methods=['post'])
    def upload(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data,
                status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def delete_file(self, request, *args, **kwargs):
        if request.data['file'] is None:
            return Response({"status": "no file provide"}, status.HTTP_400_BAD_REQUEST)
        file = request.data['file']
        user_id = kwargs['pk']
        files = File.objects.filter(owner=user_id)
        file_serilizer  =  None
        file_instance = None
        for f in files:
            file_serilizer = FileSerializer(f)
            file_instance = f
            if file_serilizer.data['file'] == file:
                f.file.delete(save=True)
                file_instance.delete()
                return Response({"status": "deleted"}, status.HTTP_200_OK)
        return Response({"status": "failed"}, status.HTTP_404_NOT_FOUND)

