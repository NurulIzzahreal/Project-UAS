from django.http import HttpResponse
from django.template import loader

def ArbainNawawiyah(request):
  template = loader.get_template('Hadits.html')
  return HttpResponse(template.render())