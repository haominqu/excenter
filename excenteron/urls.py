"""excenteron URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^userinfo/', include('userinfo.urls')),
    url(r'^hmmqtt/', include('hmmqtt.urls')),
    url(r'^onlinemac/', include('machine.urls')),
    url(r'^index/', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^face/', include('face.urls')),
    url(r'^adminor/', include('adminor.urls')),
    url(r'^staff/', include('staff.urls')),
    url(r'^guest/', include('guest.urls')),
    url(r'^history/', include('history.urls')),
    url(r'drugcon/$', TemplateView.as_view(template_name='drugcon.html'), name='drugcon'),
# phone
    url(r'^phone/$', TemplateView.as_view(template_name="phone.html"), name='phone'),
    url(r'^phoned/', TemplateView.as_view(template_name="phoned.html"), name='phoned'),
    url(r'^phchpwd/', TemplateView.as_view(template_name="ph_change_pwd.html"), name='phchpwd'),
    url(r'^invite/', TemplateView.as_view(template_name="ph_invite.html"), name='invite'),
    url(r'^inviteadd/', TemplateView.as_view(template_name="ph_invite_add.html"), name='inviteadd'),
    url(r'^invitesuc/', TemplateView.as_view(template_name="ph_invite_success.html"), name='inviteadd'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
