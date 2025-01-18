import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.schema import AIMessage, HumanMessage


# Streamlit app setup
st.title("Code Guru: Your AI Coding Assistant By Biswajeet Dixit")

# Options for the user
task = st.radio(
    "What do you want to do?",
    options=["Generate Code", "Debug Code", "Other"],
    help="Choose the coding task you need help with."
)

# Programming language selection
language = st.radio(
    "Which Programming Language you Prefer for the Task",
    options=["Python", "Java", "C++", "R", "JavaScript"],
    help="Choose the programming language for the task."
)

# User input text
user_input = st.text_area("Enter your code or task description:", height=200)

# Temperature and max tokens sliders
temperature = st.slider("Set Temperature:", 0.0, 1.0, 0.5, help="Controls randomness of the response.")
max_tokens = st.slider("Set Max Tokens:", 100, 2000, 500, help="Limits the response length.")

# Groq API configuration
groq_api_key = st.text_input("Enter your Groq API key:", type="password", help="Provide your Groq API key.")

if st.button("Run"):
    if not user_input.strip():
        st.warning("Please provide your code or task description.")
    elif not groq_api_key.strip():
        st.warning("Please provide your Groq API key.")
    else:
        try:
            # Load the LLaMA model using Groq API
            llm = ChatGroq(
                model="llama-3.3-70b-specdec",  # Specify the LLaMA model
                api_key="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",
                temperature=temperature,
                max_tokens=max_tokens,
            )

            # Create task-specific prompt based on the selected language
            if task == "Generate Code":
                if language == "Python":
                    prompt = f"Generate Python code for the following task:\n{user_input}"
                elif language == "Java":
                    prompt = f"Generate Java code for the following task:\n{user_input}"
                elif language == "C++":
                    prompt = f"Generate C++ code for the following task:\n{user_input}"
                elif language == "R":
                    prompt = f"Generate R code for the following task:\n{user_input}"
                elif language == "JavaScript":
                    prompt = f"Generate JavaScript code for the following task:\n{user_input}"

            elif task == "Debug Code":
                if language == "Python":
                    prompt = f"Debug the following Python code and explain the issues:\n{user_input}"
                elif language == "Java":
                    prompt = f"Debug the following Java code and explain the issues:\n{user_input}"
                elif language == "C++":
                    prompt = f"Debug the following C++ code and explain the issues:\n{user_input}"
                elif language == "R":
                    prompt = f"Debug the following R code and explain the issues:\n{user_input}"
                elif language == "JavaScript":
                    prompt = f"Debug the following JavaScript code and explain the issues:\n{user_input}"

            else:
                st.warning("This app is only designed for coding tasks.")
                prompt = f"Hey, I don’t have any expertise on other questions. Biswajeet Dixit create me Oly for Cooding Task So plese Ask  a Cooding   Question."

            # Get response from the model
            response = llm.predict(prompt)

            # Handle non-code tasks explicitly
            if task == "Other":
                st.info(response)
            else:
                st.success("Task Completed!")
                st.code(response, language=language.lower())
        except Exception as e:
            st.error(f"An error occurred: {e}")





