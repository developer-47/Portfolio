from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    if request.method == 'GET':
        return render(request, 'contact/contact.html', {'form': ContactForm()})
    else:
        try:
            form = ContactForm(request.POST)
            form.save()
            return render(request, 'contact/contact.html', {'form': ContactForm(), 'info': 'Data Captured'})
        except ValueError:
            return render(request, 'contact/contact.html', {'form': ContactForm(), 'info': 'Error generated, Please try again'})
  
