# A simple example using the HTTP plugin that shows the retrieval of a
# single page via HTTP.
 
from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPRequest
 
test1 = Test(1, "Request resource")
request1 = HTTPRequest()
test1.record(request1)
 
class TestRunner:
    def __call__(self):
        result = request1.GET("http://ysrtc.co.sin:8080/ysrtc/bookTicket?bookedBy=abc")
