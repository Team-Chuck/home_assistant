# -*- coding: utf-8 -*-
"""This module contains the dialogue states for the 'greeting' domain
in the MindMeld home assistant blueprint application
"""
from .root import app


@app.handle(intent='greet')
def greet(request, responder):
    responder.reply('Hi, I am your office facility assistant. I can help you to find the closest meeting room,'
                    ' set temperature'
                    ' and control the lights and other appliances.')


@app.handle(intent='exit')
def exit(request, responder):
    responder.reply('Have a productive day!')
