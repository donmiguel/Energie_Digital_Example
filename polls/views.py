from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def test(request):
    return HttpResponse("test")

def index(request):
    firstName = ""

    if request.POST:
        firstName = request.POST['first']
        #print("first name " + request.POST['first'])
        #return render(request, 'result.html', { 'inputFirstName' : firstName })

    return render(request, 'form.html', { 'inputFirstName' : firstName })

def login(request):
    if request.POST:
        user = request.POST['user']
        password = request.POST['password']
        print("user name " + user)
        #return render(request, 'result.html', { 'inputFirstName' : firstName })

    return render(request, 'login.html')
