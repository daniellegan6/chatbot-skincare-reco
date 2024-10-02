##getting data from user

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI 
import os

openai_API_key = os.environ["OPENAI_API_KEY"]

#qa
def chatStaticConv():
    print("Hello, I'm here to help you diagnose your skin and find you a good skincare routin. let's go!")
    messages = {
        'age': input("How old are you?\n"),
        'gender': input("what is your gender?\n"),
        'skin_type': input("what is your skin type? oily/dry/sensitive/even/redness\n"),
        'issue': input("what is your issue? acne/red/post acne/acne scars/rinkle/ pigmantation\n"),
        'goal': input("what is your goal to achive? anti aging/remove acne/remove scars/ remove pigmantation\n"),
        'price_limit': input("what is your price limit?\n"),
        'max_products_amount': input("max prudauct do you care to use?\n"),
        'products_preferance': input("do you have products preferance?\n"),
        'extra_details': input("is there anything else i need to know?\n"),

    }
    return messages

messages = chatStaticConv()

# from langchain.prompts import PromptTemplate

# template = """
#     ###
#     You are a dermatologist, helping the user to understand her skin type and give her a skincare treatment.
#     ###

#     ###
#     Below is the user list of her skin data:
#     age: {age},
#     gender: {gender},
#     skin_type: {skin_type},
#     issue: {issue},
#     goal: {goal},
#     price_limit: {price_limit},
#     max_products_amount: {max_products_amount},
#     products_preferance: {products_preferance}
#     extra_details: {extra_details}
#     ###

#     ###
#     You need to consider these data and explain her as a dermaatologist what are the best ingredients she shoulf have in her products for\
#     the best skincare rutine.
#     after you share the ingredients list, give her the best products in the market corresponding to the ingredients based on the amount and price.
#     ###

#     YOUR ANSWER:
#     """

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a dermatologist, helping the user to understand her skin type and give her a skincare treatment."),
    ("ai", "Hello, I'm here to help you diagnose your skin and find you a good skincare routin. \
     Once I have a better understanding of your skin type and concerns, I can recommend a personalized list of products for your skincare routine. \
     let's go! \nHow old are you?\n"),
    ("human", "{age}\n"),
    ("ai", "what is your gender?\n"),
    ("human", "{gender}\n"),
    ("ai", "what is your skin type? oily/dry/combination/normal\n"),
    ("human", "{skin_type}\n"),
    ("ai", "Do you have any specific skin concerns? acne/aging/dullness/red/post acne/acne scars/rinkle/pigmantation/sensitivity\n"),
    ("human", "{issue}\n"),
    ("ai", "what is your goal to achive? anti aging/remove acne/remove scars/ remove pigmantation\n"),
    ("human", "{goal}\n"),
    ("ai", "what is your price limit?\n"),
    ("human", "{price_limit}\n"),
    ("ai", "max prudauct do you care to use?\n"),
    ("human", "{max_products_amount}\n"),
    ("ai", "Do you have products preferance?\n"),
    ("human", "{products_preferance}\n"),
    ("ai", "Is there anything else i need to know?\n"),
    ("human", "{extra_details}\n"),
    ("system", "As a dermatologist, give the user a list of the recommended ingredients for a skincare and the top products to use in her rutine based on the preice and max amount of products.")
])

chetVal = chat_template.invoke(messages)
conversation = chetVal.to_messages()

llm=ChatOpenAI()
response = llm(messages=conversation)

# response
print(response)
