import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)


def english_to_french(english_text):
    """
    Converts text from English to French
    """

    response = language_translator.translate(
        text = english_text,
        model_id='en-fr'
    ).get_result()

    french_text = response['translations'][0]['translation']

    return french_text

def french_to_english(french_text):
    """
    Converts text from French to English
    """

    response = language_translator.translate(
        text = french_text,
        model_id = 'fr-en'
    ).get_result()

    english_text = response['translations'][0]['translation']

    return english_text
