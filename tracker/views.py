from django.http import HttpResponse
from django.template import Template, Context, loader
from django.http import HttpResponseNotFound
from django.template import loader

def index(request):
	html = render_to_string('index.html')
	return HttpResponse(html)

def analysis(request):
	html = loader.get_template('analysis.html')
	return HttpResponse(html)
	
def about(request):
	html = loader.get_template('about.html')
	return HttpResponse(html)
	
#def custom_500(request):
#    t = loader.get_template('500.html')
#    type, value, tb = sys.exc_info(),
#   return HttpResponseServerError(t.render(Context({
#    'exception_value': value,
#})))