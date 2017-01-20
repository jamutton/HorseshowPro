from django.db import models
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

STYLE_CHOICES = (
    ('ENGLISH', 'English'),
    ('WESTERN', 'Western'),
    ('NONE', 'None'),
)

DIVISION_CHOICES = (
    ('OPEN', 'Open'),
    ('JUNIOR', 'Junior'),
    ('INTERMEDIATE', 'Intermediate'),
    ('SENIOR', 'Senior'),
)

RIDER_FLAGS = (
    ('NOVICE','Novice'),
    ('OOC', 'Out of County'),
)

SHOWCLASS_FLAGS = (
    ('MEDALSQUAL','Qualifies for Medals'),
    ('STATEQUAL', 'Qualifies for State'),
    ('TRAIL',     'Score as Trail'),
)

# Create your models here.
class Club(models.Model):
    Name = models.CharField(unique=True, max_length=48, help_text="The name of the club")
    def __unicode__(self):
        return self.Name

class Location(models.Model):
    Name = models.CharField(unique=True, max_length=64, help_text="A unique name for this location")
    StreetAddress = models.CharField(max_length=200, help_text="The street address for this location")
    City = models.CharField(max_length=64, help_text="The city that this location resides in")
    MailRegion = models.CharField(max_length=64, help_text="The state that this location resides in")
    PostalCode = models.CharField(max_length=24, help_text="The postal code for this locaiton")
    def __unicode__(self):
        return self.Name

class Seat(models.Model):
    Name = models.CharField(max_length=24)
    Style = models.CharField(max_length=24, choices=STYLE_CHOICES) # may not need this
    def __unicode__(self):
        return self.Name

class Show(models.Model):
    Name = models.CharField(unique=True, max_length=64)
    Description = models.CharField(max_length=255, blank=True, null=True)
    Date = models.DateField(help_text="The date of the show")
    EndDate = models.DateField(null=True, help_text="[optional] The date the show ends (if the show is longer then one day)")
    Location = models.ForeignKey('Location')
    def __str__(self):
        return self.Name
    def __unicode__(self):
        return self.Name
    @models.permalink
    def get_absolute_url(self):
        return ( 'horse_show.views.update', [str(self.id)] )
    @models.permalink
    def get_read_url(self):
        return ( 'horse_show.views.read', [str(self.id)] )

class HighpointPlacing(models.Model):
    Place = models.IntegerField(primary_key=True)
    Points = models.IntegerField()
    def __unicode__(self):
        return str(self.Place)
    class Meta:
        ordering = ['Place']

class Division(models.Model):
    Division = models.CharField(max_length=24, primary_key=True)
    Exclusivity = models.BooleanField(default=True, help_text="Enforces that rider entries MUST match the division when assigned to a class.")
    def __unicode__(self):
        return self.Division

class Rider(models.Model):
    LastName = models.CharField(max_length=64)
    FirstName = models.CharField(max_length=64)
    MiddleInitial = models.CharField(max_length=2, blank=True, null=True)
    EmailAddress = models.EmailField(blank=True, null=True)
    PhoneNumber = models.CharField(max_length=16, blank=True, null=True)
    Grade = models.CharField(max_length=4, blank=True, null=True)
    Birthday = models.DateField(blank=True, null=True)
    StreetAddress = models.CharField(max_length=200, blank=True, null=True)
    City = models.CharField(max_length=64, blank=True, null=True)
    MailRegion = models.CharField(max_length=64, blank=True, null=True)
    PostalCode = models.CharField(max_length=24, blank=True, null=True)
    Novice = models.BooleanField(default=False)
    Club = models.ForeignKey('Club')
    HighpointTeam = models.ForeignKey('HighpointTeam', blank=True, null=True)
    Division = Division = models.ForeignKey('Division')
    #Division = models.CharField(max_length=24, choices=DIVISION_CHOICES)
    def __unicode__(self):
        return self.LastName + ", " + self.FirstName + " " + str(self.MiddleInitial)

class RiderAttributes(models.Model):
    '''Defines additional attribute flags that can be assigned to a rider'''
    Rider = models.ManyToManyField('Rider')
    Flag = models.CharField(max_length=24, help_text="The assigned attribute of this rider", choices=RIDER_FLAGS)

class Number(models.Model):
    Number = models.CharField(primary_key=True, max_length=5)
    Rider = models.ForeignKey('Rider')
    HorseName = models.CharField(max_length=48)
    HighpointDivision = models.ForeignKey('Seat', null=True, blank=True)
    def __unicode__(self):
        return str(self.Number)
    class Meta:
        order_with_respect_to = 'Rider'

class HighpointTeam(models.Model):
    '''Defines a Team of riders that can collectively qualify for highpoint'''
    TeamName = models.CharField(primary_key=True, max_length=24, help_text="The name of the Hightpoint Team")
    def __unicode__(self):
        return self.TeamName

class ShowClass(models.Model):
    Name = models.CharField(max_length=48)
    Seat = models.ForeignKey('Seat')
    FormName = models.CharField(max_length=64, blank=True, null=True, verbose_name="text to match with entry form")
    Division = models.ForeignKey('Division')
    #Division = models.CharField(max_length=24, choices=DIVISION_CHOICES, blank=True)
    isHighpoint = models.BooleanField(default=True, verbose_name="counts toward highpoint")
    isTrail = models.BooleanField(default=False, verbose_name="scored as trail")
    isMedals = models.BooleanField(default=False, verbose_name="scored as medals")
    isMedalsQualifying = models.BooleanField(default=True, verbose_name="qualification for medals")
    isStateQualifying = models.BooleanField(default=False, verbose_name="qualificaiton for state")
    def __unicode__(self):
        return self.Name
    class Meta:
        verbose_name_plural = 'Classes'
        verbose_name = 'Class'

class ShowClassFlags(models.Model):
    ShowClass = models.ManyToManyField('ShowClass')
    Flag = models.CharField(max_length=24, help_text="The name of the flag for this class", choices=SHOWCLASS_FLAGS)
    def __unicode__(self):
        return self.Flag
    class Meta:
        verbose_name = "Class Flag"

class ShowClassSchedule(models.Model):
    ShowClass = models.ForeignKey('ShowClass')
    Show = models.ForeignKey('Show')
    ShowPosition = models.IntegerField()
    ClassNumber = models.CharField(max_length=8, blank=True, null=True)
    class Meta:
        verbose_name = 'Class Schedule'
        verbose_name_plural = 'Class Schedules'
        unique_together = ('Show', 'ShowPosition')
        ordering = ['ShowPosition']

class ExtraFee(models.Model):
    Name = models.CharField(max_length=64)
    Description = models.CharField(max_length=255, blank=True, null=True)
    Cost = models.DecimalField(max_digits=6, decimal_places=2)
    Default = models.BooleanField()
    def __unicode__(self):
        return self.Name

class Danish(models.Model):
    Name = models.CharField(max_length=16)
    isMedalsQualifying = models.BooleanField(default=True, verbose_name="Earning this danish qualifies the rider for medals in an appropriate class")
    isStateQualifying = models.BooleanField(default=False, verbose_name="Earning this danish qualifies the rider for State in an appropriate class")
    def __unicode__(self):
        return self.Name
    class Meta:
        verbose_name_plural = 'Danishes'

class Judge(models.Model):
    Name = models.CharField(max_length=48)
    def __unicode__(self):
        return self.Name

class Judging(models.Model):
    Show = models.ForeignKey('Show', null=True, blank=True)
    ShowClass = models.ForeignKey('ShowClass')
    Number = models.ForeignKey('Number')
    SeatRidden = models.ForeignKey('Seat')
    Place = models.ForeignKey('HighpointPlacing')
    #Place = models.IntegerField(help_text="What place did the rider recieve")
    Judge = models.ForeignKey('Judge', help_text="Who was the judge for this judging")
    Danish = models.ForeignKey('Danish', help_text="What danish did the rider recieve", default=None, null=True, blank=True)
    Point = models.BooleanField(help_text="Did the rider 'Point' in the class", default=False)
    Comments = models.CharField(max_length=255, help_text="What comments did the judge have for the rider", null=True, blank=True)

class Entry(models.Model):
    '''A number entering in a show'''
    Number = models.ForeignKey('Number')
    Show = models.ForeignKey('Show')
    def __unicode__(self):
        return str(self.Number)
    class Meta:
        verbose_name_plural = 'Entries'
        unique_together = ('Number', 'Show')

class EntryType(models.Model):
    '''EntryTypes are meant to categorize entries.  This is where you'd expect to put classes of
    entries such as "late" or "earlybird" or "clubmember", etc... Things that would be a primary
    differentiator of the entry'''
    Name = models.CharField(max_length=24)
    def __unicode__(self):
        return self.Name

class ClassEntry(models.Model):
    '''Binds an entry to a class as a given EntryType.  Allows you to say that these were early
    while these were "day-of", etc...'''
    Entry     = models.ForeignKey('Entry')
    ShowClass = models.ForeignKey('ShowClass')
    EntryType = models.ForeignKey('EntryType', blank=True, null=True, editable=False)
    def validate_unique(self, *args, **kwargs):
        super(ClassEntry, self).validate_unique(*args, **kwargs)
        show = self.Entry.Show
        if len(ShowClassSchedule.objects.filter(Show=show, ShowClass=self.ShowClass)) == 0:
            raise ValidationError("Attempt to add entry for show that was not scheduled")
        if self.ShowClass.Division and \
                    self.ShowClass.Division.Exclusivity and \
                    self.Entry.Number.Rider.Division != self.ShowClass.Division:
            raise ValidationError("Rider division differs from class division")
        #clsEntry = ClassEntry.objects.filter(name=self.name)
        #class ShowClassSchedule(models.Model):
        #    ShowClass = models.ForeignKey('ShowClass')
        #    Show = models.ForeignKey('Show')
        #    ShowPosition = models.IntegerField()
        #
        #if qs.filter(zone__site=self.zone__site).exists():
        #    raise ValidationError({'name':['Name must be unique per site',]})

class FeedBackQuestion(models.Model):
    Question = models.CharField(max_length=255)

class FeedBack(models.Model):
    Show = models.ForeignKey('Show')
    Rider = models.ForeignKey('Rider')
    Answer = models.ManyToManyField('FeedBackQuestion', through='FeedBackResponse')

class FeedBackResponse(models.Model):
    FeedBack = models.ForeignKey('FeedBack')
    FeedBackQuestion = models.ForeignKey('FeedBackQuestion')
    Answer = models.IntegerField()
