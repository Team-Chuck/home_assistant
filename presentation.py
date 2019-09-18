from .root import app
from .root import se_office_manager
from .root import se_handler


@app.handle(domain='presentation', intent='start')
def start(request, response):
    # SE query
    # se_office_manager.alarm_events
    se_handler.lights_control('test', '65')
    response.reply('Starting the presentation')


@app.handle(domain='presentation', intent='finish')
def end(request, response):
    # SE query
    se_handler.lights_control('test', '75')
    response.reply('Finishing the presentation')
