from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello world")
def firstpage(request):
    return render(request,'index.html')
def secpage(request):
    return render(request,'sec.html')