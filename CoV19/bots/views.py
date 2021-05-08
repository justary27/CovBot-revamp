from django.shortcuts import render

# Create your views here.
def bots(request):
    return render(request,'chatbots/bots.html')
