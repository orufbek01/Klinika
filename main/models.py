from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
import re
import qrcode
from io import BytesIO
from django.core.files import File


class User(AbstractUser):
    avatar = models.ImageField(upload_to='foto/', verbose_name='Rasm')
    passport_seria = models.CharField(max_length=55, verbose_name='Passport seriasi')
    age = models.IntegerField(verbose_name='Yosh')
    address = models.ForeignKey(to='Address', on_delete=models.CASCADE, verbose_name='Yashash joyi')
    phone_number = models.CharField(max_length=13,null=True,blank=True, verbose_name='Telefon raqam' ,validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message = 'Invalide phone number',
            code = 'Invalid number'
        )
    ])
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Famale', 'Famale')
    )
    gender = models.CharField(max_length=55,verbose_name='Jins', choices=GENDER_CHOICES)
    slugify = models.SlugField()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.passport_seria, self.phone_number)
        super().save(*args, **kwargs)


class Employee(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    age = models.IntegerField(default=19)
    specialty = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=13, null=True, blank=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    address = models.ForeignKey(to='Address', on_delete=models.CASCADE)
    extra_phone_number = models.CharField(max_length=13, null=True, blank=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=15, decimal_places=2)
    start_work_time = models.TimeField()
    end_work_time = models.TimeField()
    started_work = models.DateField(auto_now=True)
    slugify = models.SlugField()
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=4,
    )
    # qr.add_data(f"Your data to encode in the QR code: {self.Employee.specialty}")
    # qr.make(fit=True)
    # img = qr.make_image(fill_color="black", back_color="white")
    # buffer = BytesIO()
    # img.save(buffer)
    # buffer.seek(0)
    # self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name, self.phone_number)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name


class Address(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Cashflow(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=255)
    PATMENT_TYPE = (
        ('Karta', 'Karta'),
        ('Naqd', 'Naqd'),
    )
    payment_type = models.CharField(max_length=55, choices=PATMENT_TYPE)
    timestamp = models.DateTimeField(auto_now=True)
    # qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    slugify = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name, self.phone_number)
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=4,
    )
    # qr.add_data(f"Your data to encode in the QR code: {self.Cashflow.user}")
    # qr.make(fit=True)
    # img = qr.make_image(fill_color="black", back_color="white")
    # buffer = BytesIO()
    # img.save(buffer)
    # buffer.seek(0)
    # self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

    def __str__(self):
        return self.user


class Room(models.Model):
    name = models.CharField(max_length=55)
    deparment = models.ForeignKey(to='Department', on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    place = models.IntegerField(default=0)
    busy_empty = models.FloatField()

    def __str__(self):
        return self.number


class Patient(models.Model):
    full_name = models.CharField(max_length=55)
    doctor = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE)
    suggestions = models.CharField(max_length=55)
    age = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=13, null=True, blank=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    email = models.EmailField()
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE)
    adress = models.ForeignKey(to=Address, on_delete=models.CASCADE)
    # qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    slugify = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name, self.phone_number)
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=4,
    )
    # qr.add_data(f"Your data to encode in the QR code: {self.Patient.room}")
    # qr.make(fit=True)
    # img = qr.make_image(fill_color="black", back_color="white")
    # buffer = BytesIO()
    # img.save(buffer)
    # buffer.seek(0)
    # self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

    def __str__(self):
        return self.name


class Department(models.Model):
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.number


class Operation(models.Model):
    name = models.CharField(max_length=55)
    doctor = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
    patient = models.ForeignKey(to='Patient', on_delete=models.CASCADE)
    equipment = models.ForeignKey(to='Equipment', on_delete=models.CASCADE)


class Equipment(models.Model):
    name = models.CharField(max_length=55)
    type = models.CharField(max_length=55)
    number = models.IntegerField(default=0)
    room = models.ManyToManyField(to='Room')

    def __str__(self):
        return self.name


class Cassa(models.Model):
    total_amout = models.DecimalField(max_digits=55, decimal_places=2)

    def __str__(self):
        return self.total_amout


class Testimonal_patient(models.Model):
    patient = models.ForeignKey(to='Patient', on_delete=models.CASCADE)
    comments = models.CharField(max_length=55)
    complaints = models.CharField(max_length=55)

    def __str__(self):
        return self.patient
