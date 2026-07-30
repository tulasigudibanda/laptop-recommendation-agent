from agent import agent
from db import init_db
from tools import load_data_if_needed

init_db()

load_data_if_needed()


# response = agent.invoke(
#     {
#         "messages": [
#             ("user", "Compare Dell G15 and ASUS TUF A15")
#         ]
#     }
# )
messages = []

while True:
    user_input = input("You: ")

    messages.append(("user", user_input))

    response = agent.invoke({
        "messages": messages
    })

    ai_message = response["messages"][-1]

    print(ai_message.content)

    messages.append(ai_message)

print(response["messages"][-1].content)


# For verbose messages
# for message in response["messages"]:
#     print("=" * 50)
#     print(type(message).__name__)
#     print(message)

# for step in agent.stream(
#     {
#         "messages": [
#             ("user", "Recommend a Lenovo laptop under 80000")
#         ]
#     }
# ):
#     print(step)