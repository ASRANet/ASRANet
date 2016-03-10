from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models


class Venue(models.Model):

    venue_name = models.CharField(max_length=100, unique=True, primary_key=True)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    gmaps_iFrame_src = models.URLField(max_length=1000, unique=True)

    def __unicode__(self):
        return self.venue_name


class Course(models.Model):

    course_name = models.CharField(max_length=200, unique=True, primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.ForeignKey(Venue)
    brochure = models.FileField(upload_to='PDFs/')
    main_description = models.CharField(max_length=4000)
    testimonials = models.CharField(max_length=2000)
    who_should_attend = models.CharField(max_length=2000)
    registration_cost_in_pounds = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.course_name)
        super(Course, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.course_name


class Conference(models.Model):

    conference_name = models.CharField(max_length=200, unique=True, primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.ForeignKey(Venue)
    call_for_papers_programme = models.FileField(upload_to='PDFs/')
    call_for_papers_or_programme = models.CharField(max_length=16, choices=[('Call for papers', 'Call for papers'),
                                                                            ('Programme', 'Programme')])
    description = models.CharField(max_length=4000)
    conference_themes = models.CharField(max_length=4000)
    is_partner_conference = models.BooleanField(default=False)
    registration_cost_in_pounds = models.IntegerField(default=0)
    student_cost_in_pounds = models.IntegerField(default=0)
    slug = models.SlugField()

    def __unicode__(self):
        self.slug = slugify(self.conference_name)
        return self.slug
