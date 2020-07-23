from django.shortcuts import render, redirect
from django.core.validators import EmailValidator
from .models import Contact, NewsLetter, Presentation, SiteInfo, SocialAccount, Team
from .forms import ContactForm
# Create your views here.
def index(request):
    
    data = {
        
    }
    
    return render(request, 'pages/index.html', data)

def about(request):
    
    presentation = Presentation.objects.filter(status=True)[:2]
    team = Team.objects.filter(status=True)[:4]
    social = SocialAccount.objects.filter(status=True)[:4]

    data = {
        'presentation' : presentation,
        'team' : team,
        'social' : social,
    }
    
    return render(request, 'pages/about.html', data)

def contact(request):

    presentation = Presentation.objects.filter(status=False).last
    social = SocialAccount.objects.filter(status=True)[:4]

    contact_form = ContactForm(request.POST or None)
    
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
            contact_form = ContactForm()

    data = {
        'presentation' : presentation,
        'social' : social,
        'contact_form': contact_form
    }
    
    return render(request, 'pages/contacts.html', data) 

def news_letter(request):
    if request.method == 'POST':
        newsletter = request.POST.get('newsletter')
        if newsletter:
            nl = NewsLetter.objects.create(email=newsletter)
            nl.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))         