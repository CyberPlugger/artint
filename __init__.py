import requests, os
from artint import libhelp

BASIC_PROMPT = f"You are an ai made in a python library called artint. This library was made for easier AI access. It has: a function yesorno made for getting True or False to your question that\'s answered by AI, a function called translate to translate a text into a specific language, and a class AI for custom AIs. This library is located in {os.path.dirname(__file__)}. You were made by the company CPDP with Andrew Cherepennikov Sergeyvich as the leader (aka CyberPlugger)."
exc = libhelp.exc

class AI:
    """
    AI Assistant Class for easier AI Access and creation.
    Maintains conversation history and returns responses as strings.
    """
    def __init__(self, system_prompt=BASIC_PROMPT, model="openai"):
        self.url = "https://text.pollinations.ai/"
        self.system_prompt = system_prompt
        self.model = model
        self.history = [
            {"role": "system", "content": self.system_prompt}
        ]

    def ask(self, user_query):
        """
        Sends query to the AI, stores it in history, and returns the response.
        """
        self.history.append({"role": "user", "content": user_query})
        
        payload = {
            "messages": self.history,
            "model": self.model,
            "cache": False
        }

        try:
            response = requests.post(self.url, json=payload, timeout=989898989898989)
            
            if response.status_code == 200:
                ai_reply = response.text
                self.history.append({"role": "assistant", "content": ai_reply})
                return ai_reply
            else:
                return f"Server is busy. returned status {response.status_code}"
        
        except Exception as e:
            return f"System Error: {str(e)}"

    def clear_history(self):
        """Resets the conversation history to the initial system prompt."""
        self.history = [{"role": "system", "content": self.system_prompt}]
        return True

def yesorno(question):
    """
    The user asks a yes or no question, then he gets True as yes or False as no.
    The question is answered by AI.
    :param question:
    :return:
    """
    global exc
    x = AI()
    response = x.ask(f'{question + '?' if not question.endswith('?') else ''} Only answer yes or no. If the question is not for yes or no, answer it normally.')
    return response.lower().startswith('yes')

def translate(string, language):
    """The user asks a string to translate into a specific language.
    :param string:
    :param language:
    :return: """
    x = AI()
    response = x.ask(f'translate "{string}" to {language} language. Only answer the translation.')
    return str(response)

__all__ = ('AI',
'yesorno',
'translate',
'exc'
)
