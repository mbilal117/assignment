from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Policy(models.Model):
    type = models.CharField(max_length=255)
    premium = models.IntegerField()
    cover = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return "({0}) {1}".format(self.type, self.customer.first_name)
