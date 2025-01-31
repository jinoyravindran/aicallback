# AI Callback

**AI Callback** is a lightweight, framework-agnostic Python library that **post-processes** responses from Large Language Models (LLMs) using **modular condition–action callbacks**. This design enables developers to easily:

- **Append disclaimers** for financial, medical, or legal advice  
- **Redact abusive or hateful language**  
- **Enrich outputs** with real-time data (e.g., weather)  
- **Track time** from request to response  
- Detect **incomplete** or **inaccurate** responses and automatically re-prompt  

---

## Features

- **Easy Integration**: Works with **OpenAI**, **Hugging Face**, or any custom LLM.  
- **Modular**: Add or remove condition–action pairs with minimal refactoring.  
- **Extensible**: Create new rules for compliance checks, brand guidelines, disclaimers, or specialized tasks.  
- **Lightweight**: Minimal dependencies and pure Python.  
- **Framework-Agnostic**: Doesn’t lock you into a single approach (like chain-of-thought or agent-based solutions).

---

## Table of Contents

1. [Installation](#installation)  
2. [Basic Usage](#basic-usage)  
3. [Examples](#examples)  
   1. [Hugging Face (`usage_hf.py`)](#hugging-face-usage_hfpy)  
   2. [OpenAI (`usage_openai.py`)](#openai-usage_openaipy)  
4. [Testing in a Fresh VM](#testing-in-a-fresh-vm)  
5. [Developing & Contributing](#developing--contributing)  
6. [License](#license)

---

## Installation

### 1. Clone this repository

```bash
git clone git clone https://github.com/jinoyravindran/aicallback.git
cd aicallback

2. Install dependencies

It’s recommended to use a virtual environment or conda environment to avoid polluting system-wide packages:

# Create and activate a virtual environment (example using venv)
python3 -m venv venv
source venv/bin/activate

cd aicallback/
# Install required packages
pip install -r ai_callback/requirements.txt

(On Windows, activate via venv\Scripts\activate.)

This installs dependencies like transformers, requests, openai, etc.

Basic Usage

The core library is in the ai_callback/ folder:
	•	callback.py: Defines the AICallback manager.
	•	conditions.py: Example condition functions (detecting abuse, disclaimers, incomplete responses, etc.).
	•	actions.py: Example action functions (redacting text, adding disclaimers, calling weather APIs, etc.).
	•	time_tracking.py: Simple utility to measure elapsed time from LLM request to final callback.

Workflow:
	1.	Create an instance of AICallback.
	2.	Add (condition, action) pairs.
	3.	Generate an LLM response, then call callback.process(response) to get the modified output.

Examples

We provide two main usage scripts:

Hugging Face (usage_hf.py)
	•	Generates text using GPT-2 (for a demo).
	•	Registers disclaimers, abusive language redaction, weather enrichment, incomplete response handling, and optional time tracking or toxicity detection.

To run:

python ai_callback/usage_hf.py

You’ll see the Raw Output from GPT-2 vs. the Processed Output after callbacks.

OpenAI (usage_openai.py)
	•	Similar approach but uses openai.Completion.create (or openai.ChatCompletion.create).
	•	Requires your OpenAI API key.

To run:
	1.	Export or set your OpenAI API key:

export OPENAI_API_KEY="sk-..."


	2.	Then:

python ai_callback/usage_openai.py


	3.	The script prints the LLM’s raw response and the final output after callbacks.

Testing in a Fresh VM

For reviewers or anyone wanting a clean environment (e.g., an AWS EC2 instance):
	1.	Create VM (Ubuntu 22.04 recommended).
	2.	Install basic packages:

sudo apt-get update
sudo apt-get install -y python3 python3-pip git


	3.	Clone & Install:

git clone https://github.com/jinoyravindran/aicallback.git
cd aicallback
pip3 install -r requirements.txt


	4.	Run usage_hf.py:

python3 ai_callback/usage_hf.py


	5.	(Optional) For OpenAI, set OPENAI_API_KEY and run:

python3 ai_callback/usage_openai.py



This ensures a reproducible setup for testing.

Developing & Contributing
	1.	Fork the repository and create a feature branch.
	2.	Add new conditions/actions in conditions.py and actions.py.
	3.	Test by running the usage scripts.
	4.	Submit a Pull Request for review.

Open issues for any questions or suggestions.

License

This project is licensed under the MIT License. You’re free to use, modify, and distribute the code with attribution.

Thank you for trying AI Callback. We hope it streamlines your LLM post-processing for safer, richer, and more compliant AI outputs!
