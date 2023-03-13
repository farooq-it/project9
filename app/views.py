from django.shortcuts import render

# Create your views here.
def first_jinja(request):
    d={'name':'ayaan'}
    return render(request,'first_jinja.html',context=d)