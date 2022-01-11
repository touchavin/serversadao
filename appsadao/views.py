from django.shortcuts import render

# Create your views here.
def index(request): #หน้า index.html
    
    return render(request, 'index.html')