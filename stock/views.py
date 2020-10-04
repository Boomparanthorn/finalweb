from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')
def addblog(request):
    Fristname=request.GET['Fristname']
    Lastname=request.GET['Lastname']
    Email=request.GET['Email']
    Main=request.GET['Main']
    Main2=request.GET['Main2']
    city=request.GET['city']
    zip=request.GET['zip']

    return render(request, 'frontend/result.html',{'Fristname':Fristname, 'Lastname':Lastname, 
 'Email':Email, 'Main':Main, 'Main2':Main2, 'city':city, 'zip':zip})
