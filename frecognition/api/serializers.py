from rest_framework import serializers

from frecognition.models import Clases
from frecognition.models import Profesor
from frecognition.models import Alumno
from frecognition.models import Embedding
from frecognition.models import Asistencia

class ClasesSerializer(serializers.ModelSerializer):
    profesores = serializers.PrimaryKeyRelatedField(many=True, queryset=Profesor.objects.all())
    class Meta:
        model = Clases
        fields = '__all__'
    def __str__(self):
        return self.nombre
    
class AlumnoSerializer(serializers.ModelSerializer):
    clases = serializers.PrimaryKeyRelatedField(many=True, queryset=Clases.objects.all())
    class Meta:
        model = Alumno
        fields = '__all__'

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'


class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'

class EmbeddingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Embedding
		fields = ["codigo", "codigo_alumno", "atributos"]

class RollcallSerializer(serializers.Serializer):
	candidatos = serializers.ListField(
			child = serializers.ListField(
				child = serializers.DecimalField(
					max_digits = 22,
					decimal_places = 18,
					coerce_to_string = False
					)
				)
			)
