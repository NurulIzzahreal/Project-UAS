from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def ArbainNawawiyah(request):
  template = loader.get_template('Hadits.html')
  return HttpResponse(template.render())

  template = loader.get_template('about.html')
  return HttpResponse(template.render())

  template = loader.get_template('galery.html')
  return HttpResponse(template.render())

  template = loader.get_template('service.html')
  return HttpResponse(template.render())