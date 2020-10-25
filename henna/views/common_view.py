from henna.model.MainSlideImage import MainSlideImage
from henna.model.PageImage import PageImage
from henna.model.GalleryImage import GalleryImage
from henna.model.ContactRequest import ContactRequest

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_200_OK as ok,
    HTTP_201_CREATED as created,
    HTTP_400_BAD_REQUEST as bad_request,
)

from henna.serializers import (
    MainSlideImageSerializer,
    PageImageSerializer,
    GalleryImageSerializer,
    ContactRequestSerializer,
)


@api_view(('get',))
def get_main_slide_images(request, *args, **kwargs):
    main_slide_images = MainSlideImage.objects.order_by('-created_at')
    main_slide_images = MainSlideImageSerializer(main_slide_images, many=True)

    data = {
        'main_slide_images': main_slide_images.data,
    }
    return Response({'status': True, 'data': data}, status=ok)


@api_view(('get',))
def get_page_images(request, *args, **kwargs):
    page_images = PageImage.objects.order_by('-created_at')
    page_images = PageImageSerializer(page_images, many=True)

    data = {
        'page_images': page_images.data,
    }
    return Response({'status': True, 'data': data}, status=ok)


@api_view(('get',))
def get_gallery_images(request, *args, **kwargs):
    sort_by = request.GET['sort']
    if sort_by == 'h':
        gallery_images = GalleryImage.objects.filter(henna_area='h').order_by('-created_at')
    elif sort_by == 'f':
        gallery_images = GalleryImage.objects.filter(henna_area='f').order_by('-created_at')
    elif sort_by == 'o':
        gallery_images = GalleryImage.objects.filter(henna_area='o').order_by('-created_at')
    else:
        gallery_images = GalleryImage.objects.order_by('-created_at')
    gallery_images = GalleryImageSerializer(gallery_images, many=True)

    data = {
        'gallery_images': gallery_images.data,
    }
    return Response({'status': True, 'data': data}, status=ok)


@api_view(('post',))
def post_contact_request(request, *args, **kwargs):
    serializer = ContactRequestSerializer(data=request.data['data'])
    if serializer.is_valid():
        serializer.save()
        return Response({'status': True, 'detail': 'New Contact request created successfully', }, status=created)

    return Response({'status': False, 'message':serializer.errors}, status=bad_request)


@api_view(('get',))
def get_bridal_package_images(request, *args, **kwargs):
    bridal_package_images = GalleryImage.objects.filter(package=request.GET['name']).order_by('-created_at')[:6]
    if bridal_package_images.count() == 0:
        bridal_package_images = GalleryImage.objects.order_by('-created_at')[:6]

    bridal_package_images = GalleryImageSerializer(bridal_package_images, many=True)

    data = {
        'bridal_package_images': bridal_package_images.data,
    }
    return Response({'status': True, 'data': data}, status=ok)
