from django.conf.urls import url
from dashboard import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<company_id>[0-9]+)/$', views.company, name='company')
]
