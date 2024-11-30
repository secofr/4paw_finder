from django import forms
from .models import TypeOfPets, Breed, Pets, TypeOfEquipment, Equipment, Users


class TypeOfPetsForm(forms.ModelForm):
    class Meta:
        model = TypeOfPets
        fields = ['name']


class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ['name']


class PetsForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields = ['name', 'description', 'photo', 'breed', 'type_pets']


class TypeOfEquipmentForm(forms.ModelForm):
    class Meta:
        model = TypeOfEquipment
        fields = ['name']


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'type_equipment', 'user', 'pet']


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'consent_personal_date', 'consent_to_send_SMS', 'consent_to_send_whatsapp', 'consent_to_telegram', 'phone_main', 'phone_addict', 'whatsapp', 'telegram']


