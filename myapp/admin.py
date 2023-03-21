from django.contrib import admin

# Register your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.text()
    date = models.DateField()

    def__str__(self):
        return self.name
        