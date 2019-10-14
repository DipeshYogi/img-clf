from rest_framework import serializers
from .models import ImgModel

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImgModel
        fields = ('img',)
