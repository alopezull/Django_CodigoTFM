from django.shortcuts import render
from django.http import HttpResponse
from upload.models import AlarmsData, FiltersDevices
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.decorators.csrf import requires_csrf_token
from django.template import RequestContext
from upload.form import inicial
import pandas as pd
from datetime import datetime


# Create your views here.
def upload_file(request):
	return render_to_response('upload/index2.html')

def resultados(request):
	form  = inicial(request.POST)
	data = request.POST.copy()
	c = data.getlist('check_box')
	#box = data.get('boxes')
	e=data.getlist('check_devices')
	#dev=data.get('devices')
	fechaI_day=data['fechaInicial_day']
	fechaI_month=data['fechaInicial_month']
	fechaI_year=data['fechaInicial_year']
	fechaF_day=data['fechaFinal_day']
	fechaF_month=data['fechaFinal_month']
	fechaF_year=data['fechaFinal_year']
	fechaInicial=fechaI_year+'/'+fechaI_month+'/'+fechaI_day
	dateInicial=datetime.strptime(fechaInicial, '%Y/%m/%d').date()
	fechaFinal=fechaF_year+'-'+fechaF_month+'-'+fechaF_day

			

	return render(request, 'upload/resultados.html', {'dateInicial':dateInicial, 'data':data, 'c':c, 'e':e})

def index(request):
	form = inicial()
	return render(request,'upload/index.html',{'form':form})
