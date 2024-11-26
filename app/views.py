from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def kalpa(request):
    return HttpResponse('she is a software tester')

def siri(request):
    return HttpResponse('<h1> HI SIRI HOW ARE YOU</h1>')
def prabhas(request):
    return HttpResponse('<h1>PRABHAS</h1><i>HOLLYWOOD ACTOR</i><br><img src=''https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRap6tBSWs8w6dcd7g5yULwwe6_GwK81LX1P4g6Mp-1jPhGxqxJL14b6KkhJLh8C_1cJB4eTmm-mRSmQkoXF2oAF_0IqMKfj33Ga7b5Nw>')
def anu(request):
    return HttpResponse('<marquee>she is a software tester</marquee>')