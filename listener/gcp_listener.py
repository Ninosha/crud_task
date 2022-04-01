"""
1. connect to gcp
2. see if bucket is empty and what files are on it
3. while true check if file numbers are raised message what file was created dowload all files from gcp
4. check all files data and compare dowloaded files in dataframes message updated
5. id files are less then it was message deleted
6. check





"""
import http.client
import urllib.request

h1 = http.client.HTTPConnection("http://127.0.0.1", 5000)
print(h1)

print(h1.sock)
print(h1.host)
# def poll_notifications(subscription_id):
#     client = pubsub.Client()
#     subscription = pubsub.subscription.Subscription(
#         subscription_id, client=client)
#     while True:
#         pulled = subscription.pull(max_messages=100)
#         for ack_id, message in pulled:
#             print('Received message {0}:\n{1}'.format(
#                 message.message_id, summarize(message)))
#             subscription.acknowledge([ack_id])
#
# def summarize(message):
#     # [START parse_message]
#     data = message.data
#     attributes = message.attributes
#
#     event_type = attributes['eventType']
#     bucket_id = attributes['bucketId']
#     object_id = attributes['objectId']
#     return "A user uploaded %s, we should do something here." % object_idields=False, **kwargs)
