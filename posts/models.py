from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
def upload_location(instance , filename):
    return "%s/%s" %(instance.id, filename)

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=10000)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __unicode__(self):
         return self.title
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={'id':self.id})
    
    class Meta:
        ordering = ["-timestamp", "-update"]