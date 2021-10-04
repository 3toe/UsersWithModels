from django.shortcuts import render, redirect
from .models import Users

def index(request):
   context = {
      "Userbase" : Users.objects.all()
   }
   return render(request, "index.html", context)

def process(request):
   if request.POST['fname'] == "" or request.POST['lname'] == "" or request.POST['email'] == "" or request.POST['age'] == "":
      return redirect('/')
   Users.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email_address = request.POST['email'], age = request.POST['age'])
   return redirect('/')