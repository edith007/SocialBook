from channels import route


# This function will display all messages received in the console
def message_handler(message):
    print(message['text'])
    print("bhak Sale")

channel_routing = [
    route("websocket.receive", message_handler)  # register your message handler
]
