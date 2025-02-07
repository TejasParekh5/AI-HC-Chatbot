# AI Healthcare Chatbot

## Overview

The **AI Healthcare Chatbot** is an AI-driven virtual assistant designed to provide immediate, context-aware responses to healthcare queries. It leverages natural language processing (NLP) techniques to analyze user inputs and determine the best response—using a rule-based system for critical symptoms and a pre-trained GPT-2 model (via Hugging Face Transformers) for general inquiries. Every response includes a standard medical disclaimer to remind users that the chatbot is not a substitute for professional medical advice.

This repository contains the complete codebase and project report detailing the design, implementation, and evaluation of the chatbot.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Literature Survey](#literature-survey)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **User-Friendly Interface:** Built using Streamlit for a simple and interactive web experience.
- **NLP Preprocessing:** Utilizes NLTK and regular expressions for text cleaning, tokenization, and stopword removal.
- **Rule-Based Emergency Handling:** Detects critical keywords (e.g., "emergency", "chest pain") and returns predefined responses advising immediate action.
- **Generative Response Module:** For non-critical queries, a GPT-2 model generates detailed, context-aware responses.
- **Medical Disclaimer:** All responses include a disclaimer reminding users to seek professional medical help when needed.

## System Architecture

The system is organized into several key modules:
1. **User Input Module:** Captures queries via a web interface.
2. **Preprocessing Module:** Normalizes and tokenizes the input text using NLTK and regex.
3. **Healthcare-Specific Rule-Based Module:** Checks for critical symptoms and returns immediate, safe responses.
4. **Response Generation Module:** Uses a pre-trained GPT-2 model (via Hugging Face Transformers) to generate responses for general queries.
5. **Disclaimer Module:** Appends a standardized medical disclaimer to every response.
6. **User Interface Module:** Provides a clean, accessible interface through Streamlit.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/ai-healthcare-chatbot.git
   cd ai-healthcare-chatbot
   
2. **Create and activate a virtual environment**
  python -m venv venv
  # On Windows:
  venv\Scripts\activate
  # On macOS/Linux:
  source venv/bin/activate

3. **Create and activate a virtual environment**
  pip install -r requirements.txt

4. **Download the necessary NLTK data (if not already available)**
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

## Usage
Start the chatbot application using Streamlit:
*streamlit run app.py*
Then, open your browser and navigate to the local URL (typically http://localhost:8501) to interact with the chatbot.

## Literature Survey
The development of this chatbot is informed by current research in AI and healthcare, including:
  1.Conversational Agents in Healthcare: Systematic reviews that discuss the role of chatbots in enhancing patient engagement and reducing wait times.
  2.Context-Aware Chatbots: Studies highlighting the effectiveness of transformer-based models like GPT-2 in generating human-like, context-aware responses for healthcare applications 
  3.Challenges in Healthcare Chatbots: Research identifying limitations such as scalability, context maintenance, and privacy concerns in existing systems 

## Contributing
Contributions to improve the chatbot are welcome! To contribute:

Fork the repository.
Create a new branch:
*git checkout -b feature/your-feature-name*
Commit your changes:
*git commit -m "Add feature or fix bug"*
Push your branch:
*git push origin feature/your-feature-name*
Open a pull request for review.

## License
This project is licensed under the MIT License.

## Acknowledgements
Project Mentor: Jay Rathod, for invaluable guidance and support.
TechSaksham: For providing the platform and resources during the AICTE Internship on AI.
Open-Source Community: Gratitude to the developers behind Streamlit, Hugging Face Transformers, and NLTK for their excellent libraries.
