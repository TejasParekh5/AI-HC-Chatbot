import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

# Download necessary NLTK data (only the first time)
nltk.download('punkt')
nltk.download('stopwords')

# Load a pre-trained Hugging Face model suitable for medical queries
model_name = "gpt2"  # Using GPT-2 model as an alternative
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Define a medical disclaimer to be appended to all responses.
MEDICAL_DISCLAIMER = ("\n\n*Disclaimer: I am not a licensed medical professional. "
                      "For medical emergencies or serious health concerns, please seek professional help immediately.*")

# Define a function to preprocess user input (e.g. lowercasing, removing stopwords)


def preprocess_text(text):
    # Lowercase and remove non-alphanumeric characters (except spaces)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    tokens = word_tokenize(text)
    filtered_tokens = [
        word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(filtered_tokens)

# Define healthcare-specific response logic.


def healthcare_chatbot(user_input):
    processed_input = preprocess_text(user_input)

    # Rule-based responses for common healthcare queries.
    if "emergency" in processed_input or "chest pain" in processed_input or "severe" in processed_input:
        return ("It sounds like you might be describing a potentially serious situation. "
                "If this is an emergency, please call your local emergency services immediately." + MEDICAL_DISCLAIMER)
    elif "symptom" in processed_input or "fever" in processed_input or "cough" in processed_input:
        return ("It seems like you're experiencing some symptoms. "
                "While I can provide general information, please note that I'm not a substitute for professional medical advice. "
                "If your symptoms worsen or concern you, consider consulting a healthcare provider." + MEDICAL_DISCLAIMER)
    elif "appointment" in processed_input:
        return ("I can help guide you through the appointment process. "
                "Would you like me to assist in finding nearby clinics or scheduling an appointment? Please provide your location details." + MEDICAL_DISCLAIMER)
    elif "medication" in processed_input or "prescription" in processed_input:
        return ("It's important to follow your doctor's instructions regarding medication. "
                "For any changes or concerns, please consult your healthcare provider. " + MEDICAL_DISCLAIMER)
    elif "mental health" in processed_input or "anxiety" in processed_input:
        return ("I understand that mental health is very important. "
                "If you are experiencing distress or need someone to talk to, please consider reaching out to a trusted professional or a support helpline." + MEDICAL_DISCLAIMER)
    else:
        # For other inputs, use the Hugging Face model to generate a response.
        # We include the medical disclaimer in the prompt to bias the generation.
        prompt = user_input + \
            "\n\nPlease provide detailed and compassionate information in response."
        response = chatbot(prompt, max_length=300, num_return_sequences=1)[
            0]['generated_text']

        # Append the disclaimer to the generated text.
        return response + MEDICAL_DISCLAIMER

# Streamlit web app interface.


def main():
    st.title("Healthcare Assistant Chatbot")
    st.markdown(
        "**Note:** I am a virtual assistant and not a substitute for professional medical advice.")

    # Display a simple text input for user queries.
    user_input = st.text_input("How can I assist you today?", "")

    if st.button("Submit"):
        if user_input:
            st.write("**User:**", user_input)
            response = healthcare_chatbot(user_input)
            st.write("**Healthcare Assistant:**", response)
        else:
            st.write("Please enter a query.")


if __name__ == "__main__":
    main()
