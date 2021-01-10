from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='images/')
    picture = models.ImageField(upload_to='images/')
    body = models.TextField()
    pub_date = models.DateTimeField()
    url = models.URLField()
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)


    def pub_date_pretty(self):
        return self.pub_date.strftime("%d-%m-%Y")

    def __str__(self):
        return self.title

    def summary(self):
        self.summary = self.body.split()
        self.summary = self.summary[:20]
        return " ".join(self.summary) + "..."


