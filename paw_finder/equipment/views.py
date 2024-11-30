from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import TypeOfPets, Breed, Pets, TypeOfEquipment, Equipment, Users
from .forms import TypeOfPetsForm, BreedForm, PetsForm, TypeOfEquipmentForm, EquipmentForm, UsersForm


class TypeOfPetsListView(ListView):
    model = TypeOfPets


class TypeOfPetsCreateView(CreateView):
    model = TypeOfPets
    form_class = TypeOfPetsForm


class TypeOfPetsDetailView(DetailView):
    model = TypeOfPets


class TypeOfPetsUpdateView(UpdateView):
    model = TypeOfPets
    form_class = TypeOfPetsForm


class BreedListView(ListView):
    model = Breed


class BreedCreateView(CreateView):
    model = Breed
    form_class = BreedForm


class BreedDetailView(DetailView):
    model = Breed


class BreedUpdateView(UpdateView):
    model = Breed
    form_class = BreedForm


class PetsListView(ListView):
    model = Pets


class PetsCreateView(CreateView):
    model = Pets
    form_class = PetsForm


class PetsDetailView(DetailView):
    model = Pets


class PetsUpdateView(UpdateView):
    model = Pets
    form_class = PetsForm


class TypeOfEquipmentListView(ListView):
    model = TypeOfEquipment


class TypeOfEquipmentCreateView(CreateView):
    model = TypeOfEquipment
    form_class = TypeOfEquipmentForm


class TypeOfEquipmentDetailView(DetailView):
    model = TypeOfEquipment


class TypeOfEquipmentUpdateView(UpdateView):
    model = TypeOfEquipment
    form_class = TypeOfEquipmentForm


class EquipmentListView(ListView):
    model = Equipment


class EquipmentCreateView(CreateView):
    model = Equipment
    form_class = EquipmentForm


class EquipmentDetailView(DetailView):
    model = Equipment


class EquipmentUpdateView(UpdateView):
    model = Equipment
    form_class = EquipmentForm


class UsersListView(ListView):
    model = Users


class UsersCreateView(CreateView):
    model = Users
    form_class = UsersForm


class UsersDetailView(DetailView):
    model = Users


class UsersUpdateView(UpdateView):
    model = Users
    form_class = UsersForm

