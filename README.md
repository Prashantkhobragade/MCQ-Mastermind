# MCQ Generator and Evaluator

This project uses the Langchain package to generate and evaluate multiple-choice quizzes.

## Project Structure

- `MCQGenerator.py`: This script generates and evaluates multiple-choice quizzes.
- `StreamlitApp.py`: This script provides a Streamlit interface for the MCQ generator and evaluator.

## Setup

1. Clone the repository:
    ```
    git clone https://github.com/Prashantkhobragade/QnA_Generator.git
    ```
2. Install the requirements:
    ```
    pip install -r requirements.txt
    ```
3. Set up your environment variables in a `.env` file. You'll need to provide your OpenAI API key:
    ```
    OPENAI_API_KEY=yourapikey
    ```

## Usage

You can run the Streamlit app with the following command:
```
streamlit run StreamlitApp.py

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
