#!/usr/bin/env python
# -*- coding: utf-8 -*-
from children.models import Child
from django.http import JsonResponse


def children_list(request):
    if request.method == 'GET':
        _children_list = [x.to_json() for x in Child.objects.all().order_by('last_name')]
        return JsonResponse({'data': sorted(_children_list, key=lambda k: k['full_name'])}, safe=False)
