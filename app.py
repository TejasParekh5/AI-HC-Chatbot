import streamlit as st
import requests

GEMINI_API_KEY = "AIzaSyAp8amnVeQDs-gchdS4QLvfQtwrp8UcxVc"


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
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        if response.status_code == 200:
            candidates = response.json().get("candidates", [])
            if candidates and "content" in candidates[0] and "parts" in candidates[0]["content"]:
                return candidates[0]["content"]["parts"][0]["text"].strip()
            else:
                return "Sorry, I couldn't generate a response."
        else:
            return f"Sorry, there was an error processing your request. (Status code: {response.status_code})"
    except Exception as e:
        return f"Sorry, there was an error connecting to the Gemini API: {e}"


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
