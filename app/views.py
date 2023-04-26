from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def student(request):
    formdata=Student_form()
    d={'formdata':formdata}
    if request.method=='POST':
        obj=Student_form(request.POST)
        if obj.is_valid():
            obj.save()
            return HttpResponse(str(obj.cleaned_data))
        else:
            return HttpResponse('invalid')

    return render(request,'student.html',d)