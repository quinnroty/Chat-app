import bottle
import json

# We can use import to call function in other python files we write
import chat

@bottle.route('/')
def index():
    return bottle.static_file("index.html", root="")


@bottle.route('/chat.js')
def static():
    return bottle.static_file("chat.js", root="")


@bottle.route('/chat')
def get_chat():
    chat_list = chat.get_chat()
    return json.dumps(chat_list)


@bottle.post('/send')
def do_chat():
    content = bottle.request.body.read()
    #print(content)
    content = content.decode()
    #print(content)
    content_ = json.loads(content)
    chat.add_message(content_['message'])
    return get_chat()

bottle.run(host="0.0.0.0", port=8080)