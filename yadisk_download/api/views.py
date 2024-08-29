from django.http import HttpRequest

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

from yadisk_download.api.serializers import UserSerializer
from yadisk_download.api.utils import get_files_from_yadisk_link


@api_view(['POST'])
def get_files(request: HttpRequest) -> Response:
    '''
    Принимает ссылку в request.data['link'], парсит ссылки на файлы,
    возвращает список файлов со ссылками вида:
    [{
        'filename': 'имя файла',
        'link': 'ссылка_на_скачивание_файла'
    },]
    '''
    public_link = request.data['link']
    try:
        links_list = get_files_from_yadisk_link(public_link)
        return Response(status=200, data=links_list)
    except KeyError:
        return Response(status=400, data='Неверный запрос')


@api_view(['POST'])
def user_create(request: HttpRequest) -> Response:
    '''
    Регистрирует пользователя в базе данных.
    Модель пользователя:
    {
        'username': 'имя_пользователя',
        'password': 'пароль'
    }
    '''
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
