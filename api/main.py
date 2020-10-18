import camera
import picoweb
import machine
import time
import uasyncio as asyncio

camera.init(0, format=camera.JPEG)

    
app = picoweb.WebApp('app')

@app.route('/hello')
def hello(req, resp):
    yield from picoweb.start_response(resp, "text/html")
    yield from resp.awrite('hello')
    
@app.route('/capture')
def capture(req, resp):
    #await asyncio.sleep(2)
    buf = camera.capture()
    #camera.deinit()
    if len(buf) > 0:
        yield from picoweb.start_response(resp, "image/jpeg")
        yield from resp.awrite(buf)
    else:
        picoweb.http_error(resp, 503)
app.run(host='0.0.0.0',port=80,debug=True)
