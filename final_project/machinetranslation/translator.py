"""This code is to authenticate language translator"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """Translating enlgish to french"""
    if english_text == None:
        french_text = ''
        return french_text
    translation = language_translator.translate(
    text=english_text,
    model_id= 'en-fr'
    ).get_result()
    resp = json.dumps(translation,skipkeys=True, sort_keys=True, indent=2, ensure_ascii=False)
    info =json.loads(resp)
    french_text=(info['translations'][0]['translation'])
    return french_text

def french_to_english(french_text):
    """Translating french to english"""
    if french_text == None:
        english_text = ''
        return english_text
    translation = language_translator.translate(
    text=french_text,
    model_id= 'fr-en'
    ).get_result()
    resp = json.dumps(translation,skipkeys=True, sort_keys=True, indent=2, ensure_ascii=False)
    info =json.loads(resp)
    english_text=(info['translations'][0]['translation'])
    return english_text
