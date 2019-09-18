import requests
from .root import app


@app.dialogue_flow(domain='easter_egg', intent='destroy_building')
def destroy_building(request, response):
    del request
    response.reply("You want to destroy the room. Right?")
    response.listen()


@destroy_building.handle(default=True)
def default_handler(request, response):
    # if we enter this flow, the assistant will do the destroy
    del request
    # response.frame // to store any temporary data through the flow
    response.reply("Got you! Preparing for THE DESTROY!!!")
    # reload directive or subprocess via http call (or add support in ANLP for this)
    # TODO: make the third turn instead (with reload or windows blue screen)
    url = "http://10.10.20.153/putxml"

    payload = """
        <Command>
        <SystemUnit>
        <Boot>
    		<Restart/>
    	<Boot>
    	</SystemUnit>
        </Command>
        """
    headers = {
        'Content-Type': "text/xml",
        'Authorization': "Basic YWRtaW46Y2lzY29wc2R0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "10.10.20.153",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "116",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    # sync for simplicity
    device_response = requests.request("POST", url, data=payload, headers=headers)
    del device_response
    response.exit_flow()
