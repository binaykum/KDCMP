from django.shortcuts import render, HttpResponse
from complaints.models import Villagename
import csv

def complaints_records(request):
    return render(request,"complaints/complaints_list.html")

def complaints_form(request):
    return render(request,"complaints/complaints_form.html")

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
        writer.writerow([villagename.snno,villagename.villagename])  
    return response