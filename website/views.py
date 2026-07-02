from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import ContactForm, RegisterForm, ProjectForm
from .models import Event, Project , Publication


def home(request):
    return render(request, 'home.html')

def people(request):
    return render(request, 'people.html')

def facilities(request):
    return render(request, 'facilities.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def events(request):
    today = timezone.now().date()
    upcoming = Event.objects.filter(date__gte=today).order_by('date')
    past = Event.objects.filter(date__lt=today).order_by('-date')
    return render(request, 'events.html', {
        'upcoming': upcoming,
        'past': past,
    })

def projects(request):
    approved_projects = Project.objects.filter(status='approved').order_by('-submitted_at')
    return render(request, 'projects.html', {'projects': approved_projects})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('projects')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('submit_project')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('submit_project')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('submit_project')
        else:
            messages.error(request, 'Invalid email or password.')
    response = render(request, 'login.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate'
    return response

def logout_view(request):
    logout(request)
    return redirect('projects')

@login_required(login_url='login')
def submit_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.submitted_by = request.user
            project.save()
            messages.success(request, 'Project submitted! It will appear after approval.')
            return redirect('submit_project')
    else:
        form = ProjectForm()
    return render(request, 'submit_project.html', {'form': form})

def publications(request):
    pub_type = request.GET.get('type', '')
    year = request.GET.get('year', '')
    
    pubs = Publication.objects.all()
    
    if pub_type:
        pubs = pubs.filter(pub_type=pub_type)
    if year:
        pubs = pubs.filter(year=year)
    
    years = Publication.objects.values_list('year', flat=True).distinct().order_by('-year')
    
    return render(request, 'publications.html', {
        'publications': pubs,
        'years': years,
        'selected_type': pub_type,
        'selected_year': year,
    })

def research(request):
    return render(request, 'research.html')

def landing(request):
    return render(request, 'landing.html')


from .models import BodhiShalaPublication
from .forms import BodhiShalaContactForm

def bodhishala_home(request):
    return render(request, 'bodhishala_home.html')

def bodhishala_research(request):
    return render(request, 'bodhishala_research.html')

def bodhishala_people(request):
    return render(request, 'bodhishala_people.html')

def bodhishala_facilities(request):
    return render(request, 'bodhishala_facilities.html')

def bodhishala_publications(request):
    pub_type = request.GET.get('type', '')
    year = request.GET.get('year', '')

    pubs = BodhiShalaPublication.objects.all()

    if pub_type:
        pubs = pubs.filter(pub_type=pub_type)
    if year:
        pubs = pubs.filter(year=int(year))

    years = BodhiShalaPublication.objects.values_list('year', flat=True).distinct().order_by('-year')

    return render(request, 'bodhishala_publications.html', {
        'publications': pubs,
        'years': years,
        'selected_type': pub_type,
        'selected_year': year,
    })

def bodhishala_contact(request):
    if request.method == 'POST':
        form = BodhiShalaContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
            return redirect('bodhishala_contact')
    else:
        form = BodhiShalaContactForm()
    return render(request, 'bodhishala_contact.html', {'form': form})