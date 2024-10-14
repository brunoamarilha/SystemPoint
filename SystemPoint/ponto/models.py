from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if self.pk is None: 
            self.password = make_password(self.password)
        super(MeuUsuario, self).save(*args, **kwargs)

class Point(models.Model):
    point_id = models.CharField(max_length=10, primary_key=True)
    hr_join = models.TimeField()
    hr_exit = models.TimeField()
    desc = models.CharField(max_length=2000)


class Register(models.Model):
    register_id = models.CharField(max_length=10, primary_key=True)
    point = models.ForeignKey(Point, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)