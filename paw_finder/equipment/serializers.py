from . import models

from rest_framework import serializers


class TypeOfPetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TypeOfPets
        fields = (
            'slug',
            'name',
            'created',
            'last_updated',
        )


class BreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Breed
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class PetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pets
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'description', 
            'photo', 
        )


class TypeOfEquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TypeOfEquipment
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Equipment
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Users
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'consent_personal_date', 
            'consent_to_send_SMS', 
            'consent_to_send_whatsapp', 
            'consent_to_telegram', 
            'phone_main', 
            'phone_addict', 
            'whatsapp', 
            'telegram', 
        )


