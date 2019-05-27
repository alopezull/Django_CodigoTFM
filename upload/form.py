from django import forms

BOX_CHOICES = (
	('15','BOX U1'), 
	('16','BOX U2'),
	('26','BOX U3'),
	('24','BOX U4'),
	('25','BOX U5'),
	('30','BOX U6'),
	('31','BOX U7'), 
	('32','BOX U8'),
	('33','BOX U9'),
	('34','BOX U10'),
	('35','BOX U11'),
	('36','BOX U12'),
	('37','BOX U13'), 
	('38','BOX U14'),
	('39','BOX U15'),
	('40','BOX U16'),
	('17','BOX S17'),
	('27','BOX S18'),
	('28','BOX S19'), 
	('29','BOX S20'),
	('41','BOX U21'),
	('42','BOX U22'),
	('43','BOX U23'),
	('44','BOX U24'),
	)

DEVICES_CHOICES = (
	('BIG_DIPPER','Monitor Mindray'), 
	('Alaris','Bombas Alaris'),
	('Respironics','Respironics'),
	('Servo','ServoI/U'),
	('PrismaFlex','PrismaFlex'),)

class inicial(forms.Form):
	fechaInicial=forms.DateField(label='Fecha Inicial', input_formats= ["%d-%m-%Y"], widget=forms.SelectDateWidget)
	fechaFinal=forms.DateField(label='Fecha Final',input_formats= ["%d-%m-%Y"], widget=forms.SelectDateWidget)
	check_box = forms.ChoiceField(choices=BOX_CHOICES, required=True, label="Seleccione el box")
	check_devices = forms.ChoiceField(choices=DEVICES_CHOICES, required=True, label="Seleccione el dispositivo")

