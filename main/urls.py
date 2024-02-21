from django.urls import path
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