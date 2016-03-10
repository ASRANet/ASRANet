from django.shortcuts import render
from courses.models import Course


def course(request, course_name_slug):

    context_dict = {}

    try:
        slug_course = Course.objects.get(slug=course_name_slug)
        context_dict['title'] = slug_course.event_name
        context_dict['event_name'] = slug_course.event_name
        context_dict['start_date'] = slug_course.start_date
        context_dict['end_date'] = slug_course.end_date
        context_dict['venue'] = slug_course.venue
        context_dict['brochure'] = slug_course.brochure
        context_dict['testimonials'] = slug_course.testimonials
        context_dict['main_description'] = slug_course.main_description
        context_dict['who_attend'] = slug_course.who_should_attend
        context_dict['registration_cost'] = slug_course.registration_cost_in_pounds

    except Course.DoesNotExist:
        pass

    return render(request, 'baseTemplates/courseBase.html', context_dict)


def course_list(request):
    print Course.objects.all().order_by('start_date')
    return render(request, 'baseTemplates/listCoursesConferencesBase.html',
                  {'event_list': Course.objects.all().order_by('start_date')})
