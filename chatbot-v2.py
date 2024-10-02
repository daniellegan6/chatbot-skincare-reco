from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
import os


openai_API_key = os.environ["OPENAI_API_KEY"]

# while(True):