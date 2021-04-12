# Django Bot

A TWILIO SMS bot in Django with a SMS simulator.

1. `python3 -m pip install django`
1. `python3 manage.py migrate`
1. `python3 manage.py test`
1. `python3 manage.py runserver`
1. follow the link to the bot

*Note try the `inclass` branch for a more complete example

The code that you change is:

```
from django.db import models

# Create your models here.


class Order(models.Model):
    phone = models.CharField(max_length=255, default='')
    data = models.JSONField()

    def handleInput(self, sInput):
        # self.data["state"] starts out as WELCOMING
        aReturn = []
        return aReturn

    def isDone(self):
        if self.data["state"] == "DONE":
            return True
        else:
            return False

    class Meta:
        indexes = [models.Index(fields=['phone'])]
```