# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

#
from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, EventType, Form, AllSlotsReset
from rasa_sdk import Action, Tracker
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
# from price import give_stockprice

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class StockPriceForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "stock_price_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["stock"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "stock": [
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        
        stock=tracker.get_slot('stock')
       # print("Latest message"+entities)
        stock_price = 1211.04
         
        api_key = 'RNZPXZ6Q9FEFMEHM'
        ts = TimeSeries(key=api_key, output_format='pandas')
        data, meta_data = ts.get_intraday(symbol=stock, interval = '1min', outputsize = '100')
        stock_price = data['4. close'][1]

        response = "Okay. The price of {} is  - ${}".format(stock, stock_price)
        
        dispatcher.utter_message(response)

        # return [SlotSet('stock',stock)]
        return [AllSlotsReset()]


# class ActionStockPrice(Action):
    
#     def name(self) -> Text:
#         return "action_stock_price"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         stock=tracker.get_slot('stock')
#        # print("Latest message"+entities)

#         if stock is None:
#             response = "Sure. Please provide the stock symbol so that I can fetch that information for you"
#         else:
#             response = "Okay. The price of <strong>{}</strong> is <strong>NAV - $1211.04</strong>".format(stock)
        
#         # try:
#         #     stock.upper()
#         #     price,market,company=give_stockprice(stock)
#         #     if price == "error":
#         #         response = "Stock - {} data not found from Yahoo Finance".format(stock)
#         #     else:
#         #         response='The stock price of '+company+' is '+price+' in '+market
#         # except:
#         #     response='Please enter the correct stock ID'
#         dispatcher.utter_message(response)

#         return [SlotSet('stock',stock)]


class InvestmentForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "investment_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["age", "married", "no_of_child", "yearly_earnings", "liabilities", "credit_score"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "age": [
                self.from_text(),
            ],
            "married": [
                self.from_text(),
            ],
            "no_of_child": [
                self.from_text(),
            ],
            "yearly_earnings": [
                self.from_text(),
            ],
            "liabilities": [
                self.from_text(),
            ],
            "credit_score": [
                self.from_text(),
            ],
        }

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_age(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate age value."""

        if self.is_int(value):
            return {"age": value}
        else:
            dispatcher.utter_message(template="utter_wrong_age")
            return {"age": None}

    def validate_married(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate married value."""

        if value.lower() in ['yes', 'no']:
            return {"married": value}
        else:
            dispatcher.utter_message(template="utter_wrong_married")
            return {"married": None}

    def validate_no_of_child(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate no_of_child value."""

        if self.is_int(value):
            return {"no_of_child": value}
        else:
            dispatcher.utter_message(template="utter_wrong_no_of_child")
            return {"no_of_child": None}

    def validate_yearly_earnings(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate yearly_earnings value."""

        # if self.is_int(value):
        #     return {"yearly_earnings": value}
        # else:
        #     dispatcher.utter_message(template="utter_wrong_yearly_earnings")
        #     return {"yearly_earnings": None}

        return {"yearly_earnings": value}

    def validate_liabilities(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate liabilities value."""

        # if self.is_int(value):
        #     return {"liabilities": value}
        # else:
        #     dispatcher.utter_message(template="utter_wrong_liabilities")
        #     return {"liabilities": None}
        return {"liabilities": value}

    def validate_credit_score(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate credit_score value."""

        if self.is_int(value):
            return {"credit_score": value}
        else:
            dispatcher.utter_message(template="utter_wrong_credit_score")
            return {"credit_score": None}


    def request_next_slot(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> Optional[List[EventType]]:
        """Request the next slot and utter template if needed,
            else return None"""
        for slot in self.required_slots(tracker):
            if self._should_request_slot(tracker, slot):

                ## For all other slots, continue as usual
                # logger.debug(f"Request next slot '{slot}'")
                dispatcher.utter_message(
                    template=f"utter_ask_{slot}", **tracker.slots
                )
                return [SlotSet("requested_slot", slot)]
        return None

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        # dispatcher.utter_message("All slots are takens. Thanks")
        # print(tracker.current_slot_values())
        all_slots = tracker.current_slot_values()
        
        age = all_slots['age']
        married = all_slots['married']
        no_of_child = all_slots['no_of_child']
        yearly_earnings = all_slots['yearly_earnings']
        liabilities = all_slots['liabilities']
        credit_score = all_slots['credit_score']

        if int(age)>=21 and int(age)<30:
          riskage = 10;
        if int(age)>=30 and int(age)<40:
          riskage = 7;
        if int(age)>=40 and int(age)<50:
          riskage = 4;
        if int(age)>=50 and int(age)<60:
          riskage = 1;

        if married == 'no':
          riskmarried = 10;
        if married == 'yes':
          riskmarried = 5;

        if int(no_of_child) == 0:
           riskchild = 10;
        if int(no_of_child) == 1:
           riskchild = 7;
        if int(no_of_child) == 2:
           riskchild = 4;
        if int(no_of_child) == 3:
           riskchild = 1;

        if int(yearly_earnings)>=3 and int(yearly_earnings)<10:
           riskearning = 3;
        if int(yearly_earnings)>=10 and int(yearly_earnings)<15:
           riskearning = 5;
        if int(yearly_earnings)>=15 and int(yearly_earnings)<25:
           riskearning = 7;
        if int(yearly_earnings)>=25 and int(yearly_earnings)<50:
           riskearning = 9;
        if int(yearly_earnings)>=50 and int(yearly_earnings)<100:
           riskearning = 10;
  
        if int(liabilities)>=3 and int(liabilities)<10:
           riskdebt = 10;
        if int(liabilities)>=10 and int(liabilities)<15:
           riskdebt = 9;
        if int(liabilities)>=15 and int(liabilities)<25:
           riskdebt = 7;
        if int(liabilities)>=25 and int(liabilities)<50:
           riskdebt = 5;
        if int(liabilities)>=50 and int(liabilities)<100:
           riskdebt = 3;


        if int(credit_score)>300 and int(credit_score)<630:
           riskcredit = 3;
        if int(credit_score)>=630 and int(credit_score)<690:
           riskcredit = 5;
        if int(credit_score)>=690 and int(credit_score)<720:
           riskcredit = 7;
        if int(credit_score)>=720 and int(credit_score)<850:
           riskcredit = 10;
        

        risk = riskage + riskmarried + riskchild + riskearning + riskdebt + riskcredit
        if int(risk) > 50:
          risk = "Gamestpop (GME)";
        elif int(risk) > 40 and int(risk) < 50:
          risk = "Futu Holdings (FUTU)";
        elif int(risk) > 30 and int(risk) < 40:
          risk = "Tesla (TSLA)";
        else:
          risk = "Apple (AAPL)";

        res = """Details Collected:
        1. Age - {}
        2. Married - {}
        3. No_of_children - {}
        4. Yearly_earnings - {}
        5. Liabilities - {}
        6. Credit_score - {}
        Suggested stock for you to invest in - {}
        """.format(age,married, no_of_child, yearly_earnings, liabilities, credit_score, risk)
        
        dispatcher.utter_message(text=res)
        # dispatcher.utter_template("utter_showResult", tracker)
        return [AllSlotsReset()]
