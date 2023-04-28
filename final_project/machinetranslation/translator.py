'''Translator code'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

api_key = '3AXZVvYcBZcj7lPpfgZ0jDjNMwl59ag9lKeEItcE1Cf-'
url = 'https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/7ca7136d-9495-4fa9-bcd3-af9abc28f31b'



# Set up the authenticator
authenticator = IAMAuthenticator(api_key)
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

# Set up the service URL
translator.set_service_url(url)


def englishToFrench(english_text):
    '' 'Set the source and target languages'''
    source_language = 'en'
    target_language = 'fr'
    # Call the translate() method to translate the text
    frenchText = translator.translate(
        text=english_text,
        source=source_language,
        target=target_language
    ).get_result()

    # Extract and return the translated text
    return frenchText['translations'][0]['translation']


def frenchToEnglish(french_text):
    ''' Set the source and target languages'''
    source_language = 'fr'
    target_language = 'en'

    # Call the translate() method to translate the text
    englishText = translator.translate(
        text=french_text,
        source=source_language,
        target=target_language
    ).get_result()

    # Extract and return the translated text
    return englishText['translations'][0]['translation']
