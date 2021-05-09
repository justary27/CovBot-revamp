from django.shortcuts import render

# Create your views here.
def bots(request):
    return render(request,'bots/bots.html')

def features(request):
    return render(request,"bots/features.html")

def commands(request):
    return render(request,"bots/commands.html")

def tutorial(request):
    return render(request,"bots/tutorial.html")