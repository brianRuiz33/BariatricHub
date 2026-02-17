from django.shortcuts import redirect, render
from website.forms import ContactForm
from website.models import Appointment, Contact

social_links = {
        "facebook": "https://www.facebook.com/profile.php?id=100086618873618",
        "instagram": "https://www.instagram.com/nietobariatric/",
        "whatsapp": "https://wa.me/16199049303",
        "tiktok": "https://www.tiktok.com/@nietobariatric",
    }

def index(request):
    return render(request, 'index.html', {"social": social_links})

def about(request):
    return render(request, 'about.html')

def sleeve(request):
    return render(request, 'gastric-sleeve.html')

def travel(request):
    return render(request, 'travel.html')

def table_view(request):
    contacts = Contact.objects.all().order_by("-created_date")
    leads = Appointment.objects.all().order_by("-created_at")
    return render(request, "tables.html", {"leads": leads, "contacts": contacts})

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
            prev_surgeries=request.POST.get("prev_surgeries"),
            medical_conditions=request.POST.get("medical_conditions"),
            medications=request.POST.get("medications"),
            travel=request.POST.get("travel") == "true",
            forms_of_contact=", ".join(request.POST.getlist("forms_of_contact")),
        )
        return redirect("/")

    return redirect("/")