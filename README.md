# AI Callback

**AI Callback** is a lightweight, framework-agnostic Python library that **post-processes** responses from Large Language Models (LLMs) using **condition–action callbacks**. This allows you to:

- Append **disclaimers** for financial, medical, or legal advice
- **Redact abusive language** or flagged content
- **Enrich** responses with real-time data (like weather)
- **Track** time from request to response
- Detect **incomplete** or **inaccurate** responses and automatically re-prompt or notify users

## Features

- **Easy Integration**: Works with OpenAI, Hugging Face, or any custom LLM.
- **Modular**: Add or remove condition–action pairs without heavy refactoring.
- **Extensible**: Write your own rules for brand guidelines, disclaimers, compliance checks, etc.
- **Lightweight**: Minimal dependencies. Pure Python.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/jinoyravindran/ai-callback.git
