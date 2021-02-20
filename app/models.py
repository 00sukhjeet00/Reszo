from django.db import models


class Blog(models.Model):
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='static/img')
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Menu(models.Model):
    choice = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    ]
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='static/img')
    category = models.CharField(max_length=10, choices=choice)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    day = models.CharField(max_length=20)
    hour = models.CharField(max_length=20)
    person = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Subcribe(models.Model):
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.IntegerField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name
