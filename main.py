from agent import agent
from agent import ask_agent
# from db import init_db
# from tools import load_data_if_needed

# init_db()

# load_data_if_needed()


# response = agent.invoke(
#     {
#         "messages": [
#             ("user", "Compare Dell G15 and ASUS TUF A15")
#         ]
#     }
# )
# print(response["messages"][-1].content)

# #if you want conversational history and llm to remember the previous messages
# messages = []
# while True:
#     user_input = input("You: ")

#     messages.append(("user", user_input))

#     response = agent.invoke({"messages": messages})

#     ai_message = response["messages"][-1]

#     print(ai_message.content)

#     messages.append(ai_message)

# print(response["messages"][-1].content)


# To reuse across main.py and 
question = input("Ask a question: ")

print()

print(ask_agent(question))