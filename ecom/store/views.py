from django.shortcuts import render
from store.models import Student

# Create your views here.
def show_data(request):
    all=Student.objects.all()
    return render(request,'show_data.html',{'all':all})