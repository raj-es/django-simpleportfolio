from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.


def home(request):
    # return HttpResponse("This is my home page")
    return render(request, "home.html")


def about(request):
    # return HttpResponse("This is my home page")
    return render(request, "about.html")


def projects(request):
    # return HttpResponse("This is my home page")
    return render(request, "projects.html")


def contact(request):
    # return HttpResponse("This is my home page")
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "contact.html")
