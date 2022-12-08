""" sadlfkjasf """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

auth = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=auth
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)


def english_2_french(english_text):
    """ fasd """
    if english_text is None or english_text == "":
        return None
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return translation['translations'][0]['translation']


def french_2_english(french_text):
    """ lkjjl """
    if french_text is None or french_text =="":
        return None
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return translation['translations'][0]['translation']
