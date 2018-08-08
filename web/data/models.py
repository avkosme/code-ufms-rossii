from django.db import models


# Create your models here.


class d4826085213(models.Model):
    guid = models.CharField(max_length=500)
    fio = models.CharField(max_length=500)
    born_date = models.CharField(max_length=500)
    born_place = models.CharField(max_length=500, default='', blank=True)
    pass_num = models.CharField(max_length=500)
    pass_date = models.CharField(max_length=500)
    pass_issued = models.CharField(max_length=500)
    code = models.CharField(max_length=500)
    inn = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    number = models.CharField(max_length=500)

    def __str__(self):
        return ' '.join(
            (self.guid, self.fio, self.born_date, self.born_place, self.pass_num, self.pass_date, self.pass_issued,
             self.code, self.inn, self.name, self.number))


class d6162070130(models.Model):
    guid = models.CharField(max_length=500)
    fio = models.CharField(max_length=500)
    born_date = models.CharField(max_length=500)
    born_place = models.CharField(max_length=500, default='', blank=True)
    pass_num = models.CharField(max_length=500)
    pass_date = models.CharField(max_length=500)
    pass_issued = models.CharField(max_length=500)
    code = models.CharField(max_length=500)
    inn = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    number = models.CharField(max_length=500)

    def __str__(self):
        return ' '.join(
            (self.guid, self.fio, self.born_date, self.born_place, self.pass_num, self.pass_date, self.pass_issued,
             self.code, self.inn, self.name, self.number))


class d6168077734(models.Model):
    guid = models.CharField(max_length=500)
    fio = models.CharField(max_length=500)
    born_date = models.CharField(max_length=500)
    born_place = models.CharField(max_length=500, default='', blank=True)
    pass_num = models.CharField(max_length=500)
    pass_date = models.CharField(max_length=500)
    pass_issued = models.CharField(max_length=500)
    code = models.CharField(max_length=500)
    inn = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    number = models.CharField(max_length=500)

    def __str__(self):
        return ' '.join(
            (self.guid, self.fio, self.born_date, self.born_place, self.pass_num, self.pass_date, self.pass_issued,
             self.code, self.inn, self.name, self.number))
