from django.shortcuts import render, HttpResponse

def complaints_records(request):
    return render(request,"complaints/complaints_list.html")

def complaints_form(request):
    return render(request,"complaints/complaints_form.html")

def complaints_delete(request):
    return     

def test(request):
    return HttpResponse("abhinav")