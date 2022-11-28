from django.db import models


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


class VolumeCargo(models.Model):
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

    
class Order(models.Model):
    # users = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    # car = models.ForeignKey(Truck, on_delete=models.CASCADE)
    title = models.CharField(max_length=65)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    from_here = models.CharField(max_length=50)
    to_here = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    weight_cargo = models.ForeignKey(WeightCargo, on_delete=models.CASCADE)
    volume_cargo = models.ForeignKey(VolumeCargo, on_delete = models.CASCADE)
    type_cargo = models.ForeignKey(TypeCargo, on_delete=models.CASCADE)
    mode_cargo = models.ForeignKey(ModeCargo, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='apps/order/', null=True)
    image2 = models.ImageField(upload_to='apps/order/', null=True, blank=True)
    image3 = models.ImageField(upload_to='apps/order/', null=True, blank=True)

    def __str__(self) -> str:
        return self.title, self.image


class Truck(models.Model):
    title = models.CharField()
    image = models.ImageField(upload_to = 'image/truck_images', null = True)
    description = models.TextField()
    category = models.ForeignKey(CategoryForTruck, on_delete=models.CASCADE, null=True, blank=True)
    car_weight = models.FloatField(default=0)
    car_length = models.FloatField(default=0)
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-title"]

    def __str__(self):
        return self.title


class BlogAboutTruck(models.Model):
    title = models.CharField(max_length=75)
    is_active = models.BooleanField()

    def __str__(self) -> str:
        return self.title


class Blog(models.Model):
    category = models.ForeignKey(BlogAboutTruck, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/blogimages', null=True)
    description = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class AboutCompany(models.Model):
    title = models.CharField(max_length=65)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AboutCompanyImages(models.Model):
    about = models.ForeignKey(AboutCompany, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='image/aboutimages', null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Image of {self.about.id}'

CONTACT_STATUS = (
    (0, "NEW"),
    (1, "PROCEED"),
    (2, "DISMISS"),
    (3, "COMPLETED")
)

class Contact(models.Model):
    title = models.CharField(max_length=75)
    date_created = models.DateTimeField(auto_now_add=True, blank = True)
    description = models.TextField()
    from_somewhere = models.CharField(max_length=100)
    to_somewhere = models.CharField(max_length=100)
    phone_number = models.IntegerField(default=True)
    status = models.IntegerField(choices=CONTACT_STATUS, default=0)

    def __str__(self) -> str:
        return self.title


class Calculate_the_Cost():
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


class User():
    email = models.EmailField()
    password = models.CharField(max_length = 100)


    class Meta:
        ordering = ['-email']

    def __str__(self) -> str:
        return self.email


# class Services():
#     pass




# class For_business():
#     pass


# class Individuals():
#     pass
