from reports.forms import ReportsForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from reports.drafters.list import report as report_list
from reports.drafters.summary import report as report_summary


def reports(request):

    options = {
        1: report_list,
        2: report_summary
    }

    if request.method == "POST":
        form = ReportsForm(request.POST)
        if form.is_valid():
            report_type = int(form.cleaned_data['report_type'])

            response = options[report_type](**form.cleaned_data)

            if response:
                return response

            else:
                return render_to_response(
                    'reports/index.html',
                    {
                        'message': 'Ошибка формирования',
                        'message_type': 'danger',
                        'form': form,
                    },
                    context_instance=RequestContext(request))

        else:
            return render_to_response(
                'reports/index.html',
                {
                    'message': 'Ошибка формирования',
                    'message_type': 'danger',
                    'form': form,
                },
                context_instance=RequestContext(request))

    else:
        form = ReportsForm()

    return render_to_response(
        'reports/index.html',
        {'form': form},
        context_instance=RequestContext(request))
