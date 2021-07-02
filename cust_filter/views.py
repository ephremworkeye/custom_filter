from django.shortcuts import render

# Create your views here.

def index(request):
    names = 'abiy,demeke,Gedu,Tola'
    return render(request, 'index.html', {'names':names})