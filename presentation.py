from .root import app
from .root import se_office_manager
from .root import se_handler


@app.handle(domain='presentation', intent='start')
def start(request, response):
    # SE query
    # se_office_manager.alarm_events
    lights_value = str(47)
    response.reply(f'Starting the presentation. Lights to {lights_value}')
    se_handler.lights_control('test', lights_value)
    response.listen()


@app.handle(domain='presentation', intent='finish')
def end(request, response):
    # SE query
    se_handler.lights_control('test', '75')
    response.reply('Finishing the presentation...')
