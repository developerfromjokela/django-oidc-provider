# -*- coding: utf-8 -*-
from django.dispatch import Signal


try:
    user_accept_consent = Signal(providing_args=['user', 'client', 'scope'])
    user_decline_consent = Signal(providing_args=['user', 'client', 'scope'])
except TypeError:
    # Starting from django 4, signals don't accept providing arguments
    user_accept_consent = Signal()
    user_decline_consent = Signal()
