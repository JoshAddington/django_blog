from django.db import models
from django.utils import timezone


# Model for keeping track of Projects
class Project(models.Model):
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=50)

        preview = models.CharField(max_length=250, blank=True)
        content = models.TextField()
        code = models.TextField(blank=True)
        js = models.TextField(blank=True)
        created_date = models.DateTimeField(default=timezone.now)
        published_date = models.DateTimeField(blank=True, null=True)

        def publish(self):
                self.published_date = timezone.now()
                self.save()

        def __str__(self):
                return self.title
