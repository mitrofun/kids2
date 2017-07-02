#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import *  # noqa

try:
    from .local import *  # noqa
except ImportError:
    print("Can't find module settings.local! Make it from local.py.skeleton")
