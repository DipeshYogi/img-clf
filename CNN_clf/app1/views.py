from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from . import serializers
from .cnn_data_prep import image_predict
from .models import ImgModel
from rest_framework.permissions import IsAuthenticated

class ImgUploadViewSet(viewsets.ViewSet):
    serializer_class = serializers.ImageSerializer
    permission_classes = (IsAuthenticated,)

    def create(self,request):
        serializer =  self.serializer_class(data=request.data)

        if serializer.is_valid():
            img = serializer.validated_data.get('img')
            image = ImgModel(img=img)
            image.save()
            id = image.id
            data = ImgModel.objects.get(pk=id)
            op = image_predict(data)
            return Response({'message':op})
        else:
            return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
