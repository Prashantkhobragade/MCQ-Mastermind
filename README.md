# 🧠 MCQ Mastermind: Your Personal Quiz Generator and Evaluator 📚

Welcome to MCQ Mastermind, a project that harnesses the power of artificial intelligence to create and evaluate multiple-choice quizzes. This project is perfect for educators, students, or trivia enthusiasts looking for a smart way to generate and assess quizzes.

## ⚙️ Tech Stack

This project is built using the following technologies:

- **Python**: The backbone of the project. All the scripts are written in Python.
- **Langchain**: A package used for generating and evaluating quizzes.
- **Streamlit**: A Python library used to create the web interface for the application.
- **OpenAI API**: Used to interact with the OpenAI models.
- **OpenAI Model**: gpt-3.5-turbo
- **PyPDF2**: A Python library used for handling PDF files.

## 🧩 Project Structure

- `MCQGenerator.py`: The brain of the operation! This script uses the mystical powers of the Langchain package to generate and evaluate multiple-choice quizzes.

- `StreamlitApp.py`: The face of the operation! This script provides a user-friendly Streamlit interface for the MCQ generator and evaluator.


## 🚀 Getting Started

1. **Clone the Universe (or just this repository):**
    ```
    git clone https://github.com/Prashantkhobragade/MCQ-Mastermind.git
    ```
2. **Install the Magic Spells (dependencies):**
    ```
    pip install -r requirements.txt
    ```
3. **Set up your Crystal Ball (environment variables) in a `.env` file:**
    ```
    OPENAI_API_KEY=yourapikey
    ```


## Usage

You can run the Streamlit app with the following command:
```
streamlit run StreamlitApp.py

```

## ⚠️ Limitations

Please note that the model can handle up to 4000 tokens at a time. If your input text exceeds this limit, you may need to shorten it or split it into multiple parts.


## 🤝 Contributing

I welcome wizards and witches from all houses! Feel free to open a pull request. For major changes, please open an issue first to discuss what you would like to change.


## 🎉 Final Words

I hope you enjoy using MCQ Mastermind as much as we enjoyed brewing it. Happy quizzing!
