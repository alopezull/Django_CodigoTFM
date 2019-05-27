from .models import FiltersDevices
import pandas as pd

def data_filters(dev):
	if dev=="BIG_DIPPER":
		dev="Monitor Mindray"
	if ((dev=="Alaris GH") or (dev=="Alaris CC_G") or (dev=="Alaris_GP") or (dev=="Alaris GH_G")):
		dev="Bombas Alaris"
	if dev=="Respironics":
		dev="Respironics"
	if dev=="Servo":
		dev="ServoI/U"
	if dev=="PrismaFlex":
		dev="PrismaFlex"
	df_filters = pd.DataFrame.from_records(FiltersDevices.objects.filter(Device_Type__contains=dev).values().distinct())
	return df_filters