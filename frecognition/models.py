from django.db import models
from django.contrib.postgres.fields import ArrayField
import psycopg2
# Create your models here.

connection = psycopg2.connect(user = "facerecognition",password = "facerecognition.1234",host = "107.180.91.147",
                                port = "5432",
                                database = "facerecognitiondb")
cursor= connection.cursor()


class Image(models.Model):
    image = models.ImageField(upload_to="images")


class Clases(models.Model):
	codigo=models.CharField(max_length=30,primary_key=True)
	nombre=models.CharField(max_length=30)
	seccion=models.IntegerField()

class Alumno(models.Model):
	codigo=models.IntegerField(primary_key=True)
	nombre=models.CharField(max_length=30)
	foto=models.ImageField()
	clases = models.ManyToManyField(Clases, verbose_name="clases")


class Profesor(models.Model):
	codigo=models.IntegerField(primary_key=True)
	nombre=models.CharField(max_length=30)
	ususario=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	clases = models.ManyToManyField(Clases, verbose_name="clases")

class Admin(models.Model):
	ususario=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	role=models.CharField(max_length=30)

class Asistencia(models.Model):
	codigo=models.CharField(max_length=30,primary_key=True)
	nombre_profesor=models.CharField(max_length=50)
	nombre_clase=models.CharField(max_length=50)
	fecha=models.DateField()



class Embedding(models.Model):
	codigo=models.IntegerField(primary_key=True)
	atributos= ArrayField(models.DecimalField(max_digits=22, decimal_places=18))