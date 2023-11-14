from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'admin/inicio.html')

def activity(request):
    return render(request, 'admin/activity.html')

def calendar(request):
    return render(request, 'admin/calendario.html')

