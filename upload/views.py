from django.shortcuts import render
from django.http import HttpResponse
from upload.models import AlarmsData

# Create your views here.
def upload_file(request):
	respuesta = AlarmsData.objects.filter(id=2)
	return HttpResponse(respuesta)


