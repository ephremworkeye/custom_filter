from django.shortcuts import render

# Create your views here.

def index(request):
    names = 'abiy,demeke,Gedu,Tola'
    titles = 'I wonder the 2020 races for the 1st time'
    return render(request, 'index.html', {'names':names, 'titles':titles})