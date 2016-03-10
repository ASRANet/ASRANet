from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models


class Venue(models.Model):

    venue_name = models.CharField(max_length=100, unique=True, primary_key=True)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=30)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    gmaps_iFrame_src = models.URLField(max_length=1000, unique=True)

    def __unicode__(self):
        return self.venue_name


class Conference(models.Model):

    event_name = models.CharField(max_length=200, unique=True, primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.ForeignKey(Venue)
    url = models.URLField(blank=True)
    call_for_papers_programme = models.FileField(upload_to='PDFs/', blank=True)
    call_for_papers_or_programme = models.CharField(max_length=16, choices=[('Call for papers', 'Call for papers'),
                                                                            ('Programme', 'Programme')], blank=True)
    main_description = models.CharField(max_length=4000, blank=True)
    conference_themes = models.CharField(max_length=4000, blank=True)
    is_partner_conference = models.BooleanField(default=False, blank=True)
    registration_cost_in_pounds = models.IntegerField(default=0, blank=True)
    student_cost_in_pounds = models.IntegerField(default=0, blank=True)
    one_day_cost = models.IntegerField(default=0, blank=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.event_name)
        super(Conference, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.event_name
