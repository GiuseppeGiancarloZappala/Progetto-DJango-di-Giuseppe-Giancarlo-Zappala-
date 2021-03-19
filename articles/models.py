

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from config.utils import sendTransactions
import hashlib

class Article(models.Model):
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,
        on_delete=models.CASCADE,related_name='articles'
    )
    hash = models.CharField(max_length=66, default=None, null=True)
    txId = models.CharField(max_length=66, default=None, null=True)

    def writeOnChain(self):
        self.hash = hashlib.sha256(self.body.encode('utf-8')).hexdigest()
        self.txId = sendTransactions(self.hash)
        self.save()

        # def get_absolute_url(self):
        #     return reverse("article_detail", kwargs={"pk": self.pk})

    # def __str__(self):
    #     return self.hash

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
    class Meta:
        get_latest_by = "id"

class Ipp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address