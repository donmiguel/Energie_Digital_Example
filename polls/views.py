from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
import pandas as pd
import matplotlib.pyplot as plt

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


def dashboard(request):
    #load local stored file
    df = pd.read_csv('data.csv')

    #load remote stored file
    #df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')

    df = pd.DataFrame(df)
    df.plot(y=['Pulse', 'Calories'], kind='line', use_index=True)
    plt.savefig('polls/static/datalocal.png')

    #get remote data in json format
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    ext_df = pd.read_json(url)

    print(ext_df.columns)
    ext_df.plot(y='rates', kind='line', use_index=True)
    plt.savefig('polls/static/dataext.png')

    return render(request, 'data.html')