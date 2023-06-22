# GPT Creator

This is a Streamlit web application that generates YouTube video titles and scripts using OpenAI's GPT model. It leverages prompts and conversation memories to create interactive and dynamic content.

## Getting Started

To run the application locally, follow these steps:

1. Install the necessary dependencies by running the command `pip install -r requirements.txt`.
2. Set your OpenAI API key by replacing <API_KEY> with your own API key in the `os.environ["OPENAI_API_KEY"]` line of the code.
3. Run the application by executing the command `streamlit run main.py`.
4. Access the application in your browser at `http://localhost:8501`.

## Usage

1. Enter your prompt in the provided text input field.
2. The application will generate a YouTube video title based on the prompt.
3. It will also perform Wikipedia research based on the prompt.
4. The generated title and researched information will be used to create a YouTube video script.
5. The generated title, script, and conversation history will be displayed on the application interface.

## Prompt Templates and Chains

- The application uses prompt templates to structure the inputs and templates for generating titles and scripts.
- The `title_template` prompts the model to generate a YouTube video title based on a given topic.
- The `script_template` prompts the model to generate a YouTube video script based on a given title and Wikipedia research.
- Conversation buffer memories are used to maintain a history of inputs and outputs for the title and script generation.

## Credits

- This application is powered by [OpenAI](https://openai.com/) and uses the [Streamlit](https://streamlit.io/) framework.
- Nicholas Renotte.

## License

This project is licensed under the [MIT License](LICENSE).
