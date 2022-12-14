from django.db import models
from django.conf import settings


class CategoryForTruck(models.Model):
    cars = models.CharField(max_length=50)
    isactive = models.BooleanField()

    def __str__(self) -> str:
        return self.cars


class WeightCargo(models.Model):
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class LengthCargo(models.Model):
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class TypeCargo(models.Model):
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class ModeCargo(models.Model):
    title = models.CharField(max_length = 50)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class Truck(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField(max_length=50)
    category = models.ForeignKey(CategoryForTruck, on_delete=models.CASCADE, null=True, blank=True)
    car_weight = models.FloatField(default=0)
    car_length = models.FloatField(default=0)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/truckimages', null=True)
    created_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-title"]

    def __str__(self):
        return self.title


class Truck_Images(models.Model):
    title = models.ForeignKey(Truck, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/truckimages', null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Image of {self.about.id}'




## Автопарк

 
class Order(models.Model):
    # users = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    car = models.ForeignKey(Truck, on_delete=models.CASCADE)
    title = models.CharField(max_length=65)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    from_here = models.CharField(max_length=50)
    to_here = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    weight_cargo = models.ForeignKey(WeightCargo, on_delete=models.CASCADE)
    length_cargo = models.ForeignKey(LengthCargo, on_delete = models.CASCADE)
    type_cargo = models.ForeignKey(TypeCargo, on_delete=models.CASCADE)
    mode_cargo = models.ForeignKey(ModeCargo, on_delete=models.CASCADE)


    class Meta:
        ordering = ["-title"]

    def __str__(self) -> str:
        return self.title


class Order_Images(models.Model):
    about = models.ForeignKey(Truck, on_delete=models.CASCADE, null=True, related_name="orderimages")
    image = models.ImageField(upload_to='images/orderimages', null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Image of {self.about.id}'


## Блог


class Category_Blog(models.Model):
    title = models.CharField(max_length=75)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class Blog(models.Model):
    category = models.ForeignKey(Category_Blog, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-title"]

    def __str__(self) -> str:
        return self.title


class Blog_Images(models.Model):
    about = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name="blogimages")
    image = models.ImageField(upload_to='images/blogimages', null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Image of {self.about.id}'


## Главная_2


class About_Company(models.Model):
    title = models.CharField(max_length=65)
    description = models.TextField(max_length=50)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-title"]

    def __str__(self):
        return self.title


class About_Company_Images(models.Model):
    about = models.ForeignKey(About_Company, on_delete=models.CASCADE, null=True, related_name="aboutimages")
    image = models.ImageField(upload_to='images/aboutimages', null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Image of {self.about.id}'


## Контакты


CONTACT_STATUS = (
    (0, "NEW"),
    (1, "PROCEED"),
    (2, "DISMISS"),
    (3, "COMPLETED")
)

class Contact(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    from_somewhere = models.CharField(max_length=100)
    to_somewhere = models.CharField(max_length=100)
    phone_number = models.IntegerField(default=True)
    status = models.IntegerField(choices=CONTACT_STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True, blank = True)


    class Meta:
        ordering = ["-title"]

    def __str__(self) -> str:
        return self.title


## Поп-ап


class Calculate_The_Cost():
    full_name = models.CharField(max_length = 250)
    from_somewhere = models.CharField(max_length = 70)
    to_somewhere = models.CharField(max_length = 100)
    email = models.EmailField()
    comments = models.CharField(max_length=50)
    phone_number = models.IntegerField(default=0)

    
    class Meta:
        ordering = ["-full_name"]

    def __str__(self):
        return self.full_name


## Frame 26


class Unloading_And_Loading():
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)

    class Meta:
        ordering = ['-title']

    def __str__(self) -> str:
        return self.title


## Внутренняя


class Work_Principles():
    title = models.CharField(max_length=65)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-title"]

    def __str__(self):
        return self.title


class Work_Principles_Images(models.Model):
    about = models.ForeignKey(About_Company, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='image/principlesimages', null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Image of {self.about.id}'



## Submit_The_Application

class Submit_Your_Application():
    stuff = models.CharField(max_length=150)
    from_to = models.CharField(max_length=75)
    phone_number = models.IntegerField(default=0)

    
    class Meta:
        ordering = ["-stuff"]

    def __str__(self):
        return self.stuff


class User():
    email = models.EmailField()
    password = models.CharField(max_length = 100)


    class Meta:
        ordering = ['-email']

    def __str__(self) -> str:
        return self.email


# Не сборные грузы


class Our_Services():
    title = models.CharField(max_length=65)
    price = models.CharField(max_length=75)

    class Meta:
        ordering = ["-title"]

    def __str__(self):
        return self.title


class Our_Services_Images(models.Model):
    image = models.ImageField(upload_to='images/serviceimages', null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'Image of {self.title.id}'


# Frame 25


class Cost_Of_Delivery(models.Model):
    country = models.CharField(max_length=100)
    shipping_cost = models.CharField(max_length=75)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-country']

    def __str__(self) -> str:
        return self.country


## Delivery Method


class Delivery_Method(models.Model):
    title = models.CharField(max_length=100)
    shipping_cost = models.CharField(max_length=75)

    class Meta:
        ordering = ['-title']

    def __str__(self) -> str:
        return self.title


class Delivery_Method_Images(models.Model):
    title = models.CharField(max_length=100)
    shipping_cost = models.CharField(max_length=75)

    class Meta:
        ordering = ['-title']

    def __str__(self) -> str:
        return self.title

