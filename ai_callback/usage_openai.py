# ai_callback/usage_openai.py

import openai
from ai_callback.callback import AICallback
from ai_callback.conditions import (
    detect_financial_advice,
    detect_medical_advice,
    detect_legal_advice,
    detect_abuse,
    detect_weather_query,
    detect_incomplete_response
)
from ai_callback.actions import (
    add_financial_disclaimer,
    add_medical_disclaimer,
    add_legal_disclaimer,
    redact_abusive_language,
    append_weather_info,
    handle_incomplete_response
)
from ai_callback.time_tracking import (
    start_time_tracking,
    always_true_condition,
    append_time_taken
)

def openai_usage_example():
    """
    Demonstrates how to use AI Callback with OpenAI completion.
    Includes disclaimers, moderation, weather, and time tracking.
    """

    # 1) Create a callback manager
    callback = AICallback()

    # 2) Register disclaimers
    callback.add_rule(detect_financial_advice, add_financial_disclaimer)
    callback.add_rule(detect_medical_advice, add_medical_disclaimer)
    callback.add_rule(detect_legal_advice, add_legal_disclaimer)

    # 3) Register abuse & weather
    callback.add_rule(detect_abuse, redact_abusive_language)
    callback.add_rule(detect_weather_query, append_weather_info)

    # 4) Register incomplete
    callback.add_rule(detect_incomplete_response, handle_incomplete_response)

    # 5) Register time tracking (always true condition => always append time)
    callback.add_rule(always_true_condition, append_time_taken)

    # 6) Set OpenAI API key
    openai.api_key = "<YOUR_OPENAI_API_KEY>"

    # 7) Start time tracking
    start_time_tracking()

    prompt = (
        "Give me some financial advice about investing in crypto. "
        "Also, I'd like the weather in Paris. "
        "Finally, I'd like some legal advice about a lawsuit."
    )
    print(f"USER PROMPT: {prompt}")

    # 8) Make the OpenAI request
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=80,
        temperature=0.7
    )

    raw_llm_output = response.choices[0].text.strip()
    print("\nRAW LLM OUTPUT:")
    print(raw_llm_output)

    # 9) Pass the output through the callback
    final_output = callback.process(raw_llm_output)
    print("\nFINAL OUTPUT AFTER CALLBACK:")
    print(final_output)

if __name__ == "__main__":
    openai_usage_example()
