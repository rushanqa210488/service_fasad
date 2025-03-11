from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.service_detail, name='service_detail'),
    path('calculate/', views.calculate_fasad, name='calculate'),
    path('photos/', views.show_photos, name='photos'),
    path('contact_data/', views.send_contact_data, name='contact_data'),
]
