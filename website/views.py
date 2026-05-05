import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.db.models import F
from website.forms import ContactForm
from website.models import Appointment, Contact, Review
from django.contrib.auth.decorators import login_required

from website.procedures_data.procedures import PROCEDURES

social_links = {
        "facebook": "https://www.facebook.com/profile.php?id=100086618873618",
        "instagram": "https://www.instagram.com/nietobariatric/",
        "whatsapp": "https://wa.me/14133219187", 
        "tiktok": "https://www.tiktok.com/@nietobariatric",
    }


def index(request):
    reviews = Review.objects.all().order_by("date_review")
    return render(request, 'index.html', {"social": social_links, "reviews": reviews})

def about(request):
    return render(request, 'about.html')

def sleeve(request):
    return render(request, 'procedures.html', {"p": PROCEDURES["GASTRIC_SLEEVE"]})

def endoscopic(request):
    return render(request, 'procedures.html', {"p": PROCEDURES["ENDOSCOPIC_G_SLEEVE"]})

def balloon(request):
    return render(request, 'procedures.html', {"p": PROCEDURES["GASTRIC_BALLOON"]})

def one_bypass(request):
    return render(request, 'procedures.html', {"p": PROCEDURES["ONE_ANASTOMOSIS_GASTRIC_BYPASS"]})

def roux(request):
    return render(request, 'procedures.html', {"p": PROCEDURES["ROUX_EN_Y_GASTRIC_BYPASS"]})

def bipartition(request):
    return render(request, 'procedures.html', {"p": PROCEDURES["INTESTINAL_BIPARTITION"]})

def travel(request):
    return render(request, 'travel.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def questions(request):
    return render(request, 'questions.html')

@login_required
def dashboard(request):
    pending_contacts = Contact.objects.filter(was_contacted=False, is_spam=False).order_by("-created_date")
    contacted_contacts = Contact.objects.filter(was_contacted=True, is_spam=False).order_by("-created_date")
    pending_leads = Appointment.objects.filter(was_contacted=False).order_by("-created_at")
    contacted_leads = Appointment.objects.filter(was_contacted=True).order_by("-created_at")
    return render(request, "dashboard.html", {
        "pending_leads": pending_leads,
        "contacted_leads": contacted_leads,
        "pending_contacts": pending_contacts,
        "contacted_contacts": contacted_contacts,
    })

def contact_submit(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "partials/contact_success.html")

        return render(request, "partials/contact_errors.html", {
            "form": form
        })

def appointment_create(request):
    if request.method == "POST":
        Appointment.objects.create(
            full_name=request.POST.get("full_name"),
            age=request.POST.get("age"),
            phone=request.POST.get("phone"),
            weight=request.POST.get("weight"),
            weight_unit=request.POST.get("weight_unit"),
            height=request.POST.get("height"),
            height_unit=request.POST.get("height_unit"),
            procedure_of_interest=request.POST.get("procedure_of_interest"),
            weight_to_lose=request.POST.get("weight_to_lose"),
            weight_to_lose_unit=request.POST.get("weight_to_lose_unit"),
            travel=request.POST.get("travel") == "true",
            forms_of_contact=", ".join(request.POST.getlist("forms_of_contact")),
        )
        return redirect("/")
    
def appointment_update(request):
    data = json.loads(request.body)
    appointment_id = int(data.get("id"))

    updated = Appointment.objects.filter(id=appointment_id).update(
        was_contacted=~F("was_contacted")
    )

    return JsonResponse({
        "success": bool(updated)
    })

def contact_update(request):
    data = json.loads(request.body)
    contact_id = int(data.get("id"))

    updated = Contact.objects.filter(id=contact_id).update(
        was_contacted=~F("was_contacted")
    )

    return JsonResponse({"success": bool(updated)})

def contact_spam_update(request):
    data = json.loads(request.body)
    contact_id = int(data.get("id"))

    updated = Contact.objects.filter(id=contact_id).update(
        is_spam=~F("is_spam")
    )

    return JsonResponse({"success": bool(updated)})