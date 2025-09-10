from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import json
import os

def detect_language(text: str) -> str:
    """Simple language detection based on Unicode ranges"""
    hindi_chars = set("अआइईउऊएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक़ख़ग़ज़ड़ढ़फ़य़ृॄॅॆेैॉॊोौ्ँंःॐ।॥०१२३४५६७८९")
    
    # Count Hindi characters
    hindi_count = sum(1 for char in text if char in hindi_chars)
    
    # If more than 30% are Hindi characters, consider it Hindi
    if len(text) > 0 and (hindi_count / len(text)) > 0.3:
        return 'hi'
    return 'en'

class ActionProvidePreventiveTips(Action):
    def name(self) -> Text:
        return "action_provide_preventive_tips"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        disease = tracker.get_slot("disease")
        user_message = tracker.latest_message.get('text', '')
        
        # Load knowledge base
        try:
            knowledge_path = os.path.join('knowledge_base', 'healthcare_faq.json')
            with open(knowledge_path, 'r', encoding='utf-8') as f:
                faq_data = json.load(f)
        except Exception as e:
            print(f"Error loading knowledge base: {e}")
            dispatcher.utter_message(text="Sorry, I couldn't access the knowledge base.")
            return []
        
        # Detect language
        lang_detected = detect_language(user_message)
        
        if disease:
            disease_lower = disease.lower()
            # Handle variations
            if disease_lower in ['मलेरिया', 'malaria']:
                disease_key = 'malaria'
            elif disease_lower in ['डेंगू', 'dengue']:
                disease_key = 'dengue'
            elif disease_lower in ['टीबी', 'tuberculosis', 'tb']:
                disease_key = 'tuberculosis'
            elif disease_lower in ['डायबिटीज', 'diabetes']:
                disease_key = 'diabetes'
            else:
                disease_key = disease_lower
            
            if disease_key in faq_data["preventive_tips"]:
                tips_data = faq_data["preventive_tips"][disease_key]
                
                if lang_detected == 'hi':
                    message = tips_data.get("hindi", tips_data.get("english"))
                else:
                    message = tips_data.get("english", tips_data.get("hindi"))
                    
                dispatcher.utter_message(text=message)
            else:
                if lang_detected == 'hi':
                    dispatcher.utter_message(text="कृपया कोई विशिष्ट बीमारी का नाम बताएं। जैसे: मलेरिया, डेंगू, टीबी, डायबिटीज")
                else:
                    dispatcher.utter_message(text="Please specify a disease name. For example: malaria, dengue, tuberculosis, diabetes")
        else:
            if lang_detected == 'hi':
                dispatcher.utter_message(text="कृपया कोई विशिष्ट बीमारी का नाम बताएं। जैसे: मलेरिया, डेंगू, टीबी, डायबिटीज")
            else:
                dispatcher.utter_message(text="Please specify a disease name. For example: malaria, dengue, tuberculosis, diabetes")
        
        return [SlotSet("disease", disease)]

class ActionProvideSymptoms(Action):
    def name(self) -> Text:
        return "action_provide_symptoms_info"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        disease = tracker.get_slot("disease")
        user_message = tracker.latest_message.get('text', '')
        
        # Load knowledge base
        try:
            knowledge_path = os.path.join('knowledge_base', 'healthcare_faq.json')
            with open(knowledge_path, 'r', encoding='utf-8') as f:
                faq_data = json.load(f)
        except Exception as e:
            print(f"Error loading knowledge base: {e}")
            dispatcher.utter_message(text="Sorry, I couldn't access the knowledge base.")
            return []
        
        # Detect language
        lang_detected = detect_language(user_message)
        
        if disease:
            disease_lower = disease.lower()
            # Handle variations
            if disease_lower in ['मलेरिया', 'malaria']:
                disease_key = 'malaria'
            elif disease_lower in ['डेंगू', 'dengue']:
                disease_key = 'dengue'
            elif disease_lower in ['टीबी', 'tuberculosis', 'tb']:
                disease_key = 'tuberculosis'
            elif disease_lower in ['डायबिटीज', 'diabetes']:
                disease_key = 'diabetes'
            else:
                disease_key = disease_lower
            
            if disease_key in faq_data["symptoms"]:
                symptoms_data = faq_data["symptoms"][disease_key]
                
                if lang_detected == 'hi':
                    message = symptoms_data.get("hindi", symptoms_data.get("english"))
                else:
                    message = symptoms_data.get("english", symptoms_data.get("hindi"))
                    
                dispatcher.utter_message(text=message)
            else:
                if lang_detected == 'hi':
                    dispatcher.utter_message(text="कृपया कोई विशिष्ट बीमारी का नाम बताएं। जैसे: मलेरिया, डेंगू, टीबी, डायबिटीज")
                else:
                    dispatcher.utter_message(text="Please specify a disease name. For example: malaria, dengue, tuberculosis, diabetes")
        else:
            if lang_detected == 'hi':
                dispatcher.utter_message(text="कृपया कोई विशिष्ट बीमारी का नाम बताएं। जैसे: मलेरिया, डेंगू, टीबी, डायबिटीज")
            else:
                dispatcher.utter_message(text="Please specify a disease name. For example: malaria, dengue, tuberculosis, diabetes")
        
        return [SlotSet("disease", disease)]

class ActionProvideVaccinationSchedule(Action):
    def name(self) -> Text:
        return "action_provide_vaccination_schedule"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        vaccine = tracker.get_slot("vaccine")
        user_message = tracker.latest_message.get('text', '')
        
        # Load vaccination data
        try:
            vaccine_path = os.path.join('knowledge_base', 'vaccination_schedule.json')
            with open(vaccine_path, 'r', encoding='utf-8') as f:
                vaccine_data = json.load(f)
        except Exception as e:
            print(f"Error loading vaccination data: {e}")
            dispatcher.utter_message(text="Sorry, I couldn't access vaccination information.")
            return []
        
        # Detect language
        lang_detected = detect_language(user_message)
        
        if vaccine:
            vaccine_lower = vaccine.lower()
            # Handle variations
            if vaccine_lower in ['पोलियो', 'polio']:
                vaccine_key = 'polio'
            elif vaccine_lower in ['खसरा', 'measles']:
                vaccine_key = 'measles'
            elif vaccine_lower in ['हेपेटाइटिस', 'hepatitis']:
                vaccine_key = 'hepatitis'
            elif vaccine_lower in ['bcg']:
                vaccine_key = 'bcg'
            else:
                vaccine_key = vaccine_lower
            
            if vaccine_key in vaccine_data["vaccines"]:
                vac_info = vaccine_data["vaccines"][vaccine_key]
                
                if lang_detected == 'hi':
                    schedule_msg = vac_info["schedule"].get("hindi", vac_info["schedule"].get("english"))
                    importance_msg = vac_info["importance"].get("hindi", vac_info["importance"].get("english"))
                    message = f"{schedule_msg}\n\n{importance_msg}"
                else:
                    schedule_msg = vac_info["schedule"].get("english", vac_info["schedule"].get("hindi"))
                    importance_msg = vac_info["importance"].get("english", vac_info["importance"].get("hindi"))
                    message = f"{schedule_msg}\n\n{importance_msg}"
                    
                dispatcher.utter_message(text=message)
            else:
                if lang_detected == 'hi':
                    dispatcher.utter_message(text="कृपया कोई विशिष्ट टीके का नाम बताएं। जैसे: पोलियो, खसरा, हेपेटाइटिस, BCG")
                else:
                    dispatcher.utter_message(text="Please specify a vaccine name. For example: polio, measles, hepatitis, BCG")
        else:
            if lang_detected == 'hi':
                dispatcher.utter_message(text="कृपया कोई विशिष्ट टीके का नाम बताएं। जैसे: पोलियो, खसरा, हेपेटाइटिस, BCG")
            else:
                dispatcher.utter_message(text="Please specify a vaccine name. For example: polio, measles, hepatitis, BCG")
        
        return [SlotSet("vaccine", vaccine)]

class ActionCheckOutbreakAlert(Action):
    def name(self) -> Text:
        return "action_check_outbreak_alert"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        location = tracker.get_slot("location")
        user_message = tracker.latest_message.get('text', '')
        
        # Load outbreak data
        try:
            outbreak_path = os.path.join('knowledge_base', 'outbreak_alerts.json')
            with open(outbreak_path, 'r', encoding='utf-8') as f:
                outbreak_data = json.load(f)
        except Exception as e:
            print(f"Error loading outbreak data: {e}")
            dispatcher.utter_message(text="Sorry, I couldn't access outbreak information.")
            return []
        
        # Detect language
        lang_detected = detect_language(user_message)
        
        if location:
            location_variations = {
                'दिल्ली': 'Delhi',
                'delhi': 'Delhi',
                'मुंबई': 'Mumbai', 
                'mumbai': 'Mumbai',
                'लखनऊ': 'Lucknow',
                'lucknow': 'Lucknow'
            }
            
            location_key = location_variations.get(location.lower(), location)
            
            if location_key in outbreak_data["current_outbreaks"]:
                outbreak_info = outbreak_data["current_outbreaks"][location_key]
                
                if lang_detected == 'hi':
                    message = outbreak_info["message"].get("hindi", outbreak_info["message"].get("english"))
                else:
                    message = outbreak_info["message"].get("english", outbreak_info["message"].get("hindi"))
                    
                dispatcher.utter_message(text=message)
            else:
                # General advisory if no specific location outbreak
                general_advisory = outbreak_data["general_advisory"]
                
                if lang_detected == 'hi':
                    message = f"वर्तमान में {location} में कोई विशिष्ट प्रकोप की रिपोर्ट नहीं है।\n\n{general_advisory['hindi']}"
                else:
                    message = f"No specific outbreak reported in {location} currently.\n\n{general_advisory['english']}"
                    
                dispatcher.utter_message(text=message)
        else:
            # Show current outbreaks if no location specified
            if lang_detected == 'hi':
                message = "वर्तमान प्रकोप की स्थिति:\n\n"
                for loc, info in outbreak_data["current_outbreaks"].items():
                    message += f"📍 {loc}: {info['disease']}\n"
                message += f"\n{outbreak_data['general_advisory']['hindi']}"
            else:
                message = "Current outbreak status:\n\n"
                for loc, info in outbreak_data["current_outbreaks"].items():
                    message += f"📍 {loc}: {info['disease']}\n"
                message += f"\n{outbreak_data['general_advisory']['english']}"
                
            dispatcher.utter_message(text=message)
        
        return [SlotSet("location", location)]