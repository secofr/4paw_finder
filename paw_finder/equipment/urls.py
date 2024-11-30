from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

app_name = 'equipment'

router = routers.DefaultRouter()
router.register(r'typeofpets', api.TypeOfPetsViewSet)
router.register(r'breed', api.BreedViewSet)
router.register(r'pets', api.PetsViewSet)
router.register(r'typeofequipment', api.TypeOfEquipmentViewSet)
router.register(r'equipment', api.EquipmentViewSet)
router.register(r'users', api.UsersViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for TypeOfPets
    path('', views.EquipmentCreateView.as_view(), name='index'),
    path('equipment/typeofpets/', views.TypeOfPetsListView.as_view(), name='equipment_typeofpets_list'),
    path('equipment/typeofpets/create/', views.TypeOfPetsCreateView.as_view(), name='equipment_typeofpets_create'),
    path('equipment/typeofpets/detail/<slug:slug>/', views.TypeOfPetsDetailView.as_view(), name='equipment_typeofpets_detail'),
    path('equipment/typeofpets/update/<slug:slug>/', views.TypeOfPetsUpdateView.as_view(), name='equipment_typeofpets_update'),
)

urlpatterns += (
    # urls for Breed
    path('equipment/breed/', views.BreedListView.as_view(), name='equipment_breed_list'),
    path('equipment/breed/create/', views.BreedCreateView.as_view(), name='equipment_breed_create'),
    path('equipment/breed/detail/<slug:slug>/', views.BreedDetailView.as_view(), name='equipment_breed_detail'),
    path('equipment/breed/update/<slug:slug>/', views.BreedUpdateView.as_view(), name='equipment_breed_update'),
)

urlpatterns += (
    # urls for Pets
    path('equipment/pets/', views.PetsListView.as_view(), name='equipment_pets_list'),
    path('equipment/pets/create/', views.PetsCreateView.as_view(), name='equipment_pets_create'),
    path('equipment/pets/detail/<slug:slug>/', views.PetsDetailView.as_view(), name='equipment_pets_detail'),
    path('equipment/pets/update/<slug:slug>/', views.PetsUpdateView.as_view(), name='equipment_pets_update'),
)

urlpatterns += (
    # urls for TypeOfEquipment
    path('equipment/typeofequipment/', views.TypeOfEquipmentListView.as_view(), name='equipment_typeofequipment_list'),
    path('equipment/typeofequipment/create/', views.TypeOfEquipmentCreateView.as_view(), name='equipment_typeofequipment_create'),
    path('equipment/typeofequipment/detail/<slug:slug>/', views.TypeOfEquipmentDetailView.as_view(), name='equipment_typeofequipment_detail'),
    path('equipment/typeofequipment/update/<slug:slug>/', views.TypeOfEquipmentUpdateView.as_view(), name='equipment_typeofequipment_update'),
)

urlpatterns += (
    # urls for Equipment
    path('equipment/equipment/', views.EquipmentListView.as_view(), name='equipment_equipment_list'),
    path('equipment/equipment/create/', views.EquipmentCreateView.as_view(), name='equipment_equipment_create'),
    path('equipment/equipment/detail/<slug:slug>/', views.EquipmentDetailView.as_view(), name='equipment_equipment_detail'),
    path('equipment/equipment/update/<slug:slug>/', views.EquipmentUpdateView.as_view(), name='equipment_equipment_update'),
)

urlpatterns += (
    # urls for Users
    path('equipment/users/', views.UsersListView.as_view(), name='equipment_users_list'),
    path('equipment/users/create/', views.UsersCreateView.as_view(), name='equipment_users_create'),
    path('equipment/users/detail/<slug:slug>/', views.UsersDetailView.as_view(), name='equipment_users_detail'),
    path('equipment/users/update/<slug:slug>/', views.UsersUpdateView.as_view(), name='equipment_users_update'),
)
