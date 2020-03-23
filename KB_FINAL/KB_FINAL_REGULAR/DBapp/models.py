from django.db import models

# Create your models here.
class Main(models.Model):
    username = models.CharField(max_length=264, unique=True)
    hash = models.CharField(max_length=264, unique=False)
    email = models.CharField(max_length=264, unique=False)
    hs = models.CharField(max_length=264, unique=False)
    sts = models.CharField(max_length=264, unique=False)

    def __str__(self):
        return "{} {} {} {} {}".format(self.username, self.hash, self.email, self.hs, self.sts)

class Friends(models.Model):
    username = models.CharField(max_length=264, unique=True)
    name = models.CharField(max_length=264, unique=False)

    def __str__(self):
        return "{} {}".format(self.username, self.name)


class Icons(models.Model):
    username = models.CharField(max_length=264, unique=True)
    icon = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return "{} {}".format(self.username, self.icon)




class Details(models.Model):
    location = models.CharField(max_length=264, unique=True)
    prices = models.CharField(max_length=264, unique=False)
    houseprice = models.CharField(max_length=264, unique=False)
    hotelprice = models.CharField(max_length=264, unique=False)

    def __str__(self):
        return "{} {} {} {}".format(self.location, self.prices, self.houseprice, self.hotelprice)
