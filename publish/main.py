import pika
#from settings import USER, PASS, HOST
from flask import Flask
import sys
import optparse
import time
import datetime

app = Flask(__name__)

start = int(round(time.time()))

@app.route("/")
def hello_world():
    send('Message from Publisher ' + str(datetime.datetime.now()))
    return "Check publisher for message: " + "docker logs cpprabbitexample_consumer_1"

def send(message):

    message = str(message)
    # print 'trying: credentials = pika.PlainCredentials(username=USER, password=PASS)'
    # try:
    #     credentials = pika.PlainCredentials(username=USER, password=PASS)
    # except Exception:
    #     print 'Failed'
    #     print str(Exception)
    #     return 'Failed on: credentials = pika.PlainCredentials(username=USER, password=PASS) \n' + str(Exception.message)

    print 'trying: connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST, port=80, credentials=credentials))'
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host="rabbit", port=5672))
    except Exception:
        print 'Failed'
        print str(Exception)
        return 'Failed on: connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST, port=80, credentials=credentials)) \n' + str(Exception.message)

    channel = connection.channel()

    channel.queue_declare(queue='my_queue', auto_delete=False, exclusive=False)

    channel.basic_publish(exchange='amq.fanout',
                      routing_key='hello',
                      body=message)
    connection.close()

    return "Message Sent"




if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python simpleapp.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print "Missing required argument: -p/--port"
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)




