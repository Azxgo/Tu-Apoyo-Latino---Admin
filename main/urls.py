"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth.decorators import login_required
from admin_user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', login_required(views.inicio), name='inicio'),
    path('inbox/', views.inbox, name='inbox'),
    path('activity/', views.activity, name='activity'),
    path('calendar/', views.calendar, name = 'calendar'),
    path('form/',views.enviar_mensaje, name="form"),
    path('responder',views.responder_mensaje,name='responder_mensaje')
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)

admin.site.index_title = "Panel de Control"
admin.site.site_title = "Tu Apoyo Latino"