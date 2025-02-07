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
