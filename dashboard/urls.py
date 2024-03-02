from django.urls import path
from .views import *


urlpatterns = [
    path('create-employee/', CreateEmployee.as_view()),
    path('update-employee/<int:pk>/', UpdateEmployee.as_view()),
    path('delete-employee/<int:pk>/', DeleteEmployee.as_view()),

    path('create-adress/', CreateAdress.as_view()),
    path('update-adress/<int:pk>/', UpdateAdress.as_view()),
    path('delete-adress/<int:pk>/', DeleteAdress.as_view()),

    path('create-cashflow/', CreateCashflow.as_view()),
    path('update-cashflow/<int:pk>/', UpdateCashflow.as_view()),
    path('delete-cashflow/<int:pk>/', DeleteCashflow.as_view()),

    path('create-room/', CreateRoom.as_view()),
    path('update-room/<int:pk>/', UpdateRoom.as_view()),
    path('delete-room/<int:pk>/', DeleteRoom.as_view()),

    path('create-patient/', CreatePatient.as_view()),
    path('update-patient/<int:pk>/', UpdatePatient.as_view()),
    path('delete-patient/<int:pk>/', DeletePatient.as_view()),

    path('create-department/', CreateDepartment.as_view()),
    path('update-department/<int:pk>/', UpdateDepartment.as_view()),
    path('delete-department/<int:pk>/', DeleteDepartment.as_view()),

    path('create-operation/', CreateOperation.as_view()),
    path('update-operation/<int:pk>/', UpdateOperation.as_view()),
    path('delete-operation/<int:pk>/', DeleteOperation.as_view()),

    path('create-equipment/', CreateEquipment.as_view()),
    path('update-equipment/<int:pk>/', UpdateEquipment.as_view()),
    path('delete-equipment/<int:pk>/', DeleteEquipment.as_view()),

    path('create-cassa/', CreateCassa.as_view()),
    path('update-cassa/<int:pk>/', UpdateCassa.as_view()),
    path('delete-cassa/<int:pk>/', DeleteCassa.as_view()),

    path('create-testimonial_patent/', CreateTestimonial_patient.as_view()),
    path('update-testimonial_patent/<int:pk>/', UpdateTestimonial_patient.as_view()),
    path('delete-testimonial_patent/<int:pk>/', DeleteTestimonial_patient.as_view())
]
