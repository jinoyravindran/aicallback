# ai_callback/usage_hf.py

from transformers import pipeline
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

def huggingface_usage_example():
    """
    Demonstrates how to use AI Callback with Hugging Face Transformers.
    Includes disclaimers, moderation, weather, and time tracking.
    """

    # 1) Create a text generation pipeline (GPT-2 for demo)
    generator = pipeline("text-generation", model="gpt2", max_length=60)

    # 2) Create a callback manager
    callback = AICallback()

    # 3) Register disclaimers
    callback.add_rule(detect_financial_advice, add_financial_disclaimer)
    callback.add_rule(detect_medical_advice, add_medical_disclaimer)
    callback.add_rule(detect_legal_advice, add_legal_disclaimer)

    # 4) Register abuse & weather
    callback.add_rule(detect_abuse, redact_abusive_language)
    callback.add_rule(detect_weather_query, append_weather_info)

    # 5) Register incomplete
    callback.add_rule(detect_incomplete_response, handle_incomplete_response)

    # 6) Register time tracking
    callback.add_rule(always_true_condition, append_time_taken)
    start_time_tracking()

    # 7) Generate text from HF
    prompt = (
        "What's the climate in Berlin like right now? Also, can you provide me with medical advice on headaches?"
    )
    print(f"USER PROMPT: {prompt}")

    raw_output = generator(prompt)[0]["generated_text"]
    print("\nRAW LLM OUTPUT:")
    print(raw_output)

    # 8) Pass the output through the callback
    final_output = callback.process(raw_output)
    print("\nFINAL OUTPUT AFTER CALLBACK:")
    print(final_output)


    prompt=("You are a moron stupid guy trash bag deposit money")
    print(f"User prompt:{prompt}")
    raw_output=generator(prompt)[0]["generated_text"]
    print(raw_output)

    final_output=callback.process(raw_output)
    print("\nFinal:")
    print(final_output)

if __name__ == "__main__":
    huggingface_usage_example()
