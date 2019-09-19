from .root import app


@app.handle(domain='room_search', intent='find_room')
def find_room(request, response):
    # send request to Core for Meraki data (show on Chad demo)
    response.reply("Looking for the alternative room..."
                   "Please, check the closest Meraki dashboard for details and directions.")
    response.sleep()

