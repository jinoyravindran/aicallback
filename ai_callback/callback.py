# ai_callback/callback.py

class AICallback:
    """
    A simple callback manager that processes an LLM response
    through a series of (condition, action) rules.

    Example usage:
        callback = AICallback()
        callback.add_rule(lambda response: "error" in response, lambda response: response.replace("error", "issue"))
        modified_response = callback.process("This is an error message.")
        print(modified_response)  # Output: This is an issue message.
    """

    def __init__(self):
        # Each element in `rules` is a tuple: (condition_fn, action_fn).
        self.rules = []

    def add_rule(self, condition_fn: callable, action_fn: callable) -> None:
        """
        Register a new condition–action rule.
        
        Args:
            condition_fn (callable): A function that takes a single string (the LLM response)
                                     and returns True/False indicating whether the action should fire.
            action_fn (callable): A function that takes a string (the LLM response) and 
                                  returns a (possibly modified) string.
        """
        self.rules.append((condition_fn, action_fn))

    def process(self, response: str) -> str:
        """
        Run the response through each condition–action pair in sequence.
        
        Args:
            response (str): The LLM-generated text to inspect and optionally modify.
        
        Returns:
            str: The final modified (or unmodified) LLM response.
        """
        for condition, action in self.rules:
            if condition(response):
                response = action(response)
        return response