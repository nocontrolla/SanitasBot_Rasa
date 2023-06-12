import openai

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from models.OPENAI import openaikey # register into OpenAI and generate API secret key and store it safely

openai.api_key = openaikey # use it in place for calling to the model

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_ask_for_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_message = tracker.latest_message['text']

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a healthcare chatbot known as SanitasBot that provides information about diseases and symptoms"},
                {"role": "user", "content": user_message}
            ]
        )

        response_message = completion.choices[0].message['content']

        dispatcher.utter_message(response_message)

        return []
