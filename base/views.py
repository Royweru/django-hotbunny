from django.shortcuts import render
from .models import Escort
# Create your views here.


def index(request):
    escorts = Escort.objects.all()
    context={'escorts':escorts}
    return render(request,'base/index.html',context)