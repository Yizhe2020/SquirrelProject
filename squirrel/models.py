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
        max_length = 14,
        primary_key = True,
        help_text = _('Unique Squirrel ID'),
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
        default = PM,
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
    )

    Specific_Location = models.TextField(
        blank = True,
    )

    Running = models.BooleanField(
        help_text = _('whether the squirrel is running or not'),
        default = False,
    )

    Chasing = models.BooleanField(
        help_text = _('whether the squirrel is chasing or not'),
        default = False,
    )

    Climbing = models.BooleanField(
        help_text = _('whether the squirrel is climbing or not'),
        default = False,
    )

    Eating = models.BooleanField(
        help_text = _('whether the squirrel is eating or not'),
        default = False,
    )

    Foraging = models.BooleanField(
        help_text = _('whether the squirrel is foraging or not'),
        default = False,
    )

    Other_Activity = models.TextField(
        blank = True,
    )
    
    Kuks = models.BooleanField(
        help_text = _('whether the squirrel has kuks or not'),
        default = False,
    )

    Quaas = models.BooleanField(
        help_text = _('whether the squirrel has quaas or not'),
        default = False,
    )

    Moans = models.BooleanField(
        help_text = _('whether the squirrel has moans or not'),
        default = False,
    )

    Tail_Flags = models.BooleanField(
        help_text = _('whether the squirrel has tail falgs or not'),
        default = False,
    )

    Tail_Twitches = models.BooleanField(
        help_text = _('whether the squirrel has tail twitches or not'),
        default = False,
    )

    Approaches = models.BooleanField(
        help_text = _('whether the squirrel has approaches or not'),
        default = False,
    )

    Indifferent = models.BooleanField(
        help_text = _('whether the squirrel is indifferent or not'),
        default = False,
    )

    Runs_From = models.BooleanField(
        help_text = _('whether the squirrel runs from or not'),
        default = False,
    )    

    def _str_(self):
        return self.Unique_Squirrel_ID

#Create your models here.
