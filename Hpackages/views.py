from django.shortcuts import render
from .models import TravelData

# Create your views here.
def index(request):
    post = TravelData.objects.all()
    return render(request,'index.html',{'post':post})