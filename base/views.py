from django.shortcuts import render
from .models import Escort,Area
# Create your views here.


def index(request):
    escorts = Escort.objects.all()
    locations = Area.objects.all()
    context={'escorts':escorts,'locations':locations}
    return render(request,'base/index.html',context)


def individual_escort(request,pk):
    escort = Escort.objects.get(id=pk)
    context = {'escort':escort}
    return render(request, 'base/escort.html',context)