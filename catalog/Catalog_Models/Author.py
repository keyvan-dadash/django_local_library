from django.db import models
from django.urls import reverse
class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField('Died', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return "%s, %s" % (self.last_name,self.first_name)

    def natural_key(self):
        return (self.last_name+", "+self.first_name)
