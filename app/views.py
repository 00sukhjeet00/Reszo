from django.shortcuts import render, redirect
from app.models import *
from django.conf import settings
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html')


def menu(request):
    menus = Menu.objects.all()
    return render(request, 'menu.html', {'menus': menus})


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})


def bookReservation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        day = request.POST.get('day')
        hour = request.POST.get('hour')
        persons = request.POST.get('persons')
        booked = Reservation(name=name, email=email,
                             day=day, hour=hour, person=persons)
        booked.save()
    return redirect('index')


def subcribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        add_email = Subcribe(email=email)
        add_email.save()
        subject = 'Reszo'
        message = f'Thank you for Subcribing to Reszo.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['mail@gmail.com']
        send_mail(subject, message, email_from, recipient_list)

    return redirect('index')


def contact(request):
    return render(request, 'contact.html')


def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        upload = Feedback(name=name, email=email, phone=phone, message=message)
        upload.save()
    return redirect('index')
