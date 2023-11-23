from django.shortcuts import render , redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from .forms import Messages
from .models import Mensaje


# Create your views here.
def inicio(request):
    return render(request, 'admin/inicio.html')

def inbox(request):
    messages = Mensaje.objects.raw('select a.id , a.username,a.email,b.asunto,b.mensaje,b.creado from auth_user a,admin_user_mensaje b where a.id = remitente_id')
    print(messages)
    return render(request,'admin/inbox.html',{'messages': messages})

def enviar_mensaje(request):
    if request.method == 'POST':
        form = Messages(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
    else:
        form = Messages()

    return render(request, 'admin/formprueba.html', {'form': form})

def responder_mensaje(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        asunto = request.POST['asunto']
        correo = request.POST['correo']
        mensaje = request.POST['mensaje']

        template = render_to_string('email_template.html',{
            'correo' : correo,
            'mensaje' : mensaje
        })

        correo = EmailMessage(
            asunto,
            template,
            settings.EMAIL_HOST_USER,
            [correo]
        )

        correo.fail_silently = False
        correo.send()

        messages.success(request,"Se ha enviado tu correo")
        return redirect('inbox')

def activity(request):
    return render(request, 'admin/activity.html')

def calendar(request):
    return render(request, 'admin/calendario.html')
