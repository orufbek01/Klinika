from django.urls import path
from .views import *

urlpatterns = [
    ('get_employee/', Get_Employee.as_view()),
    ('get_address/', Get_Address.as_view()),

]