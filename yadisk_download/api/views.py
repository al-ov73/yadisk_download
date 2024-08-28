import requests

from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from urllib.parse import urlencode

from yadisk_download.api.serializers import UserSerializer

RESOURCES = "https://cloud-api.yandex.net/v1/disk/public/resources?"

@api_view(['POST'])
def get_files(request: HttpRequest):
    public_link = request.data['link']
    
    requests_url = RESOURCES + urlencode(dict(public_key=public_link))
    response = requests.get(requests_url)
    type = response.json()['type']

    if type == 'dir':
        links_list = []
        files_list = response.json()['_embedded']['items']
        for file in files_list:
            links_list.append({
                'filename': file['name'],
                'link': file['file']
            })
        return Response(data=links_list)
    else:
        file = response.json()
        links_list = [{
            'filename': file['name'],
            'link': file['file']
        }]

    return Response(data=links_list)


@api_view(['POST'])
def user_create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

    return Response({'Некорректные данные': serializer.errors},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)