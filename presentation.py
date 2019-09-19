from .root import app
from .root import se_office_manager
from .root import mm_handler


@app.handle(domain='presentation', intent='start')
def start(request, response):
    mm_handler.presentation_mode('test')
    response.reply(f'Starting the presentation...')
    response.sleep()


@app.handle(domain='presentation', intent='finish')
def end(request, response):
    # SE query
    mm_handler.normal_mode('test')
    response.reply('Finishing the presentation...')
    response.sleep()
