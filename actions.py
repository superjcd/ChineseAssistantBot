from rasa_sdk.forms import FormAction
from rasa_sdk import Action
from typing import Text, List


class SubscribeForm(FormAction):
    def name(self) -> Text:
        return "subscribe_form"
    
    @staticmethod
    def required_slots(tracker) -> List[Text]:
        return ["email"]

    def submit(self, dispatcher, tracker, domain):
        email = tracker.get_slot("email")
        # 可以对email 进行检验入库等等， 这里省略
        dispatcher.utter_message(template="utter_confirm_email")
        return [] # 不要忘记返回[]


# class LocationForm(FormAction):
#     def name(self) -> Text:
#         return "get_location_form"
    
#     @staticmethod
#     def required_slots(tracker) -> List[Text]:
#         return ["location"]

#     def submit(self, dispatcher, tracker, domain):
#         email = tracker.get_slot("location")
#         # 可以对email 进行检验入库等等， 这里省略
#         dispatcher.utter_message(template="utter_confirm_location")
#         return [] # 不要忘记返回[]



class CallTaxi(Action):
    """叫车服务"""

    def name(self) -> Text:
        return "call_taxi_action"

    def run(self, dispatcher, tracker, domain):
        # 
        location = tracker.get_latest_entity_values("location")
        if location:
            # 这里可以实际调用打车api
            dispatcher.utter_message(template="utter_confirm_taxicall")
