import json
import logging

import django_rq
from django.http import HttpResponse
from rq.job import Job

from reports.forms import ReportsForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from reports.drafters.list import report as report_list
from reports.drafters.summary import report as report_summary

log = logging.getLogger(__name__)


def reports_view(request):

    options = {
        1: report_list,
        2: report_summary
    }

    if request.method == "POST":
        form = ReportsForm(request.POST)
        if form.is_valid():
            report_type = int(form.cleaned_data['report_type'])

            job = options[report_type].delay(**form.cleaned_data)

            if job:
                response = render_to_response(
                    'reports/index.html',
                    {
                        'message': 'Формирование отчета началось',
                        'message_type': 'success',
                        'form': form
                    },
                    context_instance=RequestContext(request))
                response.set_cookie('kids_report_job', job.get_id())
                response.set_cookie('kids_report_job_task', '1')
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


def status_view(request):
    ret = {}
    job_id = request.GET.get('job_id')
    redis_conn = django_rq.get_connection()
    job = Job.fetch(job_id, redis_conn)
    if job.is_finished:
        ret = {'status': 'finished'}
    elif job.is_queued:
        ret = {'status': 'in-queue'}
    elif job.is_started:
        ret = {'status': 'waiting'}
    elif job.is_failed:
        ret = {'status': 'failed'}

    return HttpResponse(json.dumps(ret), content_type="application/json")


def reports_file(request):
    job_id = request.GET.get('job_id')
    redis_conn = django_rq.get_connection()
    job = Job.fetch(job_id, redis_conn)
    response = HttpResponse(job.return_value, content_type="application/vnd.ms-excel")
    response['Content-Disposition'] = 'attachment; filename=report.xls'
    return response
