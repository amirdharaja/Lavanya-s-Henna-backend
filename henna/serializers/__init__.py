from henna.models import User

from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer

from henna.model.ContactRequest import ContactRequest
from henna.model.GalleryImage import GalleryImage
from henna.model.MainSlideImage import MainSlideImage
from henna.model.PageImage import PageImage


class ContactRequestSerializer(ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = ('id', 'is_responsed', 'name', 'email', 'phone', 'details', 'response')

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
        }

    def post(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class MainSlideImageSerializer(ModelSerializer):
    class Meta:
        model = MainSlideImage
        fields = ('id', 'image',)

    def post(self, validated_data):
        return MainSlideImage.objects.create(**validated_data)

class PageImageSerializer(ModelSerializer):
    class Meta:
        model = PageImage
        fields = ('id', 'image',)

class GalleryImageSerializer(ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ('id', 'image', 'package', 'henna_area')