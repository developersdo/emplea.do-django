# Vistas
from django.shortcuts import render
from django.views import generic
from models import Job, Category

class JobList(generic.ListView):
    context_object_name = "job_list"
    queryset = Job.objects.order_by("-pub_date")
    template_name = "jobs/job_list.html"

class JobDetail(generic.DetailView):
    model = Job
    context_object_name = "job"
    template_name = "jobs/job_details.html"

class JobCreate(generic.edit.CreateView):
	model = Job
	fields = ["name", "category", "place", "description", "application", 
		"company_name", "url", "email", "logo"]
	template_name = "jobs/job_form.html"
