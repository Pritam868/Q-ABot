from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Training data with patterns and responses
training_data = [
    (r"my name is (.*)", ["Hello %1, How are you today?",]),
    (r"what is your name ?", ["My name is Chatty and I'm a chatbot.",]),
    (r"how are you ?", ["I'm doing good. How about You?",]),
    (r"(.*) created (.*) ?", ["Radhika created me using Python's NLTK library for Webinar 1.",]),
    (r"sorry (.*)", ["Its alright", "Its OK, never mind",]),
    (r"i'm (.*) doing good", ["Nice to hear that", "Alright :)",]),
    (r"hi|hey|hello", ["Hello", "Hey there",]),
    (r"(.*) age?", ["I'm a computer program dude. Seriously you are asking me this?",]),
    (r"what (.*) want ?", ["Make me an offer I can't refuse",]),
    (r"(.*) (location|city) ?", ['Hyderabad, India',]),
    (r"how is weather in (.*)?", ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1", "Never even heard about %1"]),
    (r"i work in (.*)?", ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]),
    (r"(.*)raining in (.*)", ["No rain since last week here in %2", "Damn its raining too much here in %2"]),
    (r"how (.*) health(.*)", ["I'm a computer program, so I'm always healthy.",]),
    (r"(.*) (sports|game) ?", ["I'm a very big fan of Football",]),
    (r"who (.*) sportsperson ?", ["Messi", "Ronaldo", "Roony"]),
    (r"who (.*) (moviestar|actor)?", ["Brad Pitt"]),
    (r"quit", ["Bye! Take care. See you soon :)", "It was nice talking to you. See you soon :)"]),
]

chatbot = Chat(training_data, reflections)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = chatbot.respond(user_input)
        print(f"User: {user_input}")
        print(f"Bot: {response}")
        return render_template('index.html', user_input=user_input, response=response)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
