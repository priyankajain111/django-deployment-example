from django.shortcuts import render
from basicform.models import EmpInsert
from django.contrib import messages
# Create your views here.
def InsertRecord(request):
    if request.method=="POST":
        if request.POST.get('empname') and request.POST.get('email') and request.POST.get('country'):
            saverecord=EmpInsert()
            saverecord.empname=request.POST.get('empname')
            saverecord.email=request.POST.get('email')
            saverecord.country=request.POST.get('country')
            saverecord.save()
            messages.success(request,'Record Saved Successfully')
            return render(request,'index1.html')
    else:
        return render(request,'index1.html')
