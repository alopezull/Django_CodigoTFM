from django.shortcuts import render
from django.http import HttpResponse
from upload.models import AlarmsData
from django.shortcuts import get_object_or_404, render_to_response


# Create your views here.
def upload_file(request):
	respuesta = AlarmsData.objects.filter(id=2)
	return render_to_response('upload/index.html', {'respuesta':respuesta})

def resultados(request):
	respuesta = AlarmsData.objects.filter(id=2)
	return render_to_response('upload/resultados.html', {'respuesta':respuesta})


