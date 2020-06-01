from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .viewsets import ImageViewSet
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('image', ImageViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('rollcall', views.rollcall, name='assistance'),
    path('api/', include(router.urls), name='api')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
