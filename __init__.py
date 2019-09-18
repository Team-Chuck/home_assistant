# -*- coding: utf-8 -*-
"""This module contains the MindMeld home assistant blueprint application"""
from office_assistant.root import app

import office_assistant.greeting
import office_assistant.smart_home
import office_assistant.times_and_dates
import office_assistant.unknown
import office_assistant.weather  # noqa: ignore=F401
import office_assistant.easter_egg
import office_assistant.presentation

__all__ = ['app']
