from django.urls import path

from rest_framework.routers import DefaultRouter

from yadisk_download.api import views

router = DefaultRouter(trailing_slash=True)

urlpatterns = router.urls

urlpatterns.extend([
    path('links/', views.get_files),
    path('signup/', views.user_create)
])