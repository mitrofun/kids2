# -*- coding: utf-8 -*-
import json

import django_rq
from django.http import HttpResponse
from rq.job import Job


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
