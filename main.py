import streamlit as st
from streamlit_chat import message


def main():
  st.set_page_config(
    page_title="pyChatGPT",
    page_icon="🤖"
  )

  st.header("pyChatGPT - your personal chatbot 🤖")

  message("Hello, how are you?")
  message("I'm fine", is_user=True)

  with st.sidebar:
      user_input = st.text_area(label="Input message", max_chars=100)
      st.write(user_input)


if __name__ == "__main__":
  main()
