from django.shortcuts import render
from first_project. import EmpInsert
from django.contrib import messages
from basicapp import forms
# Create your views here.
def InsertRecord(request):
    if request.method=='POST'
        if request.POST.get('empname') and request.POST.get('email') and request.POST.get('country'):
            saverecord=EmpInsert()
            saverecord.empname=request.POST.get('empname')
            saverecord.email=request.POST.get('email')
            saverecord.country=request.POST.get('country')
            saverecord.save()
            messages.success(request,'Record Saved Successfully')
            return render(request,'index1.html')
    else:
        return render(request,'basicform/index1.html')





















#def index(request):
#    return render(request,'basicapp/index.html')

#def form_name_view(request):
#    form=forms.FormName()
#    if request.method == 'POST':
#        form=forms.FormName(request.POST)
#        if form.is_valid():
#            print("NAME:"+ form.cleaned_data['name'])
#            print("EMAIL:"+ form.cleaned_data['email'])
#            print("TEXT:"+ form.cleaned_data['text'])
#    return render(request,'basicapp/form.html',{'form': form})
