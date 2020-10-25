from django.urls import include, path, re_path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from henna.viewsets import (
    ContactRequestViewSet,
    GalleryImageViewSet,
    MainSlideImageViewSet,
    PageImageViewSet,
    UserViewSet,
)

router = DefaultRouter()

router.register('all/contact-requests', ContactRequestViewSet)
router.register('all/gallery-images', GalleryImageViewSet)
router.register('all/main-slide-images', MainSlideImageViewSet)
router.register('all/page-images', PageImageViewSet)
router.register('all/users', UserViewSet)


app_name = 'henna'

from henna.views.auth_view import (
    login,
    logout,
    change_password,
)
from henna.views.common_view import (
    get_gallery_images,
    get_main_slide_images,
    get_page_images,
    post_contact_request,
    get_bridal_package_images,
)
from henna.views.admin_view import (
    ContactRequestAPI,
    GalleryImageAPI,
    MainSlideImageAPI,
    PageImageAPI,
    UserAccountAPI,
)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login),
    path('logout/', logout),
    path('password/change/', change_password),
    path('gallery/', get_gallery_images),
    path('main-slide-images/', get_main_slide_images),
    path('page-images/', get_page_images),
    path('contact/', post_contact_request),
    path('package/', get_bridal_package_images),
    re_path(r'admin/requests/', ContactRequestAPI.as_view()),
    re_path(r'admin/gallery-images/', GalleryImageAPI.as_view()),
    re_path(r'admin/main-slide-images/', MainSlideImageAPI.as_view()),
    re_path(r'admin/page-images/', PageImageAPI.as_view()),
    re_path(r'users/', UserAccountAPI.as_view()),
]