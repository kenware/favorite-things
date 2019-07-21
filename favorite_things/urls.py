# Django import
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
# local import
from favorite_app import views

router = DefaultRouter()
router.register('category', views.CategoryViewSet, basename='category')
router.register('favorite', views.FavoriteThingsViewSet, basename='favorite')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
