from django.shortcuts import render
from .models import File
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

def home(request):
    return render(request,'home.html')
class FileCreateView(SuccessMessageMixin,CreateView): #view for create new intern(done only by internAdmin not by superuser)
    model = File
    template_name = 'file_create.html'
    fields = '__all__'
    success_message = "File created successfully"
    success_url = reverse_lazy('file_create')
class FileListView(ListView): #view for list of all interns
    model = File
    template_name = 'file_view.html'
    context_object_name = 'filelist'

# def CreateSuccess(request):
#     return render(request,"create_success.html")
