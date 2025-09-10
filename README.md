# Healthcare Chatbot

This is a healthcare chatbot built with [Rasa](https://rasa.com/). It can answer frequently asked questions about healthcare, provide information about outbreak alerts, and give vaccination schedules.

## Setup

**Note:** Please use Python 3.10 for this project.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/healthcare-chatbot.git
    cd healthcare-chatbot
    ```

2.  **Install uv:**
    ```bash
    # On macOS and Linux
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # On Windows
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

3.  **Create a virtual environment:**
    ```bash
    uv venv --python 3.10
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

    **Install rasa:**
    ```bash
    uv pip install rasa
    ```

4.  **Install dependencies:**
    ```bash
    uv pip install -r requirements.txt
    ```

## Usage

1.  **Train the Rasa model:**
    ```bash
    rasa train
    ```

2.  **Run the action server:**
    Open a new terminal and run:
    ```bash
    rasa run actions
    ```

3.  **Run the chatbot:**
    In the first terminal, run:
    ```bash
    rasa shell
    ```
    You can now talk to the chatbot in the terminal.

## Project Structure

-   `actions/`: Contains the custom action code for the chatbot.
-   `data/`: Contains the NLU training data, stories, and rules.
-   `knowledge_base/`: Contains the JSON files used as a knowledge base for the chatbot.
-   `models/`: Stores the trained Rasa models.
-   `config.yml`: The main configuration file for the Rasa model.
-   `domain.yml`: The chatbot's domain, including intents, entities, actions, and responses.
-   `endpoints.yml`: Configuration for the action server and other endpoints.
-   `requirements.txt`: The Python dependencies for the project.
