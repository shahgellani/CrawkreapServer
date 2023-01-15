from django.db import models


# Create your models here.


class Emails(models.Model):
    email_from = models.CharField(max_length=50)
    email_content = models.TextField(blank=True)
    subject = models.TextField(blank=True)
    pdf_content = models.TextField(blank=True)
    has_pdf = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.email_from)
