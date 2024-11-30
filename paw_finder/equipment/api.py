from . import models
from . import serializers
from rest_framework import viewsets, permissions


class TypeOfPetsViewSet(viewsets.ModelViewSet):
    """ViewSet for the TypeOfPets class"""

    queryset = models.TypeOfPets.objects.all()
    serializer_class = serializers.TypeOfPetsSerializer
    permission_classes = [permissions.IsAuthenticated]


class BreedViewSet(viewsets.ModelViewSet):
    """ViewSet for the Breed class"""

    queryset = models.Breed.objects.all()
    serializer_class = serializers.BreedSerializer
    permission_classes = [permissions.IsAuthenticated]


class PetsViewSet(viewsets.ModelViewSet):
    """ViewSet for the Pets class"""

    queryset = models.Pets.objects.all()
    serializer_class = serializers.PetsSerializer
    permission_classes = [permissions.IsAuthenticated]


class TypeOfEquipmentViewSet(viewsets.ModelViewSet):
    """ViewSet for the TypeOfEquipment class"""

    queryset = models.TypeOfEquipment.objects.all()
    serializer_class = serializers.TypeOfEquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class EquipmentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Equipment class"""

    queryset = models.Equipment.objects.all()
    serializer_class = serializers.EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class UsersViewSet(viewsets.ModelViewSet):
    """ViewSet for the Users class"""

    queryset = models.Users.objects.all()
    serializer_class = serializers.UsersSerializer
    permission_classes = [permissions.IsAuthenticated]


