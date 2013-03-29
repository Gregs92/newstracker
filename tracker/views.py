from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render_to_response

def index(request):
	template = 'index.html'
	return render_to_response(template)


def analysis(request):
	template = 'analysis.html'
	return render_to_response(template)
	
	
def about(request):
	template = 'about.html'
	return render_to_response(template)
	
	
def error_404(request):
    template = '404.html'
    return render_to_response(request,template, {'request_path': request.path}, status=404)
     
                            
def error_500(request):
	template = '500.html'
	return render_to_response(template, context_instance = RequestContext(request))
	