from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student


def add_show(request):             
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm=StudentRegistration()    
    else:
        fm=StudentRegistration()
    stud=Student.objects.all()
    return render(request,"crud/addandshow.html",{'form':fm,'stu':stud})

def delete(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
def update(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Student.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)    
    return render(request,"crud/update.html",{'form':fm})
