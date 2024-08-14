from django.db import models


class DailyMenu(models.Model):
    Date = models.DateField(unique=True)
    soup = models.CharField(max_length=1000)
    main_course1_opt1 = models.CharField(max_length=1000)
    main_course1_opt2 = models.CharField(max_length=1000)
    main_course2 = models.CharField(max_length=1000)
    sides = models.CharField(max_length=1000)



