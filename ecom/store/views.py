from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.contrib import messages


# Create your views here.
def show_data(request):
    all=Student.objects.all()
    return render(request,'show_data.html',{'all':all})


# def insert_data(request):
#     if request.method == "POST":
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the data to the database
#             #return HttpResponse("Data saved successfully")
#             return redirect('show_data')

#         else:
#             # In case the form is invalid, you can return with the form errors
#             return render(request, 'StudentForm.html', {'form': form, 'error': 'There were errors in the form'})
#     else:
#         form = StudentForm()  # Initialize an empty form for GET request

#     # For a GET request, render the form to the user
#     return render(request, 'StudentForm.html', {'form': form})


def insert_data(request):
    if request.method == "POST":
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data saved successfully!")
            return redirect('show_data')  # Ensure 'show_data' exists in urls.py
        else:
            messages.error(request, "There were errors in the form")
    else:
        form = StudentForm()

    return render(request, 'StudentForm.html', {'form': form})
