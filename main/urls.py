from django.urls import path
from .views import *

urlpatterns = [
    ('get_employee/', Get_Employee.as_view()),
    ('get_address/', Get_Address.as_view()),
    ('get_room/', Get_Room.as_view()),
    ('get_cash_flow/', Get_Cashflow.as_view()),
    ('get_patent/', Get_Patient.as_view()),
    ('get_testimonal_patient/', Get_Testimonal_patient.as_view()),
    ('get_operation/', Get_Operation.as_view()),
    ('get_deparment/', Get_Department.as_view()),
    ('get_cassa/', Get_Cassa.as_view()),
]