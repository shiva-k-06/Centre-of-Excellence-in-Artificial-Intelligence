from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('caim/', views.home, name='home'),
    path('caim/people/', views.people, name='people'),
    path('caim/research/', views.research, name='research'),
    path('caim/facilities/', views.facilities, name='facilities'),
    path('caim/contact/', views.contact, name='contact'),
    path('caim/events/', views.events, name='events'),
    path('caim/projects/', views.projects, name='projects'),
    path('caim/projects/submit/', views.submit_project, name='submit_project'),
    path('caim/register/', views.register_view, name='register'),
    path('caim/login/', views.login_view, name='login'),
    path('caim/logout/', views.logout_view, name='logout'),
    path('caim/publications/', views.publications, name='publications'),


    path('bodhishala/', views.bodhishala_home, name='bodhishala_home'),
    path('bodhishala/research/', views.bodhishala_research, name='bodhishala_research'),
    path('bodhishala/people/', views.bodhishala_people, name='bodhishala_people'),
    path('bodhishala/facilities/', views.bodhishala_facilities, name='bodhishala_facilities'),
    path('bodhishala/publications/', views.bodhishala_publications, name='bodhishala_publications'),
    path('bodhishala/contact/', views.bodhishala_contact, name='bodhishala_contact'),
]

