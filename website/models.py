
# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Event(models.Model):
    EVENT_TYPES = [
    ('workshop', 'Workshop'),
    ('seminar', 'Seminar'),
    ('guest_lecture', 'Guest Lecture'),
    ('conference', 'Conference'),
    ('ideathon', 'Ideathon'),
    ('other', 'Other'),
]

    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='other')

    registrations = models.PositiveIntegerField(blank=True, null=True)
    attendees = models.PositiveIntegerField(blank=True, null=True)
    teams_shortlisted = models.PositiveIntegerField(blank=True, null=True)
    winning_teams = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.title} — {self.date}"

    def is_upcoming(self):
        return self.date >= timezone.now().date()
    
class Publication(models.Model):
    PUB_TYPES = [
        ('journal', 'Journal'),
        ('conference', 'Conference'),
        ('workshop', 'Workshop'),
        ('book_chapter', 'Book Chapter'),
    ]

    title = models.CharField(max_length=300)
    authors = models.CharField(max_length=300)
    venue = models.CharField(max_length=200)
    year = models.IntegerField()
    pub_type = models.CharField(max_length=20, choices=PUB_TYPES, default='journal')
    link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return f"{self.title} — {self.year}"
    


class Project(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.title} — {self.submitted_by.username}"
    



class BodhiShalaPublication(models.Model):
    PUB_TYPES = [
        ('journal', 'Journal'),
        ('conference', 'Conference'),
        ('workshop', 'Workshop'),
        ('book_chapter', 'Book Chapter'),
    ]
    title = models.CharField(max_length=300)
    authors = models.CharField(max_length=300)
    venue = models.CharField(max_length=200)
    year = models.IntegerField()
    pub_type = models.CharField(max_length=20, choices=PUB_TYPES, default='journal')
    link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return f"{self.title} — {self.year}"


class BodhiShalaContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"