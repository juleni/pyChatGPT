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

  if "messages" not in st.session_state:
      st.session_state.messages = [
        SystemMessage(content="You are very helpful personal assistant. Your name is Freddy Krueger.")
      ]


  st.header("pyChatGPT - your personal chatbot 🤖")

  with st.sidebar:
      user_input = st.text_input(label="Input message", max_chars=100)
      #st.write(user_input)
  
  if user_input:
      # Append human message into the list of messages
      st.session_state.messages.append(HumanMessage(content=user_input))
      # Ask to chatbot and return response
      with st.spinner("Thinking"):
          response = chat(st.session_state.messages)
      # Append AI message into the list of messages
      st.session_state.messages.append(AIMessage(content=response.content))

  messages = st.session_state.get("messages", [])
  # messages[1:] - start from the second message, the first is SystemMessage
  for i, msg in enumerate(messages[1:]):  
      if i % 2 == 0:
          # Show user's message on screen
          message(msg.content, is_user=True, key=str(i) + "_user", avatar_style="micah")
      else:
          # Show AI's message on screen
          message(msg.content, is_user=False, key=str(i) + "_ai", avatar_style="croodles")


if __name__ == "__main__":
  main()
