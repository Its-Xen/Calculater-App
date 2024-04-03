from django.shortcuts import render

def CalApp(request):
    return render(request, 'cal.html')