from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Service, Photo
from .forms import ContactForm
from django.core.mail import send_mail
import json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm
from django.views.decorators.csrf import csrf_exempt
import os


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
            messages.success(request, f"{subject.title()}, Ваши данные успешно отправленны!")
            return HttpResponseRedirect(reverse("service:index"))
    else:
        form = ContactForm()
    return render(request, 'service/send_data.html', {'form': form, 'sent': sent})

@csrf_exempt
def generate_pdf(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Создаем HTTP response с типом PDF
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="calculation-results.pdf"'
            
            # Создаем PDF документ
            p = canvas.Canvas(response, pagesize=A4)
            
            # Используем стандартный шрифт
            p.setFont('Helvetica', 14)
            
            # Добавляем заголовок
            p.setFontSize(24)
            p.drawString(2*cm, 27*cm, "Raschet stoimosti mokrogo fasada")
            
            # Добавляем линию под заголовком
            p.line(2*cm, 26.7*cm, 19*cm, 26.7*cm)
            
            # Устанавливаем шрифт для основного текста
            p.setFontSize(12)
            
            # Добавляем информацию о расчете
            y = 24
            p.drawString(2*cm, y*cm, f"Ploshchad fasada: {data.get('area', 'Ne ukazano')} m2")
            y -= 1.5
            
            # Преобразуем тип штукатурки в читаемый вид
            plaster_types = {
                'ceresit': 'Ceresit',
                'knauf': 'Knauf',
                'weber': 'Weber'
            }
            plaster_type = plaster_types.get(data.get('plasterType', ''), data.get('plasterType', 'Ne ukazano'))
            p.drawString(2*cm, y*cm, f"Marka shtukaturki: {plaster_type}")
            y -= 1.5
            
            # Преобразуем тип утепления в читаемый вид
            insulation_types = {
                'none': 'Bez utepleniya',
                'mineral': 'Mineralnaya vata',
                'penoplast': 'Penoplast',
                'stone': 'Kamennaya vata',
                'basalt': 'Bazaltovaya vata',
                'extruded': 'Ekstrudirovannyj penoplast'
            }
            
            insulation_type = data.get('insulationType', 'none')
            if insulation_type != 'none':
                readable_type = insulation_types.get(insulation_type, insulation_type)
                p.drawString(2*cm, y*cm, f"Tip utepleniya: {readable_type}")
                y -= 1.5
                p.drawString(2*cm, y*cm, f"Tolshchina utepleniya: {data.get('insulationThickness', 'Ne ukazano')} mm")
                y -= 1.5
            
            # Добавляем разделительную линию
            y -= 1
            p.line(2*cm, y*cm, 19*cm, y*cm)
            
            # Добавляем результаты расчета
            y -= 2
            p.setFontSize(14)
            p.drawString(2*cm, y*cm, "Rezultaty rascheta:")
            p.setFontSize(12)
            
            y -= 1.5
            p.drawString(2*cm, y*cm, f"Neobhodimoe kolichestvo shtukaturki: {data.get('materialsNeeded', '0')} kg")
            y -= 1.5
            p.drawString(2*cm, y*cm, f"Stoimost shtukaturki: {data.get('plasterCost', '0')} rub.")
            y -= 1.5
            p.drawString(2*cm, y*cm, f"Stoimost utepleniya: {data.get('insulationCost', '0')} rub.")
            y -= 1.5
            p.drawString(2*cm, y*cm, f"Obshchaya stoimost: {data.get('totalCost', '0')} rub.")
            
            # Добавляем нижний колонтитул
            p.setFontSize(10)
            p.drawString(2*cm, 2*cm, "hamzasad")
            p.drawString(2*cm, 1.5*cm, "Tel: +7 (999) 184-20-80")
            
            # Сохраняем PDF
            p.showPage()
            p.save()
            
            return response
            
        except Exception as e:
            return HttpResponse(f"Oshibka pri sozdanii PDF: {str(e)}", status=500)
            
    return HttpResponse('Method not allowed', status=405)
