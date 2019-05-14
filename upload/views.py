from django.shortcuts import render
from django.http import HttpResponse
from upload.models import AlarmsData
from django.shortcuts import get_object_or_404, render_to_response
from django.views.decorators.csrf import requires_csrf_token



# Create your views here.
def upload_file(request):
	return render_to_response('upload/index.html')

@requires_csrf_token
def resultados(request):
	respuesta = AlarmsData.objects.filter(ev_ID=478614)
	boxes = request.POST.getlist('boxes')
	print(boxes)
	c = {}
	return render(request, 'upload/resultados.html', c)
