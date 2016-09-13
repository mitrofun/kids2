from reports.forms import ReportsForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from reports.drafters.list import report as report_list


def report_summery(on_date):
    print("2\n")
    print(on_date)


def reports(request):

    options = {1: report_list,
               2: report_summery,
               }

    if request.method == "POST":
        form = ReportsForm(request.POST)
        if form.is_valid():
            report_date = form.cleaned_data['report_date']
            report_type = int(form.cleaned_data['report_type'])

            response = options[report_type](report_date)

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
