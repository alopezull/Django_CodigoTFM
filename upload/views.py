from django.shortcuts import render
from django.http import HttpResponse
from upload.models import AlarmsData, FiltersDevices
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.decorators.csrf import requires_csrf_token
from django.template import RequestContext
from upload.form import inicial
import pandas as pd
from . import dataframe_db_alarms, dataframe_db_filters, filter_data, filter_forms_data, filt_tract, event_total, statiscal_data, analysis_data, plot_device
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
	fechaInicial=fechaI_day+'-'+fechaI_month+'-'+fechaI_year
	dateInicial=datetime.strptime(fechaInicial, '%d-%m-%Y').strftime('%Y-%m-%d')
	fechaFinal=fechaF_day+'-'+fechaF_month+'-'+fechaF_year
	dateFinal=datetime.strptime(fechaFinal, '%d-%m-%Y').strftime('%Y-%m-%d')
	# Funciones generales para pasar los datos a dataframe y filtrar filas que no interesan
	df_alarms = dataframe_db_alarms.data_alarms()
	df_filter_alarms = filter_data.filtering(df_alarms)
	# Función para introducir filters en dataframe
	df_filters = dataframe_db_filters.data_filters()
	# Función para calcular cantidades de filtraje
	(filt1_tot, filt1_son, filt1_porcentaje, filt2_tot, filt2_son,filt2_porcentaje, filt3_tot, filt3_son, filt3_porcentaje)=filt_tract.reduccion(df_filters)
	(cant_alarms1, cant_alarms2, cant_alarms3, cant_pac0)=event_total.recuento_total(df_filter_alarms)
	# Funciones estadísticas
	(alarms_counts1, alarms_counts2, alarms_counts3, alarms_counts4)=statiscal_data.statiscal(df_filter_alarms)

	# Función para calcular datos de la busqueda a partir del forms
	(alarm_date, alarm_box, alarm_dev, alarm_tot)=filter_forms_data.filt_forms(df_filter_alarms, dateInicial, dateFinal, c, e)
	# Funciones para gráficas
	(analysis_filt1, analysis_filt2, analysis_filt3)=analysis_data.analysis(df_filter_alarms, df_filters)
	prueba=alarms_counts2
	prueba1=alarms_counts2['Cantidad']
	#grafica=plot_device.plot_devices(alarms_counts2)
	# prueba=cant_box_dev.cantidad_box_dev(prueba1,c,e)
	return render(request, 'upload/resultados.html', {'dateInicial':dateInicial, 'dateFinal':dateFinal, 'data':data, 'c':c, 'e':e, 'prueba':prueba,'prueba1':prueba1, 'filt1_tot':filt1_tot, 'filt1_son':filt1_son,'filt1_porcentaje':filt1_porcentaje, 'filt2_tot':filt2_tot, 'filt2_son':filt2_son,'filt2_porcentaje':filt2_porcentaje, 'filt3_tot':filt3_tot, 'filt3_son':filt3_son, 'filt3_porcentaje':filt3_porcentaje,'cant_alarms1':cant_alarms1 ,'cant_alarms2':cant_alarms2,'cant_alarms3':cant_alarms3, 'cant_pac0':cant_pac0, 'alarm_date':alarm_date, 'alarm_box':alarm_box, 'alarm_dev':alarm_dev, 'alarm_tot':alarm_tot, 'alarms_counts2':alarms_counts2})

def index(request):
	form = inicial()
	return render(request,'upload/index.html',{'form':form})
