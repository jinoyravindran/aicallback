# ai_callback/time_tracking.py
import time

# Global variable to hold the start time
_START_TIME = None

def start_time_tracking():
    """
    Call this right before making the LLM request. 
    """
    global _START_TIME
    _START_TIME = time.time()

def always_true_condition(response):
    """A condition that always returns True, to ensure the time action runs."""
    return True

def append_time_taken(response):
    """
    Appends the total time since start_time_tracking() was called.
    If _START_TIME is None, it simply returns the original response.
    """
    global _START_TIME
    if _START_TIME is None:
        return response

    elapsed = time.time() - _START_TIME
    return response + f"\n\n[Time Taken: {elapsed:.2f} seconds]"
