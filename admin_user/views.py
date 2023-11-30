from django.shortcuts import render , redirect , get_object_or_404
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from .forms import Messages
from .models import Mensaje, Calendario, UserProfile, Eventos
from django.http import JsonResponse
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.shortcuts import render



def inicio(request):
    return render(request, 'admin/inicio.html')


# Vista que muestra los mensajes del inbox
def inbox(request):
    messages = Mensaje.objects.raw('select b.id , a.nombre,a.correo,b.asunto,b.mensaje,b.creado from admin_user_userprofile a,admin_user_mensaje b where a.nombre = remitente_id')
    print(messages)
    return render(request,'admin/inbox.html',{'messages': messages})

# Vista que envia el mensaje del formulario 
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

def eliminar_mensaje(request):
    if request.method == 'POST':
        id = request.POST['message_id']
        msg = get_object_or_404(Mensaje, pk=id)
        msg.delete()
        return redirect('inbox')


# Vista para responder y enviar el mensaje
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
    pass

def calendar(request):
    all_calendar = Calendario.objects.all()
    context = {
        "calendar" : all_calendar
    }
    return render(request, 'admin/calendario.html', context)

def all_calendar(request):
    all_calendar = Calendario.objects.all()
    out = []
    for event in all_calendar:
        out.append({
            'title' : event.nombre,
            'id' : event.id,
            'start' : event.fechayhora.strftime("%m/%d/%Y %H:%M:%S"),
        })
    return JsonResponse(out, safe = False)
