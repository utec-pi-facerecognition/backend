from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .viewsets import ImageViewSet
from . import views
from rest_framework import routers

from frecognition.api.views import ClaseGetAPIView
from frecognition.api.views import ClaseCreateAPIView
from frecognition.api.views import AlumnoGetAPIView
from frecognition.api.views import AlumnoCreateAPIView
from frecognition.api.views import EmbeddingGetAPIView
from frecognition.api.views import EmbeddingCreateAPIView

from frecognition.api.views import rollcall

router = routers.DefaultRouter()
router.register('image', ImageViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls), name='api'),
    path('api/clases/get', ClaseGetAPIView.as_view(), name='clases-get'),
    path('api/clases/create', ClaseCreateAPIView.as_view(), name='clases-create'),
    path('api/alumno/get', AlumnoGetAPIView.as_view(), name='alumno-get'),
    path('api/alumno/create', AlumnoCreateAPIView.as_view(), name='alumno-create'),
    path('api/embedding/get', EmbeddingGetAPIView.as_view(), name='embedding-get'),
    path('api/embedding/create', EmbeddingCreateAPIView.as_view(), name='embedding-create'),
    path('api/rollcall/', rollcall.as_view(), name='rollcall')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
