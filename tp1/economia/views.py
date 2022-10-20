from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Person
from .forms import PersonForm

def PersonView(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        print(form.errors)
        # check whether it's valid:
        if form.is_valid():
            person = Person()
            person = form.save(commit=True)
            person.prever_emprego()
            print(person.previsao)
            return render(request,'economia/person_form.html', {'form': form, 'previsao': person.previsao})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonForm()

    return render(request, 'economia/person_form.html', {'form': form})