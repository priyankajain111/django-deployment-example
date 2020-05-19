from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<em>My second app help not working</em>")
def help(request):
    help_dict={'help_insert':"My Help Page"}
    return render(request,'NewApp/help.html',context=help_dict)
