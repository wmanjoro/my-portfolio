from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name = 'index_view'),
    path('cv/', views.cv_view, name = 'cv_view'),
    path('cv/work_history/', views.work_history_view, name = 'work_history_view'),
    path('cv/education/', views.education_view, name = 'education_view'),
    path('cv/certifications/', views.certifications_view, name = 'certifications_view'),
    path('cv/skills/', views.skills_view, name = 'skills_view'),
    path('cv/projects/', views.projects_view, name = 'projects_view'),
    path('cv/references/', views.references_view, name = 'references_view'),
    path('cv/contact/', views.contact_view, name = 'contact_view'),
    path('cv/blog/', views.blog_view, name = 'blog_view'),
    path('cv/testing/', views.testing_view, name = 'testing_view'),

]