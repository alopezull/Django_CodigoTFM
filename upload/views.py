from django.shortcuts import render
from django.http import HttpResponse
from upload.models import AlarmsData
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.decorators.csrf import requires_csrf_token
from django.template import RequestContext
from upload.form import prueba1
from django.utils import timezone


# Create your views here.
def upload_file(request):
	return render_to_response('upload/index.html')

def resultados(request):
	respuesta = AlarmsData.objects.filter(ev_ID=478614)
	boxes = request.POST.getlist('boxes')
	print(boxes)
	c = {}
	return render(request, 'upload/resultados.html', c)

def prueba1(request):
	form = prueba1()
	return render(request,'upload/prueba1.html',{'form':form})
