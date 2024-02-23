from django.urls import path
from .views import Get_Cassa, Get_Attendance, Get_Patient, Get_Address, Get_Employee, Get_Cashflow,Get_Operation, Get_Testimonal_patient,Get_Department,Get_Room
from .views import *

urlpatterns = [
    path('get_employee/', Get_Employee.as_view()),
    path('get_address/', Get_Address.as_view()),
    path('get_room/', Get_Room.as_view()),
    path('get_cash_flow/', Get_Cashflow.as_view()),
    path('get_patent/', Get_Patient.as_view()),
    path('get_testimonal_patient/', Get_Testimonal_patient.as_view()),
    path('get_operation/', Get_Operation.as_view()),
    path('get_deparment/', Get_Department.as_view()),
    path('get_cassa/', Get_Cassa.as_view()),
]