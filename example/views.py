from django.shortcuts import render

from example.autocomplete_light_registry import AutocompleteName


def form_test(request):
    # Form submission does nothing but print the POST data, if any.
    print request.POST
    return render(request, 'example/example_form.html', {
        'autocomplete_url': AutocompleteName().get_absolute_url()
    })
