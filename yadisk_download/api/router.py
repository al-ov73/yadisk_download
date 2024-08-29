from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from yadisk_download.api import views

router = DefaultRouter(trailing_slash=True)

urlpatterns = router.urls

urlpatterns.extend([
    path('links/', views.get_files),
    path('signup/', views.user_create),
    path('login/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
])
