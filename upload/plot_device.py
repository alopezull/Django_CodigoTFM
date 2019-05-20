from .models import AlarmsData, 
import pandas as pd
from matplotlib.backends_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure



def plot_devices(request):
	fig=Figure()
	ax=fig.add_subplot(111)
	ax1=fig.add_subplot(1,1,1)
	ax1.set_xlabel('Dispositivo')
	ax1.set_ylabel('Total Alarmas')
	ax1.set_title('Total alarmas por dispositivo')
	alarms.plot(kind='bar')
	# Guardamos la imagen en un buffer
	canvas = FigureCanvas(fig)
	response=django.http.HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return (response)