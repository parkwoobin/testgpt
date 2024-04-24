import streamlit as st
import openai
import datetime

# https://testgpt-krqnhuu7i9salyzrprwyff.streamlit.app/
# 

def ask_gpt(prompt, model, apikey):
    client = openai.OpenAI(api_key = apikey)
    response = client.chat.completions.create(model=model, messages=prompt)
    gptResponse = response.choices[0].message.content
    return gptResponse


def main():
    st.set_page_config(page_title="중간시험", layout="wide")
    

    st.header("ChatGPT ""텍스트"" 비서 서비스")

    st.markdown("---")


    with st.expander("채팅비서 프로그램에 관하여", expanded=False):
        st.write("""
                - 중간시험
                - 채팅비서 프로그램 웹 페이지는 streamlit으로 제작되었습니다.
                 """)
        
        st.markdown("")

    
        if "chat" not in st.session_state:
            st.session_state["chat"] = []

        if "OPENAI_API" not in st.session_state:
            st.session_state["OPENAI_API"] = ""

        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "당신은 채팅비서입니다. 한국어로 답변하세요 20자 내로"}]

        if "check_audio" not in st.session_state:
            st.session_state["check_reset"] = False

    with st.sidebar:

        st.session_state["OPENAI_API"] = st.text_input(label="OPENAI API 키", placeholder="Enter your API key", value="", type="password")
        

        st.markdown(" --- ")



        model = st.radio(label="GPT 모델", options=["gpt-3.5-turbo", "gpt-4"])
        

        st.markdown(" --- ")



       
        if st.button(label="🔄️ 리셋"):

            st.session_state["chat"] = []
            st.session_state["messages"] = [{"role": "assistant", "content": "당신은 채팅비서입니다. 한국어로 답변하세요 20자 내로"}]
            st.session_state["check_reset"] = True
        
    
    

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("질문하기")
        if st.session_state["OPENAI_API"]:
            response = st.chat_input("텍스트를 입력하세요")

    
    with col2:
        st.markdown("질문/답변")
        if not st.session_state["OPENAI_API"]:
            st.info("Please add your OpenAI API key!",icon="⚠️")
            st.stop()

        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])
        

        if  response:

   

            client = openai.OpenAI(api_key=st.session_state["OPENAI_API"])
            st.session_state.messages.append({"role": "user", "content": response})
            st.chat_message("user").write(response)
            response = client.chat.completions.create(model = model, messages=st.session_state.messages)
            msg = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": msg})
            st.chat_message("assistant").write(msg)




if __name__=="__main__":
    main()
