from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def custinfo(request):
    return render(request, "cust_info.html")

def cookie_select(request):
    return render(request, "cookie_select.html")

def my_story(request):
    return render(request, "my_story.html")

def gallery(request):
    return render(request, "gallery.html")

def menu(request):
    return render(request, "menu.html")

def faq(request):
    return render(request, "FAQ.html")

def contact(request):
    return render(request, "contact.html")

def birthday(request):
    return render(request, "birthday.html")

def celebration(request):
    return render(request, "celebration.html")

def holiday(request):
    return render(request, "holiday.html")