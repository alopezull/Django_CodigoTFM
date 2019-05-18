from upload.models import AlarmsData
import pandas as pd
from upload.form import inicial


def analysis(AlarmsData, fechaInicial, fechaFinal, Boxes, Devices):
	# Realizamos el análisis de datos 
	form  = inicial(request.POST)
	data = request.POST.copy()
	# IF POST FECHA INICIAL/FINAL no está vacío (si está vacio--> sin filtro para FechaInicial y FechaFinal)
	if 
	fechaInicial=data.get('fechaInicial')
	fechaFinal=data.get('fechaFinal')
	respuesta = AlarmsData.objects.filter((fechaInicial>=ev_EventTime)&(fechaFinal<=ev_EventTime))
	# IF POST CHECKBOX no esstá vacío (si está vacio --> sin filtro para box)
	checkbox = data.getlist('check_box')
	box = data.get('boxes')
	checkdevices = data.getlist('check_devices')
	devices = data.get('devices')
	respuesta = AlarmsData.objects.filter((boxes==BedRef)&(devices==ev_DeviceName))


return render(request, 'upload/resultados.html', {'box':box, 'c':c, 'a':a})

	alarm3_level0={}
for x in filt3_level0.Text:
    alarm3_level0[x]=data4.ev_Description.isin([x]).sum(axis=0)
df_alarm3_lev0=pd.DataFrame.from_dict(alarm3_level0,orient='index',)

print(df_alarm3_lev0)
