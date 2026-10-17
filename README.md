🤖 AI Prompt-Based Chatbot Using Ollama

A simple Python application that generates AI responses based on user-provided prompts. It uses Ollama to run a local language model, Qwen 3.5 0.8B, and displays the generated answer directly in the terminal.

The application is designed to be lightweight and easy to use, with configurable response randomness and a maximum output length.

✨ Features
💬 Interactive Prompt Input: Enter any question or prompt through the terminal.
🤖 AI-Generated Responses: Generates answers using the Qwen language model.
🏠 Local AI Inference: Uses Ollama to run the model locally.
🎯 Consistent Responses: Sets the temperature to 0 to reduce response variability.
📏 Output Length Control: Limits generation to a maximum of 256 tokens.
⚡ Simple Execution: Requires only one prompt to generate a response.
🛡️ Error Handling: Displays an error message if AI response generation fails.
🛠️ Technologies Used
Python – Core programming language.
Ollama – Runs and manages local AI language models.
Ollama Python Library – Connects Python code to the Ollama API.
Qwen 3.5 0.8B – The configured language model, referenced by qwen3.5:0.8b.
📂 Project Structure
ollama-prompt-chatbot/
│
├── main.py
├── requirements.txt
└── README.md

main.py – Contains the prompt input and AI response generation logic.
requirements.txt – Lists the required Python package.
README.md – Project documentation.
⚙️ Installation and Setup
1. Install Ollama

Download and install Ollama from the official website:

https://ollama.com/download

Follow the installation instructions for your operating system.

2. Download the Model

Open your terminal and run:

ollama pull qwen3.5:0.8b


This downloads the model used by the application. Ensure that the model tag is available in your Ollama installation.

3. Start Ollama

Ollama normally provides its local API at:

http://localhost:11434


If Ollama is not already running, start the service with:

ollama serve


Keep the service running while using the application.

To verify that the model is installed, run:

ollama list

4. Clone the Repository
git clone <your-repository-url>
cd ollama-prompt-chatbot


Replace <your-repository-url> with your actual Git repository URL.

5. Create a Virtual Environment (Optional)
python -m venv venv


Activate the environment.

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

6. Install Dependencies

Create a requirements.txt file containing:

ollama


Install the package:

pip install -r requirements.txt

7. Run the Application

Save the Python code as main.py and execute:

python main.py


Enter a prompt when requested, and the application will display the AI-generated response.

🚀 How to Use
Ensure Ollama is running on your computer.
Confirm that the configured Qwen model is installed.
Run python main.py.
Enter a question or prompt.
Wait for the model to generate its response.
Read the answer displayed in the terminal.

The application processes one prompt per execution. Run it again to submit another prompt.

💻 Example Execution
Enter your prompt: Explain artificial intelligence in simple words.

AI: Artificial intelligence (AI) is a technology that
allows computers to perform tasks that usually require
human intelligence, such as understanding language,
recognizing images, solving problems, and learning
from data.


The example output is illustrative. Actual responses depend on the model.

🧠 How It Works

The application first asks the user to enter a prompt. It then sends that prompt to the Ollama chat API along with the selected model and generation settings.

The model generates a response, which is extracted from completion.message.content and printed in the terminal. If an exception occurs, the program displays an error message rather than terminating without an explanation.

⚙️ Configuration

The following settings control response generation:

Parameter	Value	Purpose
model	qwen3.5:0.8b	Specifies the language model.
temperature	0	Reduces randomness in generation.
num_predict	256	Limits the generated output to 256 tokens.
think	False	Requests no separate thinking output, where supported.

The generation settings can be changed in the following section:

completion = ollama.chat(
    model="qwen3.5:0.8b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    think=False,
    options={
        "temperature": 0,
        "num_predict": 256
    }
)


A temperature of 0 encourages more deterministic responses, but it does not guarantee identical outputs in every environment.

📋 Requirements
Python version compatible with the installed Ollama Python package.
Ollama installed and running locally.
The configured Qwen model downloaded.
The ollama Python package.
Sufficient system memory and computing resources for the model.

An internet connection may be required to download Ollama and the model. Once installed, prompts can generally be processed by the local model without calling a cloud-hosted AI API.

⚠️ Troubleshooting

Connection error: Make sure Ollama is running and accessible at http://localhost:11434.

Model not found: Run ollama list and verify that qwen3.5:0.8b is installed.

Import error: Install the required dependency using pip install ollama.

Short responses: Increase num_predict if you need longer answers.

Unexpected answers: Try refining your prompt or adjusting the generation settings.

🔮 Future Enhancements
Support multiple prompts in a continuous conversation.
Add conversation history.
Build a graphical interface using Streamlit or Tkinter.
Allow users to choose different Ollama models.
Add response streaming.
Save generated responses to text files.
Provide configurable output length and temperature settings.
👨‍💻 Author

Developed as a Python project demonstrating prompt-based AI generation, local language models, and integration with Ollama.

📄 License

This project is intended for educational and personal use. Add an appropriate open-source license if you plan to distribute it under specific licensing terms.
