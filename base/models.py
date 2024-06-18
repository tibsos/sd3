from django.db import models as m

from uuid import uuid4

class Customer(m.Model):

    uid = m.UUIDField(default = uuid4)

    name = m.TextField()
    phone = m.TextField()

    sent_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        return self.name

class Visit(m.Model):

    uid = m.UUIDField(default = uuid4)

    url = m.URLField(null = True)
    
    # user info

    ip = m.TextField(blank = True, null = True)
    country = m.TextField(blank = True, null = True)
    city = m.TextField(blank = True, null = True)

    mobile = m.BooleanField()

    # request time

    entered_at = m.DateTimeField()

    def __str__(self):

        return str(self.entered_at)
    

class ButtonClick(m.Model):
    
    uid = m.UUIDField(default = uuid4)

    clicked_at = m.DateTimeField(auto_now_add = True)

    def __str__(self):

        return self.clicked_at