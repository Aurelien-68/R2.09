from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'firstapp/index.html')

def rep(request):
    nom=request.POST["nom"]
    return render(request,'firstapp/rep.html',{"nom":nom})