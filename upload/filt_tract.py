from .models import FiltersDevices
import pandas as pd

def reduccion(z):
	# Recuento
	if (z.empty):
		w=print("No existen valores")
	else:
		#Primer filtraje
		filt1_tot=len(z['Tractament1'])
		w1_1=z[z['Tractament1']==1]
		w1_2=z[z['Tractament1']==2]
		wl1_1=len(w1_1)
		wl1_2=len(w1_2)
		filt1_son=wl1_1+wl1_2
		filt1_porcentaje=round((filt1_son/filt1_tot),4)
		#Segundo filtraje
		filt2_tot=len(z['Tractament2'])
		w2_1=z[z['Tractament2']==1]
		w2_2=z[z['Tractament2']==2]
		wl2_1=len(w2_1)
		wl2_2=len(w2_2)
		filt2_son=wl2_1+wl2_2
		filt2_porcentaje=round((filt2_son/filt2_tot),4)
		#Tercer filtraje
		filt3_tot=len(z['Tractament3'])
		w3_1=z[z['Tractament3']==1]
		w3_2=z[z['Tractament3']==2]
		wl3_1=len(w3_1)
		wl3_2=len(w3_2)
		filt3_son=wl3_1+wl3_2
		filt3_porcentaje=round((filt3_son/filt3_tot),4)
	return (filt1_tot, filt1_son, filt1_porcentaje, filt2_tot, filt2_son,filt2_porcentaje, filt3_tot, filt3_son, filt3_porcentaje)