from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import authentication, permissions
import math

from frecognition.models import Clases
from frecognition.models import Alumno
from frecognition.models import Embedding

from .serializers import ClasesSerializer
from .serializers import AlumnoSerializer
from .serializers import EmbeddingSerializer
from .serializers import RollcallSerializer

class ClaseGetAPIView(generics.ListAPIView):
	queryset = Clases.objects.all()
	serializer_class = ClasesSerializer
	permission_classes = []
	authentication_classes = []

class ClaseCreateAPIView(generics.CreateAPIView):
	queryset = Clases.objects.all()
	serializer_class = ClasesSerializer
	permission_classes = []
	authentication_classes = []

class AlumnoGetAPIView(generics.ListAPIView):
	queryset = Alumno.objects.all()
	serializer_class = AlumnoSerializer
	permission_classes = []
	authentication_classes = []

class AlumnoCreateAPIView(generics.CreateAPIView):
	queryset = Alumno.objects.all()
	serializer_class = AlumnoSerializer
	permission_classes = []
	authentication_classes = []

class EmbeddingGetAPIView(generics.ListAPIView):
	queryset = Embedding.objects.all()
	serializer_class = EmbeddingSerializer
	permission_classes = []
	authentication_classes = []

class EmbeddingCreateAPIView(generics.CreateAPIView):
	queryset = Embedding.objects.all()
	serializer_class = EmbeddingSerializer
	permission_classes = []
	authentication_classes = []

class rollcall(APIView):
	serializer_class = RollcallSerializer
	authentication_classes = []
	permission_classes = (permissions.AllowAny,)

	def post(self, request):
		def inline_knn(alumno_vec):
			for candidato in Embedding.objects.all():
				candidato_vec = candidato.atributos

				dist = 0
				for i in range(len(alumno_vec)):
					dist += (float(candidato_vec[i]) - alumno_vec[i]) ** 2
				dist = math.sqrt(dist)

				epsilon = 0.5
				if dist < epsilon:
					return candidato.codigo_alumno
		
		alumnos = []
		embeddings = request.data['candidatos']
		for embedding in embeddings:
			alumno = inline_knn(embedding)
			if (alumno is not None):
				alumnos.append(alumno.nombre)

		print(alumnos)
		return JsonResponse({"alumnos" : alumnos})
