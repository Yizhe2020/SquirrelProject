from django.db import models
from django.utils.translation import gettext as _

class Data(models.Model):
    Latitude = models.FloatField(
        help_text = _('X Latitude'),
    )

    Longitude = models.FloatField(
        help_text = _('Y longitude'),
    )

    Unique_Squirrel_ID = models.CharField(
        max_length = 40,
        help_text = _('Unique Squirrel ID'),
        primary_key = True,
    )

    PM = 'PM'
    AM = 'AM'
    SHIFT_CHOICES = [
        (PM, _('PM')),
        (AM, _('AM')),
    ]

    Shift = models.CharField(
        max_length = 2,
        choices = SHIFT_CHOICES,
        help_text = _('Shift choice'),
    )

    Date = models.DateField(
        help_text=_('Date of record'),
    )
    
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = [
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
    ]

    Age = models.CharField(
        max_length = 10,
        choices = AGE_CHOICES,
        help_text=_('Age of Squirrel'),
        blank = True,
        null = True,
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    COLOR_CHOICES = [
        (BLACK, _('Black')),
        (CINNAMON, _('Cinnamon')),
        (BLACK, _('Black')),
    ]

    Primary_Fur_Color = models.CharField(
        max_length = 10,
        choices = COLOR_CHOICES,
        help_text=_('Color of Squirrel'),
        blank = True,
        null = True,
    )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION_CHOICES = [
        (GROUND_PLANE, _('Ground Plane')),
        (ABOVE_GROUND, _('Above Ground')),
    ]

    Location = models.CharField(
        max_length = 20,
        choices = LOCATION_CHOICES,
        blank = True,
        null = True,
    )

    Specific_Location = models.TextField(
        blank = True,
    )

    Running = models.BooleanField(
        help_text = _('whether the squirrel is running or not'),
    )

    Chasing = models.BooleanField(
        help_text = _('whether the squirrel is chasing or not'),
    )

    Climbing = models.BooleanField(
        help_text = _('whether the squirrel is climbing or not'),
    )

    Eating = models.BooleanField(
        help_text = _('whether the squirrel is eating or not'),
    )

    Foraging = models.BooleanField(
        help_text = _('whether the squirrel is foraging or not'),
    )

    Other_Activity = models.TextField(
        blank = True,
    )
    
    Kuks = models.BooleanField(
        help_text = _('whether the squirrel has kuks or not'),
    )

    Quaas = models.BooleanField(
        help_text = _('whether the squirrel has quaas or not'),
    )

    Moans = models.BooleanField(
        help_text = _('whether the squirrel has moans or not'),
    )

    Tail_Flags = models.BooleanField(
        help_text = _('whether the squirrel has tail falgs or not'),
    )

    Tail_Twitches = models.BooleanField(
        help_text = _('whether the squirrel has tail twitches or not'),
    )

    Approaches = models.BooleanField(
        help_text = _('whether the squirrel has approaches or not'),
    )

    Indifferent = models.BooleanField(
        help_text = _('whether the squirrel is indifferent or not'),
    )

    Runs_From = models.BooleanField(
        help_text = _('whether the squirrel runs from or not'),
    )    

    def __str__(self):
        return self.Unique_Squirrel_ID

#Create your models here.
