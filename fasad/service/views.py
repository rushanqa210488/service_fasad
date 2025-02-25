from django.shortcuts import render, get_object_or_404
from .models import Service, Photo
from .forms import ContactForm
from django.core.mail import send_mail


def index(request):
    services_1 = Service.objects.filter(category__pk=1)
    services_2 = Service.objects.filter(category__pk=2)
    return render(request, 'service/index.html', {'services_1': services_1, 'services_2': services_2})


def service_detail(request, id):
    service = get_object_or_404(Service, id=id)
    services_1 = Service.objects.filter(category__pk=1)
    services_2 = Service.objects.filter(category__pk=2)
    return render(request, 'service/detail.html', {'service': service,  'services_1': services_1, 'services_2': services_2})


def calculate_fasad(request):
    services_1 = Service.objects.filter(category__pk=1)
    services_2 = Service.objects.filter(category__pk=2)
    return render(request, 'service/calculate.html', {'services_1': services_1, 'services_2': services_2})

def show_photos(request):
    services_1 = Service.objects.filter(category__pk=1)
    services_2 = Service.objects.filter(category__pk=2)
    photos = Photo.objects.all()
    return render(request, 'service/photos.html', {'services_1': services_1, 'services_2': services_2, 'photos': photos})

def send_contact_data(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['first_name']
            message = f"Имя-{cd['first_name']}, Фамилия-{cd['last_name']}, Телефон-{cd['phone']}, Почта-{cd['email']}"
            send_mail(subject, message, 'rushan210488@gmail.com', ['rushan.akhmetov@inbox.ru'])
            sent = True
    else:
        form = ContactForm()
    return render(request, 'service/send_data.html', {'form': form, 'sent': sent})
