from django.shortcuts import render
from complaints.models import Villagename,Complaints
from complaints.forms import complaints_form, village_form
from django.contrib import messages
import csv
from django.http import HttpResponseRedirect, HttpResponse

def complaints_records(request):
    obj= Complaints.objects.all
    return render(request,"complaints/complaints_list.html", {'complainllist': obj})

def complaints_form1(request):
    if request.method == 'POST':
        form= complaints_form(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, 'form saved ')
                return HttpResponseRedirect('#')
         
            except:
                messages.success(request, ' from')
            
    else:
        form = complaints_form
        messages.success(request, 'exception from elsse')
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

# follwing function not used as of now
def complaints_form2(request):
    if request.method == "GET" :
        form = village_form
        messages.success(request, 'exception from elsse')
        return render(request,"complaints/complaints_form.html", {'form': form})

    else:
        form= village_form(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, 'form saved ')
                
                print ("reeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
                return HttpResponseRedirect('#')
         
            except:
                messages.success(request, ' from except')
            
    
            