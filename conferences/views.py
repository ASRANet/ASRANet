from django.shortcuts import render
from conferences.models import Conference


def conference(request, conference_name_slug):
    context_dict = {}

    try:

        slug_conference = Conference.objects.get(slug=conference_name_slug)

        if slug_conference.url != "":
            return render(request, slug_conference.url)

        else:
            context_dict['title'] = slug_conference.event_name
            context_dict['event_name'] = slug_conference.event_name
            context_dict['start_date'] = slug_conference.start_date
            context_dict['end_date'] = slug_conference.end_date
            context_dict['venue'] = slug_conference.venue
            context_dict['brochure'] = slug_conference.call_for_papers_programme
            context_dict['call_for_papers_or_programme'] = slug_conference.call_for_papers_or_programme
            context_dict['main_description'] = slug_conference.main_description
            context_dict['conference_themes'] = slug_conference.conference_themes
            context_dict['is_partner_conference'] = slug_conference.is_partner_conference
            context_dict['registration_cost'] = slug_conference.registration_cost_in_pounds
            context_dict['student_cost'] = slug_conference.student_cost_in_pounds
            context_dict['one_day_cost'] = slug_conference.one_day_cost

    except Conference.DoesNotExist:
        pass

    return render(request, 'baseTemplates/conferenceBase.html', context_dict)


def conference_list(request):
    return render(request, 'baseTemplates/listCoursesConferencesBase.html',
                  {'event_list': Conference.objects.all().order_by('start_date')})
