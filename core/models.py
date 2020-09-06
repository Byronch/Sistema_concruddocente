from django.db import models


# Create your models here.

# Create your models here.
class Docente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    email = models.EmailField()
    estado = models.IntegerField(default=1)
    sexo = models.CharField(max_length=1, default=1)
    user = models.CharField(max_length=15)
    usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.CharField(max_length=50)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']


class ReporterArticle(models.Model):
    Reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
