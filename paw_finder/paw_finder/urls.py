"""dj110 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path, reverse_lazy


from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.internal_server_error'


urlpatterns = [
    path('', include('equipment.urls', namespace='equipment')),
    path('pages/', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
    # path('auth/', include('django.contrib.auth.urls')),
    path(r'^admin/', admin.site.urls),
    # url(r'^equipment/', include('equipment.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('blog:index'),
        ),
        name='registration',
    ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
