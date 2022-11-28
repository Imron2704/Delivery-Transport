from django.db import models


class Types_of_Freight(models.Model):
    forwarding = models.CharField(max_length=30)
    consolidated_refrigerated_cargo = models.CharField(max_length=50)
    transportation_of_medicines = models.CharField(max_length=60)
    transportation_of_food = models.CharField(max_length=30)
    transportation_of_building_materials = models.CharField(max_length=50)
    logistics_and_routing = models.CharField(max_length=100)


    class Meta:
        ordering = ["-forwarding"]

    def __str__(self):
        return self.forwarding


class Calculate_the_Cost():
    first_name = models.CharField(max_length = 250)
    from_somewhere = models.CharField(max_length = 70)
    to_somewhere = models.CharField(max_length = 100)
    email = models.EmailField()
    comments = models.CharField(max_length=50)
    phone_number = models.IntegerField(default=0)

    
    class Meta:
        ordering = ["-first_name"]

    def __str__(self):
        return self.first_name


class Submit_your_application():
    stuff = models.CharField(max_length=150)
    from_to = models.CharField(max_length=75)
    phone_number = models.IntegerField(default=0)

    def __str__(self):
        return self.stuff

    
    class Meta:
        ordering = ["-stuff"]

    def __str__(self):
        return self.stuff


class Services():
    pass


class Blog():
    pass


class For_business():
    pass


class Individuals():
    pass


class Contacts():
    pass


class About_Company():
    pass


class User():
    email = models.EmailField()
    password = models.CharField(max_length = 100)


    class Meta:
        ordering = ['-email']

    def __str__(self) -> str:
        return self.email