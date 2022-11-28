from django.db import models


class Category(models.Model):
    cars = models.CharField(max_length=50)
    isactive = models.BooleanField()


class Truck(models.Model):
    title = models.CharField()
    image = models.ImageField(upload_to = 'image/truck_images', null = True)
    description = models.TextField()


    class Meta:
        ordering = ["-title"]

    def __str__(self):
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
