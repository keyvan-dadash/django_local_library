from django.db import models

class Genre(models.Model):

    #Genre have manytomany relation to book class

    name = models.CharField(max_length=200, help_text="Enter book Genre (like Science etc..)")

    def __str__(self):
        return self.name
