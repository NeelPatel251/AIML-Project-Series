from flask import Flask, render_template, request, jsonify
import re
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    response = get_Chat_response(input)
    update_conversation_history(input, response)
    return response

with open('Task2/knowledge_base.json', 'r') as f:
    knowledge_base = json.load(f)

conversation_history = []
user_info = {}

def get_Chat_response(question):
    global user_info

    if question.lower() in ["hello", "hi", "hii"]:
        if "name" not in user_info:
            response = "Hello! What's your name?"
        else:
            response = f"Hello {user_info['name']}! Which program are you applying for?"
    elif "name" not in user_info:
        user_info["name"] = question
        response = f"Nice to meet you, {user_info['name']}! Which program are you applying for?"
    elif "program" not in user_info:
        user_info["program"] = question
        response = f"Got it, you're applying for the {user_info['program']} program. How can I assist you with your application?"
        with open('user_info.json', 'a') as f:
            json.dump(user_info, f, indent=4)
    else:
        for keyword in knowledge_base:
            if re.search(keyword, question, re.IGNORECASE):
                response = knowledge_base[keyword]
                break
        else:
            response = get_error_response(question)

    return response

with open('Task2/error_responses.json', 'r') as f:
    error_responses = json.load(f)
    
def get_error_response(question):
    for category in error_responses:
        if category in question.lower():
            return error_responses[category]
    return "I'm sorry, I don't have enough information to answer that question. Could you please rephrase or provide more details?"


def update_conversation_history(question, response):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conversation_history.append({"question": question, "response": response, "timestamp": current_time})
    with open('conversation_history.json', 'w') as f:
        json.dump(conversation_history, f, indent=4)

if __name__ == '__main__':
    app.run()