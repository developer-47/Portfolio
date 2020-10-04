from django.shortcuts import render, get_object_or_404
from .models import Work

def works(request):
    works = Work.objects.all()
    return render(request, 'works/works.html', {'works': works})

def work(request, works_id):
    work = get_object_or_404(Work, pk = works_id)
    return render(request, 'works/work.html', {'work': work})    