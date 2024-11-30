from django.contrib import admin
from django import forms
from .models import TypeOfPets, Breed, Pets, TypeOfEquipment, Equipment, Users


class TypeOfPetsAdminForm(forms.ModelForm):

    class Meta:
        model = TypeOfPets
        fields = '__all__'


class TypeOfPetsAdmin(admin.ModelAdmin):
    form = TypeOfPetsAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['slug', 'created', 'last_updated']


admin.site.register(TypeOfPets, TypeOfPetsAdmin)


class BreedAdminForm(forms.ModelForm):

    class Meta:
        model = Breed
        fields = '__all__'


class BreedAdmin(admin.ModelAdmin):
    form = BreedAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['slug', 'created', 'last_updated']

admin.site.register(Breed, BreedAdmin)


class PetsAdminForm(forms.ModelForm):

    class Meta:
        model = Pets
        fields = '__all__'


class PetsAdmin(admin.ModelAdmin):
    form = PetsAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'description', 'photo']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'description', 'photo']

admin.site.register(Pets, PetsAdmin)


class TypeOfEquipmentAdminForm(forms.ModelForm):

    class Meta:
        model = TypeOfEquipment
        fields = '__all__'


class TypeOfEquipmentAdmin(admin.ModelAdmin):
    form = TypeOfEquipmentAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['slug', 'created', 'last_updated']


admin.site.register(TypeOfEquipment, TypeOfEquipmentAdmin)


class EquipmentAdminForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = '__all__'


class EquipmentAdmin(admin.ModelAdmin):
    form = EquipmentAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(Equipment, EquipmentAdmin)


class UsersAdminForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = '__all__'


class UsersAdmin(admin.ModelAdmin):
    form = UsersAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'consent_personal_date', 'consent_to_send_SMS', 'consent_to_send_whatsapp', 'consent_to_telegram', 'phone_main', 'phone_addict', 'whatsapp', 'telegram']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'consent_personal_date', 'consent_to_send_SMS', 'consent_to_send_whatsapp', 'consent_to_telegram', 'phone_main', 'phone_addict', 'whatsapp', 'telegram']

admin.site.register(Users, UsersAdmin)


