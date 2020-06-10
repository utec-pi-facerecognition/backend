from rest_framework import serializers

from frecognition.models import Clases
from frecognition.models import Alumno
from frecognition.models import Embedding

class ClasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clases
        fields = ["codigo", "nombre", "seccion"]
    def __str__(self):
        return self.nombre
    
class AlumnoSerializer(serializers.ModelSerializer):
    clases = serializers.PrimaryKeyRelatedField(many=True, queryset=Clases.objects.all())
    class Meta:
        model = Alumno
        fields = ["codigo", "nombre", "foto", "clases"]

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
