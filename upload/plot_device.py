from .models import AlarmsData
import pandas as pd
from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def plot_devices(alarms):
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax1=fig.add_subplot(1,1,1)
	ax1.set_xlabel('Dispositivo')
	ax1.set_ylabel('Total Alarmas')
	ax1.set_title('Total alarmas por dispositivo')
	alarms.plot(kind='bar')
	canvas = FigureCanvasAgg(fig)
	response = HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return (response)