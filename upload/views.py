from django.shortcuts import render
from django.http import HttpResponse
from upload.models import AlarmsData
from django.shortcuts import get_object_or_404, render_to_response
from django.views.decorators.csrf import requires_csrf_token
from django.template import RequestContext
from upload.form import inicial


# Create your views here.
def upload_file(request):
	return render_to_response('upload/index2.html')

def resultados(request):
	form  = inicial(request.POST)
	data = request.POST.copy()
	c = data.getlist('check_box')
	box = data.get('boxes')
	return render(request, 'upload/resultados.html', {'box':box, 'c':c})

def index(request):
	form = inicial()
	return render(request,'upload/index.html',{'form':form})
