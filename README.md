# MultiModelLlm

This project provides a simple interface to interact with a language model using both a command-line interface and a web interface.

## Setup

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd MultiModelLlm
    ```

2. Run the setup script to create a virtual environment, install dependencies, and launch the web application:
    ```bash
    ./setup_env.sh
    ```

## Usage

### Command-Line Interface

To use the command-line interface, run:
```bash
python main.py
```
You can ask questions directly in the terminal. Type `exit` or `quit` to end the session.

### Web Interface

After running the setup script, the web application will be available at `http://127.0.0.1:5000/`. Open this URL in your web browser to ask questions and receive responses.

## Configuration

The model configuration can be adjusted in the `config.py` file:
```python
MODEL_NAME = 'gpt-3.5-turbo'
MAX_LENGTH = 100
NUM_RETURN_SEQUENCES = 1
```

## Requirements

The required packages are listed in the `requirements.txt` file:
```pip-requirements
transformers
torch
flask
```

## License

This project is licensed under the MIT License.
