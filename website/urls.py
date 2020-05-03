from . import views
from django.urls import path

app_name = "website"

urlpatterns = [
    path('',views.index,name='index'), # {% url 'website:index' %}
    #about
    path('about/',views.about,name='about'), # {% url 'website:about' %}
    #contact
    path('contact/',views.contact,name='contact'), #{% url 'website:contact' %}

]