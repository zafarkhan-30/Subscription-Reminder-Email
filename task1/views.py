from .models import User
from rest_framework import viewsets
from .serializers import subserialzier
import datetime
from .utils import util

# Create your views here.
class SubscriptionView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    for i in queryset:
        end_date = i.end_date
        email = i.email
        final = end_date - datetime.date.today()
        if (final.days == 7):
            data = {
                'subject':'Subscription Reminder' , 
                'body' : f'Your subscrption End date is {end_date}\n please renew your Plan' , 
                'to_email': email
                }
            util.send_email(data)
    serializer_class = [subserialzier]

    
