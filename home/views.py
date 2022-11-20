import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import ContactForm
from .models import (
    Slider,
    Service,
    WorkCounter,
    Project,
    Testimonial,
    Team,
    Contact
)
from django.conf import settings
from django.db.models import Q
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    """
    :param request:
    :return:
    """
    slider = Slider.objects.order_by('-timestamp')[:1]
    service = Service.objects.all()
    work_counter = WorkCounter.objects.all()[:1]
    project = Project.objects.all()
    testimonial = Testimonial.objects.all()
    team = Team.objects.all()[:5]

    # Contact Form
    form = ContactForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Success! Thank you for your message.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if form.errors:
        errors = form.errors

    context = {
        'slider': slider,
        'service': service,
        'work_counter': work_counter,
        'project': project,
        'team': team,
        'testimonial': testimonial,
        'form': form,
        'errors': errors
    }

    return render(request, "home/home.html", context)


def contact_csv_download(request):
    """
    Download CSV files
    :param request:
    :return:
    """
    queryset = Contact.objects.all()
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow([
        'ID', 'Subject', 'Full Name', 'E-mail', 'Phone', 'Message'
    ])
    for q in queryset:
        row = []
        row.extend([
            q.id, q.subject, q.name, q.email, q.phone, q.message
        ])
        writer.writerow(row[:])

    response['Content-Disposition'] = 'attachment; filename="contact-list.csv"'
    return response
