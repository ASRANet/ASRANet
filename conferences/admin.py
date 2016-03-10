from django.contrib import admin
from django import forms
from conferences.models import Venue, Conference


class ConferenceAdminForm(forms.ModelForm):

    main_description = forms.CharField(widget=forms.Textarea, required=False)
    conference_themes = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Conference
        fields = ('event_name', 'start_date', 'end_date', 'venue', 'url', 'call_for_papers_programme',
                  'call_for_papers_or_programme', 'main_description', 'conference_themes', 'is_partner_conference',
                  'registration_cost_in_pounds', 'student_cost_in_pounds', 'one_day_cost')


class ConferenceAdmin(admin.ModelAdmin):

    #list_display = ('page', 'order', 'headline', 'element_id')
    #search_fields = ('headline', 'element_id')
    #ordering = ('page', 'order')
    form = ConferenceAdminForm

admin.site.register(Venue)
admin.site.register(Conference, ConferenceAdmin)
