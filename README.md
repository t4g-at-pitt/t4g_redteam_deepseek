# Tech for Good at Pitt: Red Team DeepSeek

## Overview
The project aims to red team Deepseek to identify potential vulnerabilities. By engineering prompts, our goal is to understand the robustness of the model against a variety of real world attacks. These results will be used to build a dataset of redteaming prompts that helps understand the performance of the model 

### Key Features
- **Red Teaming**: Simulating real-world attacks to test the model’s security.
- **Modular Design**: Includes several components such as model handling, prompt engineering, metrics collection, and logs.
- **Requirements**: A list of dependencies required to run the project.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [TODO](#TODO)
- [License](#license)

## Requirements
Before using this project, ensure you have the following dependencies:

- Python
- OpenAI API
- Additional Libraries:
  - `pandas`

For helping installing the requirments please see [Installation](#install-dependencies).

## Project Structure
The directory structure of the project is as follows:

```
/red-teaming-llm
├── /main.py             # Main file to run red teaming tests
├── /Model.py            # Used to interact with different LLMs
├── /PromptBuilder.py    # Helps engineer prompts
├── /Log.py              # Logs red teaming effects
├── /requirements.txt    # List of project dependencies
├── /README.md           # This file
```

### File Descriptions
- **main.py**: The entry point for running red teaming tests on the model. This file orchestrates the entire testing process, including model interaction and attack execution.
- **Model.py**: Contains the code to interface with the LLM model. It includes model loading ad prompting. Can be used to interact with any model. 
- **PromptBuilder.py**: Implements prompt engineering strategies to test the model’s vulnerabilities through crafted prompts.
- **Log.py**: Handles logging functionality. It records all attempts. 

## Installation
### Clone the Repository
To get started, clone the repository to your local machine and navigate to the directory:

```bash
git clone https://github.com/jal355/t4g_redteam_deepseek.git
cd t4g_redteam_deepseek
```

### Install Dependencies

## Quick Setup — Pip (Linux / macOS / Windows)      

Follow these steps to create a local Python environment, install project dependencies with `pip`, and prepare a `.env` file. Do not add real API keys to the repo — wait to receive keys and then add them locally as described below.

Linux / macOS (bash / zsh):

```bash
# create and activate a venv
python3 -m venv .venv
source .venv/bin/activate

# upgrade pip and install project requirements
python -m pip install --upgrade pip
pip install -r requirements.txt

# copy the example env file (do NOT commit your .env)
cp .env.example .env
# Edit .env and paste the real keys when you receive them
$EDITOR .env

# run the app
python main.py
```

Windows (PowerShell):

```powershell
# create and activate a venv
py -3 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1

# upgrade pip and install requirements
python -m pip install --upgrade pip
pip install -r requirements.txt

# copy example env and edit (use Notepad or VS Code)
copy .env.example .env
notepad .env

# run the app
python main.py
```

Windows (CMD):

```cmd
py -3 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
notepad .env
python main.py
```

Notes:
- The project uses environment variables to store API keys. Do not commit `.env` (the repo includes a `.gitignore` entry for this).
- If your machine needs a special PyTorch or CUDA build, follow the instructions at https://pytorch.org/get-started/locally/ before running `pip install -r requirements.txt`.
- After you receive API keys, paste them into the local `.env` file in the format `OPENAI_API_KEY=sk-...` or `DEEPSEEK_API_KEY=or-...` depending on which provider you're using.


## Usage
### Using the modules
**INSERT EXPLANATION OF CODE**

### Running the Red Team Test
To run the red teaming test, execute the following command:

```bash
python main.py
```

### Configuration
Some settings can be adjusted via environment variables:

- **MODEL_NAME**: The model to be tested (e.g., OpenAI GPT-3, HuggingFace models).

You can modify these values directly in the code. 

### Logging Results
Logs of the test results will be saved in the log.json and modification_log.txt. These logs contain detailed information about each attempt and overall performance values. For example:

## TODO
Welcome T4G Dev Team! To get started, please follow these steps:

### Using Command Line
1. Fork the repository: Go to the repository on GitHub and click the "Fork" button. This will create a copy of the repository under your own GitHub account.
2. Clone your fork to your machine: `git clone https://github.com/<YOUR USERNAME>/t4g_redteam_deepseek.git` (This creates a local copy)
4. Make your changes or add new features.
5. Sync your fork. On the github page for your fork, there should be a "Sync Fork" option. Make sure to do this before running git pull!
6. Check to make sure you have the most recent version of main. `git pull origin main` (This prevents conflicting versions of main in pull requests)
7. Stage you changes: `git add .` (This adds all modified files. Optionally, you may select only specific files.) 
8. Commit your changes: `git commit -m '<DESCRIPTION>'` 
9. Push to your fork: `git push`
10. Open a pull request: Go to GitHub and select pull request (This pulls your changes into the main copy of the repo)

Helpful tip: If you are unsure what branch you are on, you can run `git branch` to see what branch you are currently on.

### Using Github Desktop
1. Fork the repository on the GitHub website. (This creates your own personal copy)
2. Clone your fork to GitHub desktop. Click on File -> Clone Repository (This pulls it to your machine)
4. Make your changes.
5. Check to make sure you have the most recent version of main: Select Fetch Origin in Github desktop (This prevents conflicting versions of main in pull requests)
6. Commit your changes. Open GitHub desktop and you will see the changes on the left hand side. Select the files to add and select Commit. 
7. Push your changes. Select Push origin (This pushes the changes to your copy)
8. Open a Pull Request. Go to the Github website and select pull requests. (This pulls them to the main copy)

### Installing & Using .env For API Keys
Since we are using a public repository, it's essential that we do not push API keys to the github repository. Doing so allows our keys to be viewed by anyone and potentially scraped/used by others! Once pushed, it's difficult and time consuming to remove it from not only the repo but every commit and commit history that it was in. To mitigate this, we will be using .env files to ensure that our API key stays local to our machines.

**Steps:**
1. Run `pip install python-dotenv` in your cmd
2. If you don't have one, create a file named `.gitignore` in the root of your repository. Root of your repository is simple at the base level, not inside any folders.
3. Create a file named `.env` in the root of your repository
4. You will put your API key in this `.env` file. It should be formatted like: `DEEPSEEK_API_KEY={api_key_here}` (with no brackets).
5. Inside of your `.gitignore`, add `*.env`. This will ensure that any files ending in `.env` aren't added in your git commits. 
6. You will need to push your .gitignore. When pushing, ensure your .env file isn't included in the commit! If it is, do not push your commit! Reach out to me or Julie and we can try and troubleshoot.

**Using .env vars in code:**
1. make sure you have `from dotenv import load_dotenv` and `import os` in your imports.
2. Call `load_dotenv()` before using any enviroment variables
3. You can load enviroment variables using `os.getenv('Name_of_env_variable')`, ex: `key = os.getenv('DEEPSEEK_API_KEY')`
4. That's it! It's important that we try our best not to push these keys to the repo to ensure we don't have to be generating new keys. Please reach out if you have any questions!
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
