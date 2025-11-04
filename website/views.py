from django.shortcuts import render


social_links = {
        "facebook": "https://www.facebook.com/profile.php?id=100086618873618",
        "instagram": "https://www.instagram.com/nietobariatric/",
        "whatsapp": "https://wa.me/16199049303",
        "tiktok": "https://www.tiktok.com/@nietobariatric",
    }

def index(request):
    return render(request, 'index.html', {"social": social_links})