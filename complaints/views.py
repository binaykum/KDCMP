from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from complaints.models import Villagename,Complaints
from complaints.forms import complaints_form
from django.contrib import messages
import csv

def complaints_records(request):
    obj= Complaints.objects.all
    return render(request,"complaints/complaints_list.html", {'complainllist': obj})

def complaints_form1(request):
    if request.method == 'POST':
        form= complaints_form(request.POST)
        if form.is_valid():
            try:
                form.save
                messages.info(request, 'changes saved')
                return HttpResponseRedirect('/list/')
         
            except:
                messages.success(request, 'exception from')
            
    else:
        form = complaints_form
        messages.success(request, 'changes not saved from else')
    return render(request,"complaints/complaints_form.html", {'form': form})

def index(request):
    return render(request,"complaints/index.html")

def complaints_delete(request):
    return     

def test(request):
    return HttpResponse("abhinav")

def getfile(request):
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    villagename = Villagename.objects.all()  
    writer = csv.writer(response)  
    for villagename in villagename:  
        writer.writerow([villagename.srno,villagename.villagename])  
    return response