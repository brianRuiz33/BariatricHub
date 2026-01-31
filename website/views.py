from django.shortcuts import render
from website.forms import ContactForm
from website.models import Contact


social_links = {
        "facebook": "https://www.facebook.com/profile.php?id=100086618873618",
        "instagram": "https://www.instagram.com/nietobariatric/",
        "whatsapp": "https://wa.me/16199049303",
        "tiktok": "https://www.tiktok.com/@nietobariatric",
    }

def index(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            Contact.objects.create(
            name=form.cleaned_data["contactName"],
            email=form.cleaned_data["contactEmail"],
            phone=form.cleaned_data["contactPhone"],
            reason=form.cleaned_data["contactReason"],
            message=form.cleaned_data["contactMessage"],
        )            
            return render(request, "index.html", {
                "form": ContactForm(),
                "success": True,
                "social": social_links
            })
    return render(request, 'index.html', {"social": social_links})

def about(request):
    return render(request, 'about.html')

def sleeve(request):
    return render(request, 'gastric-sleeve.html')

def travel(request):
    return render(request, 'travel.html')
