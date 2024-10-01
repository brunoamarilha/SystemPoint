from django.db import models

# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        # Hash da senha antes de salvar no banco de dados
        if self.pk is None:  # Verifica se é uma nova instância
            self.password = make_password(self.password)
        super(MeuUsuario, self).save(*args, **kwargs)

class Point(models.Model):
    hr_join = models.TimeField()
    hr_exit = models.TimeField()
    desc = models.CharField(max_length=2000)


class Register(models.Model):
    point = models.ForeignKey(Point, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)