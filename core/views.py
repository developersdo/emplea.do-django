# Vistas
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from models import Job, Category

class JobList(ListView):
    context_object_name = "job_list"
    queryset = Job.objects.order_by("-pub_date")
    template_name = "jobs/job_list.html"

class JobDetail(DetailView):
    model = Job
    context_object_name = "job"
    template_name = "jobs/job_details.html"

    

