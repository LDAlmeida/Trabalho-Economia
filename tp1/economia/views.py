from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Person
from .forms import PersonForm
class PersonCreateView(CreateView):
    model = Person
    fields = ('__all__')
    form = PersonForm
    
def PersonView(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("tst")
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonForm()

    return render(request, 'economia/person_form.html', {'form': form})