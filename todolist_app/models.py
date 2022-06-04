from django.db import models

# Create your models here.


class TaskList(models.Model):
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)

    def __str__(self):
        # For not storing into the Objects
        return self.task + " - " + str(self.done)
