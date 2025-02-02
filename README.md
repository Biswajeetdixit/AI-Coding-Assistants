# AI-Coding-Assistants

# 🚀 **Code Guru: Your AI Coding Assistant** 🧑‍💻

**Developed By:** *Biswajeet Dixit*  
💡 Empower your coding journey with **Code Guru**, an AI-powered assistant designed to simplify your coding tasks! Whether you're writing fresh code, debugging existing code, or exploring innovative ideas, **Code Guru** has got your back! 🎉

---

## 🌟 **Features**
- ✨ **Generate Code**: Effortlessly create functional and optimized code snippets for any project.
- 🐞 **Debug Code**: Identify and resolve coding errors with ease.
- 🌐 **Multi-Language Support**: Choose from Python, Java, C++, R, or JavaScript.
- 🎛️ **Customizable Settings**: Adjust **temperature** and **max tokens** to control response randomness and length.

---

## 🔧 **Tech Stack**
- 🖥️ **Streamlit**: For building an interactive web app.
- ⚙️ **LangChain Groq**: To integrate cutting-edge **LLaMA** models.
- 📡 **Groq API**: AI backbone delivering fast and reliable responses.
- 🐍 **Python**: Core programming language for development.

---

## 🛠️ **Setup and Installation**

1. **Clone the Repository** 🖥️  
   ```bash
   git clone https://github.com/BiswajeetDixit/Code-Guru.git
   cd Code-Guru



## **Install Dependencies** 📦
Ensure you have Python installed, then run:

```bash
Copy

pip install -r requirements.txt
```

## **Set Up API Key** 🔑
Add your Groq API Key in the .env file:

```bash
Copy

GROQ_API_KEY=your_groq_api_key_here
```
## **Run the App** 🚀
Launch the Streamlit app locally:

```bash
Copy

streamlit run app.py
```
# Enjoy Coding with Code Guru! 🎉


## 🌐 How It Works
## 1️⃣ Select Your Task
Choose between:

- Generate Code
- Debug Code
- Other
## 2️⃣ Pick Your Language
Supported languages:

- ## 🐍 Python
- ## ☕ Java
- ## ➕➕ C++
- ## 📊 R
- ## 🌐 JavaScript



## 3️⃣ Enter Your Input
Provide a description or code snippet for the task.

## 4️⃣ Set Preferences
Customize:

- 🔥 Temperature: Controls creativity in responses.
- 📏 Max Tokens: Limits the response length.
## 5️⃣ Run and Get Results
Hit the Run button and watch Code Guru do its magic! ✨



## 🤖 Why Code Guru?
- Efficiency: Save time on repetitive tasks.

- Accuracy: Get precise and optimized solutions.

- Flexibility: Supports multiple languages and tasks.

- Interactive UI: Simple and user-friendly design.


## 🏆 Achievements
- 🌟 Built using state-of-the-art LLaMA 3.3-70B Specdec model.

- 🔥 Hands-on integration with Groq API and Streamlit.

- 💻 Developed by a passionate AI enthusiast, Biswajeet Dixit.


## 🚨 Important Notes
- Privacy First: Your input is processed securely via Groq API.

- Coding Tasks Only: Code Guru is optimized for coding-related queries. Non-coding tasks will prompt a friendly reminder! 🛑




## 📋 Sample Scenarios
## 1️⃣ Generate Python Code
Input: "Create a Python function to calculate factorial recursively."
Output:

```
python
Copy

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```
## 2️⃣ Debug JavaScript Code
Input:
```
javascript
Copy

function sum(a, b) {
return a + b;
}
console.log(sum(2));
```
Output: "Missing the second parameter in the function call. Corrected code:"

```
javascript
Copy

console.log(sum(2, 3));
```



## 💡 Future Enhancements
- 🌍 Add support for more programming languages.
- 📘 Expand to include tutorials and best practices.
- 🤝 Collaborate with developers for community contributions.
## 👨‍💻 About the Developer
- Hey there! 👋 I'm Biswajeet Dixit, a passionate AI and ML developer with a vision to simplify coding for everyone. Let's connect and build amazing things together! 🚀
- 📧 Email: biswajeetdixit8495@gmail.com
  
- 📍 Location: Jajpur, Odisha, India
- 🔗 LinkedIn: Connect with me!

## 🙌 Contributing
We welcome contributions! Please follow these steps:

1 Fork the repo.
2 Create a new branch: git checkout -b feature-branch.
3 Commit your changes: git commit -m "Added a new feature".
4 Push to the branch: git push origin feature-branch.
5 Submit a pull request.
## 🛡️ License
This project is licensed under the MIT License. Feel free to use, modify, and distribute with proper attribution. 📝

## ⭐ Show Your Support
If you find Code Guru useful, please give this project a ⭐ on GitHub and share it with your friends! Let's make coding fun and easy together! 🎉
