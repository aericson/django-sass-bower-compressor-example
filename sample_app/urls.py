from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(
        template_name='sample.html')),
]
