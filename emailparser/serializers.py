from rest_framework import serializers

from emailparser.models import Emails


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emails
        fields = ('id', 'email_content', 'pdf_content' , 'subject' , 'email_from' , 'has_pdf')