from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index_view(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def cv_view(request):
    template = loader.get_template('all_cv_items.html')
    return HttpResponse(template.render())

def work_history_view(request):
    template = loader.get_template('work_history.html')
    return HttpResponse(template.render())

def education_view(request):
    template = loader.get_template('education.html')
    return HttpResponse(template.render())

def certifications_view(request):
    template = loader.get_template('certifications.html')
    return HttpResponse(template.render())

def skills_view(request):
    template = loader.get_template('skills.html')
    return HttpResponse(template.render())

def projects_view(request):
    template = loader.get_template('projects.html')
    return HttpResponse(template.render())

def references_view(request):
    template = loader.get_template('references.html')
    return HttpResponse(template.render())

def contact_view(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def blog_view(request):
    template = loader.get_template('blog.html')
    return HttpResponse(template.render())

def testing_view(request):
    template = loader.get_template('testing.html')
    return HttpResponse(template.render())