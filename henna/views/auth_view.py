from django.contrib.auth.models import auth

from henna.models import User

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework.status import (
    HTTP_200_OK as ok,
    HTTP_201_CREATED as created,
    HTTP_400_BAD_REQUEST as bad_request,
    HTTP_404_NOT_FOUND as not_found,
)


@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if not username or not password:
        return Response({'status': False, 'detail': 'USERNAME PASSWORD CAN NOT BE EMPTY'}, status=bad_request)

    user = User.objects.filter(username=username).first()
    if not user:
        return Response({'status': False, 'detail': 'USER NOT FOUND'}, status=not_found)

    user = auth.authenticate(username=user.username, password=password)
    if not user:
        return Response({'status': False, 'detail': 'WRONG PASSWORD'}, status=bad_request)

    token, _ = Token.objects.get_or_create(user=user)

    data = {
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }

    return Response({
        'status': True,
        'token': token.key,
        'data': data,
    }, status=ok)

@api_view(["DELETE"])
@permission_classes((IsAuthenticated))
def logout(request):
    pass

@api_view(["PUT"])
@permission_classes((IsAuthenticated))
def change_password(request):
    pass