from django.contrib import admin
from django import forms
from coursesConferences.models import Venue, Course, Conference


class CourseAdminForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea)
    testimonials = forms.CharField(widget=forms.Textarea)
    who_should_attend = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Course
        fields = ('course_name', 'start_date', 'end_date', 'venue', 'brochure', 'description', 'testimonials',
                  'who_should_attend', 'registration_cost_in_pounds')


class CourseAdmin(admin.ModelAdmin):

    #list_display = ('page', 'order', 'headline', 'element_id')
    #search_fields = ('headline', 'element_id')
    #ordering = ('page', 'order')
    form = CourseAdminForm


class ConferenceAdminForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea)
    conference_themes = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Conference
        fields = ('conference_name', 'start_date', 'end_date', 'venue', 'call_for_papers_programme',
                  'call_for_papers_or_programme', 'description', 'conference_themes', 'is_partner_conference',
                  'registration_cost_in_pounds', 'student_cost_in_pounds')


class ConferenceAdmin(admin.ModelAdmin):

    #list_display = ('page', 'order', 'headline', 'element_id')
    #search_fields = ('headline', 'element_id')
    #ordering = ('page', 'order')
    form = ConferenceAdminForm


admin.site.register(Venue)
admin.site.register(Course, CourseAdmin)
admin.site.register(Conference, ConferenceAdmin)
