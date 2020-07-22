from django.conf.urls import url
from progress_report import views

urlpatterns = [
    url('', views.index, name='index'),
]