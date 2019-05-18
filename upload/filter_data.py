from upload.models import AlarmsData
import pandas as pd

def filtering(alarm):
	# Filtramos los datos que no nos interesan
	alarm1 = alarm.drop(alarm[alarm['ev_DeviceName']=='AGW'].index)
	alarm2 = alarm1.drop(alarm1[(alarm1['ev_EventType']==10)|(alarm1['ev_EventType']==20)|(alarm1['ev_EventType']==30)].index)
	alarm3 = alarm2.drop(alarm2[alarm2['ev_EndEvent']==1].index)
    # Cambiar valores BedRef con la referencia real del servicio
	alarm3['BedRef'] = alarm3['BedRef'].astype(str)
	bed = {'15':'U01', '16':'U02','17':'S17','24':'U04','25':'U05','26':'U03','27':'S18','28':'S19','29':'S20','30':'U06','31':'U07','32':'U08','33':'U09','34':'U10','35':'U11','36':'U12','37':'U13','38':'U14','39':'U15','40':'U16','41':'U21','42':'U22','43':'U23','44':'U24','45':'U25','46':'U26','47':'U27','48':'U28'}
	alarm3['BedRef'] = alarm3['BedRef'].apply(lambda x:bed[x])
	# Cambiar valores ev_DeviceName con la referencia real del servicio
	disp = {'BIG_DIPPER':'Monitor Mindray', 'Respironics':'Respironics','Servo':'ServoI/ServoU','AGW':'Rack Bombas','Alaris CC_G':'Bomba Alaris','Alaris GH':'Bomba Alaris','Alaris GH_G':'Bomba Alaris','Alaris GP':'Bomba Alaris', 'PrismaFlex' : 'PrismaFlex'}
	alarm3['ev_DeviceName'] = alarm3['ev_DeviceName'].apply(lambda x:disp[x])
	return(alarm3)