from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('img-clf', views.ImgUploadViewSet, basename='img-classify')

urlpatterns = [
    path('', include(router.urls)),

]
