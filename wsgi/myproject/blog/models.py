from django.db import models

# Create your models here.
class Blog(models.Model):
    blogtitle = models.CharField(max_length=300)
    blogdesc = models.TextField()
    doc = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.blogtitle
