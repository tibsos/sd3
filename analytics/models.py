from django.db import models as m

from uuid import uuid4 as u4

class Visit(m.Model):

    uid = m.UUIDField(default = u4)

    url = m.URLField(null = True)
    
    # user info

    ip = m.TextField(blank = True, null = True)
    country = m.TextField(blank = True, null = True)
    city = m.TextField(blank = True, null = True)

    mobile = m.BooleanField()

    # request time

    entered_at = m.DateTimeField()
    left_at = m.DateTimeField(null = True)

    def __str__(self):

        return str(self.entered_at)