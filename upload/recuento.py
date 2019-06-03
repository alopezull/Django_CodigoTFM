from .models import AlarmsData
import pandas as pd

def cuenta(x):
	# Recuento
	if (x.empty):
		y=print("No existen valores")
	else:
		y=x.count()		
	return y