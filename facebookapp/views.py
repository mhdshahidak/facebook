from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'index.html')

def Link(request):
    return render(request,'syber.html')