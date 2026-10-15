from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name= 'core/index.html')
def about(request):
    return render(request, template_name= 'core/about.html')
def contact(request):
    return render(request, template_name= 'core/contact.html')
def sample(request):
    return render(request, template_name= 'core/sample.html')
def store(request):
    return render(request, template_name= 'core/store.html')
