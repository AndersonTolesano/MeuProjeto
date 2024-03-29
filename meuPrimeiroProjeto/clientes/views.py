from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm

def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})

def persons_new(request):
    form = PersonForm(request.POST or request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


def persons_update(request, id):
    persons = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=persons)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


