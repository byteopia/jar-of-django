from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager
from django.db import transaction

User = settings.AUTH_USER_MODEL


# Create your models here.
class Plan(models.Model):
    stripe_id = models.CharField(max_length=40)
    display_name = models.CharField(max_length=24)
    price = models.FloatField()
    slug = models.CharField(max_length=24)


class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="profile")
    plan = models.ForeignKey(Plan, related_name="users")


class CompanyManager(BaseUserManager):

    def create_company(self, data_dict):
        p = Plan.objects.get(pk=int(data_dict['plan']))
        c = self.model(
            name=data_dict['company_name'],
            address_one=data_dict['address_one'],
            address_two=data_dict['address_two'],
            city=data_dict['city'],
            region=data_dict['region'],
            country=data_dict['country'],
            contact_phone_number=data_dict['contact_phone_number'],
            # org_id=data_dict['org_id'],
            # san=data_dict['san'],
            plan=p
        )
        c.save()
        return c

    @transaction.atomic
    def create_company_user(self, **kwargs):
        """ Creates and saves a User with the given username, email and password. """
        user = User.objects.create_user(name=kwargs['name'], email=kwargs['email'], password=kwargs['password'])
        user.save()
        company = self.create_company(kwargs)
        user_profile = UserProfile(user=user, company=company, is_company_admin=True)
        user_profile.save()
        return user


class Company(models.Model):
    name = models.CharField(max_length=128)
    address_one = models.CharField(max_length=256)
    address_two = models.CharField(max_length=256)
    city = models.CharField(max_length=64)
    region = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    contact_phone_number = models.CharField(max_length=15)
    san = models.CharField(max_length=20, null=True)
    stripe_key = models.CharField(verbose_name='stripe key', max_length=40, null=True)
    plan = models.ForeignKey(Plan, related_name="companies")

    objects = CompanyManager()

