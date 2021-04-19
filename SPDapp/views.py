from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def custinfo(request):
    return render(request, "cust_info.html")
