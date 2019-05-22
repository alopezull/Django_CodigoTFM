from django.shortcuts import render
from django.http import HttpResponse
from upload.models import AlarmsData, FiltersDevices
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.decorators.csrf import requires_csrf_token
from django.template import RequestContext
from upload.form import inicial
import pandas as pd
from . import dataframe_db_alarms, dataframe_db_filters, filter_data
from datetime import datetime


# Create your views here.
def upload_file(request):
	return render_to_response('upload/index2.html')

def resultados(request):
	# Recogemos los datos del formulario
	form  = inicial(request.POST)
	data = request.POST.copy()
	c = data.get('check_box')
	#box = data.get('boxes')
	e=data.get('check_devices')
	#dev=data.get('devices')
	# Para las fechas, obtenemos valor DIA, MES y AÑO por separado
	fechaI_day=data['fechaInicial_day']
	fechaI_month=data['fechaInicial_month']
	fechaI_year=data['fechaInicial_year']
	fechaF_day=data['fechaFinal_day']
	fechaF_month=data['fechaFinal_month']
	fechaF_year=data['fechaFinal_year']
	# Los agrupamos como fecha (Y/m/d)
	fechaInicial=fechaI_year+'/'+fechaI_month+'/'+fechaI_day
	dateInicial=datetime.strptime(fechaInicial, '%Y/%m/%d').date()
	fechaFinal=fechaF_year+'/'+fechaF_month+'/'+fechaF_day
	dateFinal=datetime.strptime(fechaFinal, '%Y/%m/%d').date()
	# 
	#df=dataframe_db_alarms(AlarmsData)
	#prueba=df.head()
	# x=range(1,11)
	# prueba=plot_device(x)
	prueba = dataframe_db_alarms(dateInicial, dateFinal, c, e)[:5]

	return render(request, 'upload/resultados.html', {'dateInicial':dateInicial, 'data':data, 'c':c, 'e':e, 'prueba':prueba})

def index(request):
	form = inicial()
	return render(request,'upload/index.html',{'form':form})
