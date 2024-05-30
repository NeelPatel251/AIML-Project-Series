import random

# Define the greeting function
def greet():
    greetings = ["Hello!", "Hi there!", "Hey, how are you?", "Greetings!"]
    print(" ")
    print(random.choice(greetings))

# Define the response function
def respond(message, conversation, user_responses):
    if "hello" in message.lower() or "hi" in message.lower():
        return "Hello! How can I assist you today?"
    elif "how are you" in message.lower():
        return "I'm doing great, thanks for asking!"
    elif "what's your name" in message.lower():
        return "I am Chatbot."
    elif "what can you do" in message.lower():
        return "I can respond to basic questions and provide helpful information."
    elif "tell me a joke" in message.lower():
        jokes = ["What is a sea monsters favorite snack? Ships and dip.",
                 "How do robots eat guacamole? With computer chips.",
                 "Why did the snail paint a giant S on his car? So when he drove by, people could say: \"Look at that S car go!\"",
                 "What do you call a happy cowboy? A jolly rancher.",
                 "What subject do cats like best in school? Hiss-tory.",
                 "Humpty Dumpty had a great fall. He said his summer was pretty good too.",
                 "My boss said: dress for the job you want, not for the job you have. So I went in as Batman."]
        return random.choice(jokes)
    elif "what is the weather here" in message.lower():
        return "I don't have access to real-time data, but I hope it's nice where you are!"
    elif "goodbye" in message.lower() or "bye" in message.lower():
        return farewell()
    elif "what did we talk about" in message.lower():
        print("--------------------------------------------")
        return "Here's a summary of our conversation:\n\n" + "\n".join(conversation)
    elif "what is my name" in message.lower():
        if "name" in user_responses:
            return f"Your name is {user_responses['name']}."
        else:
            return "I don't know your name yet."
    elif "what is my favorite" in message.lower():
        for question, answer in user_responses.items():
            if question.lower() in message.lower():
                return f"Your favorite {question.split('favorite ')[1]} is {answer}."
    else:
        return error_response(message)

# Define the error response function
def error_response(message):
    error_responses = [
        "I'm sorry, I didn't quite understand what you meant. Could you please rephrase or provide more context?",
        "Hmm, I'm having trouble comprehending your request. Could you try rewording it or providing more details?",
        "Apologies, but I'm not sure I follow. Could you clarify or ask your question in a different way?"
    ]
    return random.choice(error_responses)

# Define the farewell function
def farewell():
    farewells = ["Goodbye!", "Take care!", "Until next time!", "Farewell!"]
    farewell_message = random.choice(farewells)
    return farewell_message

# Define the function to ask questions
def ask_questions(conversation, user_responses):
    print("")
    question1 = "What is your name?"
    print("Chatbot:", question1)
    conversation.append(f"Chatbot: {question1}")
    user_answer1 = input("You: ")
    conversation.append(f"You: {user_answer1}")
    user_responses["name"] = user_answer1
    print(f"Nice to meet you {user_answer1}.")
    print("")
    
    question2 = "Can i ask you some basic Questions? Y/N"
    print("Chatbot:", question2)
    conversation.append(f"Chatbot: {question2}")
    user_answer2 = input("You: ")
    if user_answer2 == "N":
        return conversation, user_responses
    elif user_answer2 == "Y":
        print("")
        question3 = "What is your favorite hobby?"
        print("Chatbot:", question3)
        conversation.append(f"Chatbot: {question3}")
        user_answer3 = input("You: ")
        conversation.append(f"You: {user_answer3}")
        user_responses["favorite hobby"] = user_answer3
        print("Chatbot: That's a great hobby to have!")
        print("")
        
        question4 = "What is your favorite color?"
        print("Chatbot:", question4)
        conversation.append(f"Chatbot: {question4}")
        user_answer4 = input("You: ")
        conversation.append(f"You: {user_answer4}")
        user_responses["favorite color"] = user_answer4
        print("Chatbot: Interesting choice!")
        print("")
        
        question5 = "What is your favorite food?"
        print("Chatbot:", question5)
        conversation.append(f"Chatbot: {question5}")
        user_answer5 = input("You: ")
        conversation.append(f"You: {user_answer5}")
        user_responses["favorite food"] = user_answer5
        print("Chatbot: Yum, that sounds delicious!")
        
        return conversation, user_responses
    else:
        return conversation, user_responses

# Main loop
def main():
    greet()
    conversation = []
    user_responses = {}
    conversation, user_responses = ask_questions(conversation, user_responses)
    while True:
        print(" ")
        user_input = input("You: ")
        conversation.append(f"You: {user_input}")
        response = respond(user_input, conversation, user_responses)
        print("Chatbot:", response)
        conversation.append(f"Chatbot: {response}")
        if "goodbye" in user_input.lower() or "bye" in user_input.lower():
            break

if __name__ == "__main__":
    main()