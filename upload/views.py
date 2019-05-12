from django.shortcuts import render
from django.http import HttpResponse
from upload.models import AlarmsData
from django.shortcuts import get_object_or_404, render_to_response


# Create your views here.
def upload_file(request):
	return render_to_response('upload/index.html')

def resultados(request):
	respuesta = AlarmsData.objects.filter(ev_ID=478614)
	return render_to_response('upload/resultados.html', {'respuesta':respuesta})


