from django import forms

BOX_CHOICES = (
	('box1','BOX 1'), 
	('box2','BOX 2'),
	('box3','BOX 3'),
	('box4','BOX 4'),
	('box5','BOX 5'),
	('box6','BOX 6'),
	('box7','BOX 7'), 
	('box8','BOX 8'),
	('box9','BOX 9'),
	('box10','BOX 10'),
	('box11','BOX 11'),
	('box12','BOX 12'),
	('box13','BOX 13'), 
	('box14','BOX 14'),
	('box15','BOX 15'),
	('box16','BOX 16'),
	('box17','BOX 17'),
	('box18','BOX 18'),
	('box19','BOX 19'), 
	('box20','BOX 20'),
	('box21','BOX 21'),
	('box22','BOX 22'),
	('box23','BOX 23'),
	('box24','BOX 24'),
	)

DEVICES_CHOICES = (
	('MonitorMindray','Monitor Mindray'), 
	('BombasAlaris','Bombas Alaris'),
	('Otros','Otros'),)

class inicial(forms.Form):
	fechaInicial=forms.DateField(label='Fecha Inicial', widget=forms.SelectDateWidget)
	fechaFinal=forms.DateField(label='Fecha Final', widget=forms.SelectDateWidget)
	check_box = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
		choices=BOX_CHOICES)
	check_devices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
		choices=DEVICES_CHOICES)

