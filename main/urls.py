from django.urls import path
from .views import Get_Cassa, Get_Attendance, Get_Patient, Get_Address, Get_Employee, Get_Cashflow,Get_Operation, Get_Testimonal_patient,Get_Department,Get_Room
from .views import *

urlpatterns = [
    path('get_employee/<slug:slug>/', Get_Employee.as_view()),
    path('get_address/<slug:slug>/', Get_Address.as_view()),
    path('get_room/<slug:slug>/', Get_Room.as_view()),
    path('get_cash_flow/<slug:slug>/', Get_Cashflow.as_view()),
    path('get_patent/<slug:slug>/', Get_Patient.as_view()),
    path('get_testimonal_patient/<slug:slug>/', Get_Testimonal_patient.as_view()),
    path('get_operation/<slug:slug>/', Get_Operation.as_view()),
    path('get_deparment/<slug:slug>/', Get_Department.as_view()),
    path('get_cassa/<slug:slug>/', Get_Cassa.as_view()),
]