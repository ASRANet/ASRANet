from django.contrib import admin
from django import forms
from courses.models import Venue, Course


class CourseAdminForm(forms.ModelForm):

    main_description = forms.CharField(widget=forms.Textarea)
    testimonials = forms.CharField(widget=forms.Textarea)
    who_should_attend = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Course
        fields = ('event_name', 'start_date', 'end_date', 'venue', 'brochure', 'main_description', 'testimonials',
                  'who_should_attend', 'registration_cost_in_pounds')


class CourseAdmin(admin.ModelAdmin):

    #list_display = ('page', 'order', 'headline', 'element_id')
    #search_fields = ('headline', 'element_id')
    #ordering = ('page', 'order')
    form = CourseAdminForm

admin.site.register(Venue)
admin.site.register(Course, CourseAdmin)
