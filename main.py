import os

import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from streamlit_chat import message


def init():
  load_dotenv()
  # Load the OpenAI API key from the environment variable
  if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
      print("OPENAI_API_KEY is not set")
      exit(1)
  else:
      print("OPENAI_API_KEY is set")

  st.set_page_config(
    page_title="pyChatGPT",
    page_icon="🤖"
  )


def main():
  init()

  # temperature - how different answers can be (0=always same, 1=always different)
  chat = ChatOpenAI(temperature=0)

  messages = [
    SystemMessage(content="You are very helpful personal assistant")
  ]


  st.header("pyChatGPT - your personal chatbot 🤖")

  with st.sidebar:
      user_input = st.text_input(label="Input message", max_chars=100)
      #st.write(user_input)
  
  if user_input:
      # Write the message on screen
      message(user_input, is_user=True)
      # Append human message into the list of messages
      messages.append(HumanMessage(content=user_input))
      # Ask to chatbot and return response
      response = chat(messages)
      # Show AI message
      message(response.content, is_user=False)

if __name__ == "__main__":
  main()
