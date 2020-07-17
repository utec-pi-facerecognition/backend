from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import authentication, permissions
import math
from datetime import date

from frecognition.models import Clases
from frecognition.models import Alumno
from frecognition.models import Profesor
from frecognition.models import Embedding
from frecognition.models import Asistencia

from .serializers import ClasesSerializer
from .serializers import AlumnoSerializer
from .serializers import ProfesorSerializer
from .serializers import AsistenciaSerializer
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

class ClaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clases.objects.all()
    serializer_class = ClasesSerializer

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

class AlumnoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Alumno.objects.all()
	serializer_class = AlumnoSerializer

class ProfesorGetAPIView(generics.ListAPIView):
	queryset = Profesor.objects.all()
	serializer_class = ProfesorSerializer

class ProfesorCreateAPIView(generics.CreateAPIView):
	queryset = Profesor.objects.all()
	serializer_class = ProfesorSerializer

class ProfesorDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Profesor.objects.all()
	serializer_class = ProfesorSerializer


class AsistenciaGetAPIView(generics.ListAPIView):
	queryset = Asistencia.objects.all()
	serializer_class = AsistenciaSerializer

class AsistenciaCreateAPIView(generics.CreateAPIView):
	queryset = Asistencia.objects.all()
	serializer_class = AsistenciaSerializer

class AsistenciaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Asistencia.objects.all()
	serializer_class = AsistenciaSerializer
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
	def get(self, request):
		clase = Clases.objects.filter(codigo=request.data['course'])[0]
		today = date.today()
		asistentes = []
		alumnos = request.data['alumnos']
		asistencia_en_clase = Asistencia.objects.filter(fecha = today).filter(codigo_clase = clase)
		for alumno in alumnos:
			if (asistencia_en_clase.filter(codigo_alumno = alumno)) > 0:
				asistentes.append(1)
			else:
				asistentes.append(0)
		return JsonResponse({"alumnos" : asistentes})

	def post(self, request):
		print("IN POST")
		print("option", request.data['option'])
		option = request.data['option'] == 0
		if option:
			clase = Clases.objects.filter(codigo=request.data['course'])[0]
			today = date.today()
			def inline_knn(alumno_vec):
				best = 0.5
				bestcandidato = None
				for candidato in Embedding.objects.all():
					candidato_vec = candidato.atributos

					dist = 0
					for i in range(len(alumno_vec)):
						dist += (float(candidato_vec[i]) - alumno_vec[i]) ** 2
					dist = math.sqrt(dist)
					if dist < best:
						best = dist
						bestcandidato = candidato.codigo_alumno
				epsilon = 0.5
				if best < epsilon:
					return bestcandidato
			alumnos = []
			embeddings = request.data['candidatos']
			for embedding in embeddings:
				alumno = inline_knn(embedding)
				if (alumno is not None and len(alumno.clases.filter(codigo=clase.codigo)) == 1):
					asistencia = Asistencia(codigo = str(clase.codigo)+str(today)+str(alumno.codigo), codigo_alumno = alumno, codigo_clase = clase, fecha = today)
					asistencia.save()
					alumnos.append(True)
				else:
					alumnos.append(False)
			print("--------------------------------------------------")
			print(alumnos)
			print("-------------------------------------------------")
			return JsonResponse({"alumnos" : alumnos})
		else:
			print(request.data)
			clase = Clases.objects.filter(codigo=request.data['course'])[0]
			today = date.today()
			asistentes = []
			alumnos = request.data['alumnos']
			asistencia_en_clase = Asistencia.objects.filter(fecha = today).filter(codigo_clase = clase)
			for id in alumnos:
				# alumno = Alumno.objects.filter(codigo = id)
				if (asistencia_en_clase.filter(codigo_alumno = id)):
					asistentes.append(True)
				else:
					asistentes.append(False)
			print("--------------------------------------------------")
			print(asistentes)
			print("-------------------------------------------------")
			return JsonResponse({"alumnos" : asistentes})
