from backend.core import run_llm
import streamlit as st

st.header("LangChain Documentation Assistant")

prompt = st.text_input("Prompt", placeholder="Enter your prompt")

if (
    "user_prompt_history" not in st.session_state
    and "chat_answers_history" not in st.session_state
    and "chat_history" not in st.session_state
):
    st.session_state["user_prompt_history"] = []
    st.session_state["chat_answers_history"] = []
    st.session_state["chat_history"] = []


def create_sources_str(source_urls: set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_str = "Sources:\n"
    for i, source in enumerate(sources_list, 1):
        sources_str += f"{i}. {source}\n"
    return sources_str


if prompt:
    with st.spinner("Thinking..."):
        response = run_llm(query=prompt, chat_history=st.session_state.chat_history)
        sources = set([doc.metadata["source"] for doc in response["source_documents"]])

        formatted_response = f"{response["result"]}\n\n {create_sources_str(sources)}"

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)
        st.session_state["chat_history"].append(("human", prompt))
        st.session_state["chat_history"].append(("ai", response["result"]))

if st.session_state.chat_answers_history:
    for response, user_query in zip(
        st.session_state.chat_answers_history, st.session_state.user_prompt_history
    ):
        st.chat_message("user").write(user_query)
        st.chat_message("assistant").write(response)
