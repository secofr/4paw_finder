import unittest
from django.urls import reverse
from django.test import Client
from .models import TypeOfPets, Breed, Pets, TypeOfEquipment, Equipment, Users
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_typeofpets(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return TypeOfPets.objects.create(**defaults)


def create_breed(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Breed.objects.create(**defaults)


def create_pets(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["description"] = "description"
    defaults["photo"] = "photo"
    defaults.update(**kwargs)
    if "breed" not in defaults:
        defaults["breed"] = create_breed()
    if "type_pets" not in defaults:
        defaults["type_pets"] = create_typeofpets()
    return Pets.objects.create(**defaults)


def create_typeofequipment(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return TypeOfEquipment.objects.create(**defaults)


def create_equipment(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "type_equipment" not in defaults:
        defaults["type_equipment"] = create_typeofequipment()
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    if "pet" not in defaults:
        defaults["pet"] = create_pets()
    return Equipment.objects.create(**defaults)


def create_users(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["consent_personal_date"] = "consent_personal_date"
    defaults["consent_to_send_SMS"] = "consent_to_send_SMS"
    defaults["consent_to_send_whatsapp"] = "consent_to_send_whatsapp"
    defaults["consent_to_telegram"] = "consent_to_telegram"
    defaults["phone_main"] = "phone_main"
    defaults["phone_addict"] = "phone_addict"
    defaults["whatsapp"] = "whatsapp"
    defaults["telegram"] = "telegram"
    defaults.update(**kwargs)
    return Users.objects.create(**defaults)


class TypeOfPetsViewTest(unittest.TestCase):
    '''
    Tests for TypeOfPets
    '''
    def setUp(self):
        self.client = Client()

    def test_list_typeofpets(self):
        url = reverse('equipment_typeofpets_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_typeofpets(self):
        url = reverse('equipment_typeofpets_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_typeofpets(self):
        typeofpets = create_typeofpets()
        url = reverse('equipment_typeofpets_detail', args=[typeofpets.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_typeofpets(self):
        typeofpets = create_typeofpets()
        data = {
            "name": "name",
        }
        url = reverse('equipment_typeofpets_update', args=[typeofpets.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class BreedViewTest(unittest.TestCase):
    '''
    Tests for Breed
    '''
    def setUp(self):
        self.client = Client()

    def test_list_breed(self):
        url = reverse('equipment_breed_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_breed(self):
        url = reverse('equipment_breed_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_breed(self):
        breed = create_breed()
        url = reverse('equipment_breed_detail', args=[breed.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_breed(self):
        breed = create_breed()
        data = {
            "name": "name",
        }
        url = reverse('equipment_breed_update', args=[breed.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PetsViewTest(unittest.TestCase):
    '''
    Tests for Pets
    '''
    def setUp(self):
        self.client = Client()

    def test_list_pets(self):
        url = reverse('equipment_pets_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pets(self):
        url = reverse('equipment_pets_create')
        data = {
            "name": "name",
            "description": "description",
            "photo": "photo",
            "breed": create_breed().pk,
            "type_pets": create_typeofpets().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pets(self):
        pets = create_pets()
        url = reverse('equipment_pets_detail', args=[pets.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pets(self):
        pets = create_pets()
        data = {
            "name": "name",
            "description": "description",
            "photo": "photo",
            "breed": create_breed().pk,
            "type_pets": create_typeofpets().pk,
        }
        url = reverse('equipment_pets_update', args=[pets.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TypeOfEquipmentViewTest(unittest.TestCase):
    '''
    Tests for TypeOfEquipment
    '''
    def setUp(self):
        self.client = Client()

    def test_list_typeofequipment(self):
        url = reverse('equipment_typeofequipment_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_typeofequipment(self):
        url = reverse('equipment_typeofequipment_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_typeofequipment(self):
        typeofequipment = create_typeofequipment()
        url = reverse('equipment_typeofequipment_detail', args=[typeofequipment.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_typeofequipment(self):
        typeofequipment = create_typeofequipment()
        data = {
            "name": "name",
        }
        url = reverse('equipment_typeofequipment_update', args=[typeofequipment.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class EquipmentViewTest(unittest.TestCase):
    '''
    Tests for Equipment
    '''
    def setUp(self):
        self.client = Client()

    def test_list_equipment(self):
        url = reverse('equipment_equipment_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_equipment(self):
        url = reverse('equipment_equipment_create')
        data = {
            "name": "name",
            "type_equipment": create_typeofequipment().pk,
            "user": create_django_contrib_auth_models_user().pk,
            "pet": create_pets().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_equipment(self):
        equipment = create_equipment()
        url = reverse('equipment_equipment_detail', args=[equipment.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_equipment(self):
        equipment = create_equipment()
        data = {
            "name": "name",
            "type_equipment": create_typeofequipment().pk,
            "user": create_django_contrib_auth_models_user().pk,
            "pet": create_pets().pk,
        }
        url = reverse('equipment_equipment_update', args=[equipment.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class UsersViewTest(unittest.TestCase):
    '''
    Tests for Users
    '''
    def setUp(self):
        self.client = Client()

    def test_list_users(self):
        url = reverse('equipment_users_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_users(self):
        url = reverse('equipment_users_create')
        data = {
            "name": "name",
            "consent_personal_date": "consent_personal_date",
            "consent_to_send_SMS": "consent_to_send_SMS",
            "consent_to_send_whatsapp": "consent_to_send_whatsapp",
            "consent_to_telegram": "consent_to_telegram",
            "phone_main": "phone_main",
            "phone_addict": "phone_addict",
            "whatsapp": "whatsapp",
            "telegram": "telegram",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_users(self):
        users = create_users()
        url = reverse('equipment_users_detail', args=[users.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_users(self):
        users = create_users()
        data = {
            "name": "name",
            "consent_personal_date": "consent_personal_date",
            "consent_to_send_SMS": "consent_to_send_SMS",
            "consent_to_send_whatsapp": "consent_to_send_whatsapp",
            "consent_to_telegram": "consent_to_telegram",
            "phone_main": "phone_main",
            "phone_addict": "phone_addict",
            "whatsapp": "whatsapp",
            "telegram": "telegram",
        }
        url = reverse('equipment_users_update', args=[users.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


