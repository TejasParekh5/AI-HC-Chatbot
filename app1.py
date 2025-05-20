import streamlit as st
import requests

OPENAI_API_KEY = " Add your API Key here "

def generate_prompt(user_input):
    return (
        "You are a helpful and knowledgeable healthcare assistant. "
        "For any symptoms or health concerns described by the user, provide:\n"
        "- Possible common causes (if appropriate)\n"
        "- Step-by-step home care advice and precautions\n"
        "- Medications that may help (if safe to suggest over-the-counter options)\n"
        "- Clear guidance on when to seek professional medical attention\n"
        "Always be compassionate, clear, and concise. Do not diagnose, but give practical next steps.\n"
        f"User: {user_input}\nAssistant:"
    )


def call_chatbot_api(user_input):
    prompt = generate_prompt(user_input)
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful and knowledgeable healthcare assistant. Provide clear, concise, and medically accurate advice. If the user describes symptoms, suggest possible next steps, precautions, and when to see a doctor. Always be compassionate, clear, and concise. Do not diagnose, but give practical next steps."},
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 256,
        "temperature": 0.5
    }
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        elif response.status_code == 429:
            # Add a more helpful message for the user
            return (
                "Sorry, the service is receiving too many requests right now (rate limit exceeded). "
                "This is a temporary issue from the backend provider. "
                "Please wait a few minutes and try again. "
                "If this happens repeatedly, consider using your own OpenAI API key or upgrading your OpenAI plan."
            )
        else:
            return f"Sorry, there was an error processing your request. (Status code: {response.status_code})"
    except Exception as e:
        return f"Sorry, there was an error connecting to the OpenAI API: {e}"


def healthCare_chatbot(user_input):
    return call_chatbot_api(user_input)


def main():
    st.set_page_config(page_title="Healthcare Assistant ChatBot",
                       page_icon="💬", layout="centered")
    st.title("💬 Healthcare Assistant ChatBot")
    st.markdown(
        "**Disclaimer:** This chatbot is for informational purposes only and does not replace professional medical advice.")

    # Sidebar with info and disclaimer
    with st.sidebar:
        st.header("About")
        st.write(
            "This chatbot provides general medical information using an AI language model. "
            "It is **not** a replacement for professional medical advice, diagnosis, or treatment."
        )
        st.write(
            "For urgent or serious health concerns, always contact a licensed healthcare provider."
        )
        st.markdown("---")
        st.write("Developed for educational and informational purposes only.")

    # Conversation history using session state
    if "history" not in st.session_state:
        st.session_state.history = []

    st.markdown("### Chat")
    user_input = st.text_area(
        "How can I assist you today?", "", height=80, max_chars=500)

    col1, col2 = st.columns([1, 1])
    submit = col1.button("Submit", use_container_width=True)
    clear = col2.button("Clear Conversation", use_container_width=True)

    if clear:
        st.session_state.history = []

    if submit and user_input.strip():
        with st.spinner("Processing your query, please wait..."):
            try:
                response = healthCare_chatbot(user_input)
            except Exception as e:
                response = "Sorry, there was an error processing your request."
                st.error(e)
        st.session_state.history.append(("User", user_input))
        st.session_state.history.append(("Healthcare Assistant", response))

    # Display conversation history
    if st.session_state.history:
        for speaker, message in st.session_state.history:
            if speaker == "User":
                st.markdown(f"**🧑 {speaker}:** {message}")
            else:
                st.markdown(f"**🤖 {speaker}:** {message}")


if __name__ == "__main__":
    main()
