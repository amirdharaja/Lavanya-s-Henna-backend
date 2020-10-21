from henna.models import User

from henna.model.MainSlideImage import MainSlideImage
from henna.model.PageImage import PageImage
from henna.model.GalleryImage import GalleryImage
from henna.model.ContactRequest import ContactRequest

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view, APIView
from rest_framework.status import (
    HTTP_200_OK as ok,
    HTTP_201_CREATED as created,
    HTTP_202_ACCEPTED as accepted,
    HTTP_304_NOT_MODIFIED as no_change,
    HTTP_400_BAD_REQUEST as bad_request,
    HTTP_401_UNAUTHORIZED as un_authorized,
    HTTP_403_FORBIDDEN as forbidden,
    HTTP_404_NOT_FOUND as not_found,
)
from henna.serializers import (
    ContactRequestSerializer,
    GalleryImageSerializer,
    MainSlideImageSerializer,
    PageImageSerializer,
    UserSerializer
)


@permission_classes((IsAuthenticated,))
class UserAccountAPI(APIView):

    def get(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.user.id).first()
        if not user:
            return Response({'status': False}, status=not_found)

        user = UserSerializer(user,  many=False)
        return Response({'status': True, 'data': user.data}, status=ok)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data['data'])
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'detail': 'New user account created successfully',}, status=created)

        return Response({'status': False, 'message':serializer.errors}, status=bad_request)

    def put(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.user.id).first()
        if not user:
            return Response({'status': False}, status=not_found)

        user.first_name = request.data.get('first_name') if request.data.get('first_name') else user.first_name
        user.last_name = request.data.get('last_name') if request.data.get('last_name') else user.last_name
        user.phone = request.data.get('phone') if request.data.get('phone') else user.phone

        user.save()
        return Response({'status': True}, status=ok)

    def delete(self, request, *args, **kwargs):
        User.objects.filter(id=request.user.id).delete()
        Token.objects.filter(user=request.user).delete()
        return Response({'status': True}, status=ok)


@permission_classes((IsAuthenticated,))
class ContactRequestAPI(APIView):

    def get(self, request, *args, **kwargs):
        contact_requests = ContactRequest.objects.order_by('-created_at')
        contact_requests = ContactRequestSerializer(contact_requests,  many=False)
        return Response({'status': True, 'data': contact_requests.data}, status=ok)

    def put(self, request, *args, **kwargs):
        contact_request = ContactRequest.objects.filter(id=request.user.id).first()
        if not contact_request:
            return Response({'status': False, 'detail': 'Contact request is not found'}, status=not_found)

        contact_request.is_responsed = True
        contact_request.save()
        return Response({'status': True}, status=ok)


@permission_classes((IsAuthenticated,))
class MainSlideImageAPI(APIView):

    def get(self, request, *args, **kwargs):
        main_slide_images = MainSlideImage.objects.order_by('-created_at')
        main_slide_images = MainSlideImageSerializer(main_slide_images,  many=True)
        return Response({'status': True, 'data': main_slide_images.data}, status=ok)

    def post(self, request, *args, **kwargs):
        image = str(request.FILES['image']).split('.')
        image_format = ['jpg', 'jpeg', 'JPG', 'JPEG', 'png', 'PNG']
        if image[-1] not in image_format:
            return Response({'status': False, 'detail': 'JPEG or PNG only allowed',}, status=bad_request)

        serializer = MainSlideImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'detail': 'Main slide image added successfully',}, status=created)

        return Response({'status': False, 'message':serializer.errors}, status=bad_request)

    def put(self, request, *args, **kwargs):
        MainSlideImage.objects.filter(id=request.user.id).update(image=request)
        return Response({'status': True}, status=accepted)

    def delete(self, request, *args, **kwargs):
        MainSlideImage.objects.filter(id=request.user.id).delete()
        return Response({'status': True}, status=ok)


@permission_classes((IsAuthenticated,))
class PageImageAPI(APIView):

    def get(self, request, *args, **kwargs):
        page_images = PageImage.objects.order_by('-created_at')
        page_images = PageImageSerializer(page_images,  many=False)
        return Response({'status': True, 'data': page_images.data}, status=ok)

    def post(self, request, *args, **kwargs):
        serializer = PageImageSerializer(data=request.data['data'])
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'detail': 'Page Image added successfully',}, status=created)

        return Response({'status': False, 'message':serializer.errors}, status=bad_request)

    def put(self, request, *args, **kwargs):
        PageImage.objects.filter(id=request.user.id).update(image=request)
        return Response({'status': True}, status=accepted)

    def delete(self, request, *args, **kwargs):
        PageImage.objects.filter(id=request.user.id).delete()
        return Response({'status': True}, status=ok)


@permission_classes((IsAuthenticated,))
class GalleryImageAPI(APIView):

    def get(self, request, *args, **kwargs):
        gallery_images = GalleryImage.objects.order_by('-created_at')
        gallery_images = GalleryImageSerializer(gallery_images, many=True)
        return Response({'status': True, 'data': gallery_images.data}, status=ok)

    def post(self, request, *args, **kwargs):
        serializer = GalleryImageSerializer(data=request.data['data'])
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'detail': 'Gallery Image added successfully',}, status=created)

        return Response({'status': False, 'message':serializer.errors}, status=bad_request)

    def put(self, request, *args, **kwargs):
        GalleryImage.objects.filter(id=request.user.id).update(image=request)
        return Response({'status': True}, status=accepted)

    def delete(self, request, *args, **kwargs):
        GalleryImage.objects.filter(id=request.user.id).delete()
        return Response({'status': True}, status=ok)
