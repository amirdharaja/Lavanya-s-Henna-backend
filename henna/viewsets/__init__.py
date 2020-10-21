from henna.models import User

from rest_framework.viewsets import ModelViewSet

from henna.model.ContactRequest import ContactRequest
from henna.model.GalleryImage import GalleryImage
from henna.model.MainSlideImage import MainSlideImage
from henna.model.PageImage import PageImage

from henna.serializers import (
    ContactRequestSerializer,
    GalleryImageSerializer,
    MainSlideImageSerializer,
    PageImageSerializer,
    UserSerializer
)


class ContactRequestViewSet(ModelViewSet):
    queryset = ContactRequest.objects.order_by('-created_at')
    serializer_class = ContactRequestSerializer

class GalleryImageViewSet(ModelViewSet):
    queryset = GalleryImage.objects.order_by('-created_at')
    serializer_class = GalleryImageSerializer

class MainSlideImageViewSet(ModelViewSet):
    queryset = MainSlideImage.objects.order_by('-created_at')
    serializer_class = MainSlideImageSerializer

class PageImageViewSet(ModelViewSet):
    queryset = PageImage.objects.order_by('-created_at')
    serializer_class = PageImageSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.order_by('-created_at')
    serializer_class = UserSerializer
