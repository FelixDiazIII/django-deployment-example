from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'name': 'Felix Gangca Diaz', 'emp_id':102146944}
    return render(request, 'basic_app/index.html', context_dict)

def other(request):
    return render(request, 'basic_app/other.html', {'welcome': 'Other Page'})

def base(request):
    return render(request, 'basic_app/base.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
