from django.http import HttpResponse
from django.shortcuts import render

from .models import Place, SpecialThanks


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=SpecialThanks.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})