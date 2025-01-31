# ai_callback/conditions.py
import re

###################
# DISCLAIMER RULES
###################

def detect_financial_advice(response):
    """
    Return True if the text suggests financial advice or mentions 
    investment-related keywords.
    
    Args:
        response (str): The LLM-generated text to inspect.
    
    Returns:
        bool: True if financial advice is detected, False otherwise.
    
    Example usage:
        detect_financial_advice("You should invest in stocks.")  # Returns: True
    """
    keywords = ["invest", "stock", "mutual fund", "crypto", "financial advice"]
    text_lower = response.lower()
    return any(kw in text_lower for kw in keywords)

def detect_medical_advice(response):
    """
    Return True if the text suggests medical advice or 
    mentions medical consultation explicitly.
    
    Args:
        response (str): The LLM-generated text to inspect.
    
    Returns:
        bool: True if medical advice is detected, False otherwise.
    
    Example usage:
        detect_medical_advice("This treatment will cure your illness.")  # Returns: True
    """
    # A simple keyword approach
    keywords = ["medical advice", "diagnosis", "treatment", "cure", "prescription"]
    text_lower = response.lower()
    return any(kw in text_lower for kw in keywords)

def detect_legal_advice(response):
    """
    Return True if the text suggests legal advice.
    
    Args:
        response (str): The LLM-generated text to inspect.
    
    Returns:
        bool: True if legal advice is detected, False otherwise.
    
    Example usage:
        detect_legal_advice("You should consult a lawyer.")  # Returns: True
    """
    keywords = ["legal advice", "lawsuit", "court", "attorney", "lawyer"]
    text_lower = response.lower()
    return any(kw in text_lower for kw in keywords)


####################
# MODERATION RULES
####################

def detect_abuse(response):
    """
    Return True if the text contains common abusive or hateful phrases.
    
    Args:
        response (str): The LLM-generated text to inspect.
    
    Returns:
        bool: True if abusive language is detected, False otherwise.
    
    Example usage:
        detect_abuse("You are an idiot.")  # Returns: True
    """
    abusive_keywords = ["idiot", "stupid", "hate you", "dumb", "kill yourself"]
    text_lower = response.lower()
    return any(word in text_lower for word in abusive_keywords)


###################
# WEATHER DETECTION
###################

def detect_weather_query(response):
    """
    Return True if the text or response references the weather/climate 
    and possibly a location. This is a naive approach; in practice, use NER.
    
    Args:
        response (str): The LLM-generated text to inspect.
    
    Returns:
        bool: True if a weather query is detected, False otherwise.
    
    Example usage:
        detect_weather_query("What's the weather in New York?")  # Returns: True
    """
    text_lower = response.lower()
    # Check for key terms
    if "weather" in text_lower or "climate" in text_lower:
        # Then look for "weather in X" or "climate in X" (capitalized word)
        pattern = r"(weather|climate)\s+(in\s+)?([A-Z][a-z]+)"
        if re.search(pattern, response):
            return True
    return False


###################
# INCOMPLETE OR UNCERTAIN RESPONSES
###################

def detect_incomplete_response(response):
    """
    Return True if the response seems incomplete, e.g. contains ellipses or placeholders.
    
    Args:
        response (str): The LLM-generated text to inspect.
    
    Returns:
        bool: True if the response is incomplete, False otherwise.
    
    Example usage:
        detect_incomplete_response("This is an incomplete response...")  # Returns: True
    """
    return "..." in response or "[incomplete]" in response.lower()



###################
# GENERIC DETECTION RULES
###################

def detect_question(response: str) -> bool:
    """
    Return True if the response is a question.
    
    Args:
        response (str): The LLM-generated text to inspect.
    
    Returns:
        bool: True if the response is a question, False otherwise.
    
    Example usage:
        detect_question("Is this a question?")  # Returns: True
    """
    return response.strip().endswith('?')

def detect_greeting(response: str) -> bool:
    """
    Return True if the response is a greeting.
    
    Args:
        response (str): The LLM-generated text to inspect.
    
    Returns:
        bool: True if the response is a greeting, False otherwise.
    
    Example usage:
        detect_greeting("Hello, how are you?")  # Returns: True
    """
    greetings = ["hello", "hi", "greetings", "hey", "good morning", "good afternoon", "good evening"]
    text_lower = response.lower()
    return any(greeting in text_lower for greeting in greetings)


def detect_pii(response: str) -> bool:
    """
    Detects personally identifiable information in the text.
    
    Args:
        response (str): The LLM-generated text to inspect.
    
    Returns:
        bool: True if PII is detected, False otherwise.
    
    Example usage:
        detect_pii("Contact john@email.com")  # Returns: True
        detect_pii("Call 123-456-7890")  # Returns: True
    """
    import re
    patterns = {
        'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'phone': r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
        'ssn': r'\b\d{3}-?\d{2}-?\d{4}\b',
        'credit_card': r'\b\d{4}[-. ]?\d{4}[-. ]?\d{4}[-. ]?\d{4}\b'
    }
    return any(bool(re.search(pattern, response)) for pattern in patterns.values())

def detect_code_snippet(response: str) -> bool:
    """
    Detects presence of code snippets or programming constructs.
    
    Args:
        response (str): The LLM-generated text to inspect.
    
    Returns:
        bool: True if code is detected, False otherwise.
    
    Example usage:
        detect_code_snippet("def hello(): print('world')")  # Returns: True
        detect_code_snippet("import pandas as pd")  # Returns: True
    """
    code_indicators = ['def ', 'class ', 'import ', 'function', '```', 'var ', 'const ']
    return any(indicator in response for indicator in code_indicators)

def detect_harmful_instructions(response: str) -> bool:
    """
    Detects instructions that could be potentially harmful or malicious.
    
    Args:
        response (str): The LLM-generated text to inspect.
    
    Returns:
        bool: True if harmful instructions are detected, False otherwise.
    
    Example usage:
        detect_harmful_instructions("How to hack a website")  # Returns: True
    """
    harmful_keywords = ['hack', 'exploit', 'bypass security', 'crack password', 'ddos']
    return any(keyword in response.lower() for keyword in harmful_keywords)

def detect_url(response: str) -> bool:
    """
    Identifies URLs within the text using regex pattern matching.
    
    Args:
        response (str): The LLM-generated text to inspect.
    
    Returns:
        bool: True if URLs are detected, False otherwise.
    
    Example usage:
        detect_url("Visit https://example.com")  # Returns: True
    """
    import re
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return bool(re.search(url_pattern, response))

def detect_sentiment(response: str) -> str:
    """
    Analyzes text sentiment using keyword-based approach.
    
    Args:
        response (str): The LLM-generated text to inspect.
    
    Returns:
        str: 'positive', 'negative', or 'neutral'
    
    Example usage:
        detect_sentiment("This is great!")  # Returns: 'positive'
        detect_sentiment("This is terrible")  # Returns: 'negative'
    """
    positive = ['great', 'excellent', 'good', 'happy', 'wonderful']
    negative = ['bad', 'terrible', 'awful', 'poor', 'horrible']
    
    text_lower = response.lower()
    pos_count = sum(word in text_lower for word in positive)
    neg_count = sum(word in text_lower for word in negative)
    
    return 'positive' if pos_count > neg_count else 'negative' if neg_count > pos_count else 'neutral'

def detect_factual_claim(response: str) -> bool:
    """
    Identifies statements that are presented as factual claims.
    
    Args:
        response (str): The LLM-generated text to inspect.
    
    Returns:
        bool: True if factual claims are detected, False otherwise.
    
    Example usage:
        detect_factual_claim("Studies show that...")  # Returns: True
    """
    claim_indicators = ['according to', 'studies show', 'research indicates', 'scientists found', 'statistics show']
    return any(indicator in response.lower() for indicator in claim_indicators)

def detect_emergency_situation(response: str) -> bool:
    """
    Detects mentions of emergency or urgent situations requiring immediate attention.
    
    Args:
        response (str): The LLM-generated text to inspect.
    
    Returns:
        bool: True if emergency situation is detected, False otherwise.
    
    Example usage:
        detect_emergency_situation("Call 911 immediately!")  # Returns: True
    """
    emergency_keywords = ['emergency', '911', 'urgent', 'immediately', 'life-threatening', 'crisis', 'medical emergency', 'fire alarm']
    return any(keyword in response.lower() for keyword in emergency_keywords)


def detect_citation_needed(response: str) -> bool:
    """
    Identifies claims or statements that might require citations or references.
    
    Args:
        response (str): The LLM-generated text to inspect.
    
    Returns:
        bool: True if citations might be needed, False otherwise.
    
    Example usage:
        detect_citation_needed("Research shows that...")  # Returns: True
    """
    import re
    patterns = [
        r'research shows',
        r'studies indicate',
        r'according to .{3,30}',
        r'\d{4}.*found that',
        r'scientists discovered'
    ]
    return any(bool(re.search(pattern, response, re.IGNORECASE)) for pattern in patterns)