from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import ImageField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class TypeOfPets(models.Model):

    # Fields
    name = models.CharField(max_length=255, unique=True,)
    slug = extension_fields.AutoSlugField(
        populate_from='name',
        #  blank=True,
        unique=True,
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('equipment_typeofpets_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('equipment_typeofpets_update', args=(self.slug,))


class Breed(models.Model):

    # Fields
    name = models.CharField(max_length=255, unique=True,)
    slug = extension_fields.AutoSlugField(
        populate_from='name',
        # blank=True,
        unique=True,
        )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    type_pets = models.ForeignKey(
        TypeOfPets,
        on_delete=models.CASCADE, related_name="breeds"
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('equipment_breed_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('equipment_breed_update', args=(self.slug,))


class Pets(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=250)
    photo = models.ImageField(upload_to="upload/images/")

    # Relationship Fields
    breed = models.ForeignKey(
        Breed,
        related_name="petss",
        on_delete=models.CASCADE
    )
    type_pets = models.ForeignKey(
        TypeOfPets,
        on_delete=models.CASCADE, related_name="petss"
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('equipment_pets_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('equipment_pets_update', args=(self.slug,))


class TypeOfEquipment(models.Model):

    # Fields
    name = models.CharField(max_length=255, unique=True,)
    slug = extension_fields.AutoSlugField(
        populate_from='name',
        # blank=True,
        unique=True,
        )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('equipment_typeofequipment_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('equipment_typeofequipment_update', args=(self.slug,))


class Equipment(models.Model):

    # Fields
    name = models.CharField(max_length=255, unique=True)
    slug = extension_fields.AutoSlugField(
        populate_from='name',
        # blank=True,
        unique=True
        )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    type_equipment = models.ForeignKey(
        TypeOfEquipment,
        on_delete=models.CASCADE, related_name="equipments"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="equipments"
    )
    pet = models.ForeignKey(
        Pets,
        on_delete=models.CASCADE, related_name="equipments"
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('equipment_equipment_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('equipment_equipment_update', args=(self.slug,))


class Users(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    consent_personal_date = models.BooleanField()
    consent_to_send_SMS = models.BooleanField()
    consent_to_send_whatsapp = models.BooleanField()
    consent_to_telegram = models.BooleanField()
    phone_main = models.CharField(max_length=12)
    phone_addict = models.CharField(max_length=12)
    whatsapp = models.CharField(max_length=30)
    telegram = models.CharField(max_length=30)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('equipment_users_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('equipment_users_update', args=(self.slug,))
