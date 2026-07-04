"""
CodeAlpha - Task 1: Language Translation Tool (Beginner Version)
------------------------------------------------------------------
A simple command-line program that translates text from one language
to another using the 'deep-translator' library.

Step by step, this program:
    1. Asks the user to type some text.
    2. Asks the user which language to translate FROM and TO.
    3. Sends the text to the Google Translate engine.
    4. Prints the translated text on the screen.

Before running, install the library:
    pip install deep-translator

Run it with:
    python translator_simple.py
"""

# Step 1: Import the tool we need for translation
from deep_translator import GoogleTranslator


def translate_text(text, source_language, target_language):
    """
    This function takes:
        text             -> the sentence we want to translate
        source_language  -> the language the text is currently in (e.g. "en")
        target_language  -> the language we want to translate it to (e.g. "fr")

    It returns the translated text.
    """
    translated = GoogleTranslator(source=source_language, target=target_language).translate(text)
    return translated


def main():
    print("===================================")
    print("   Simple Language Translator")
    print("===================================")
    print("(Language codes: en=English, fr=French, es=Spanish, hi=Hindi,")
    print(" de=German, it=Italian, zh-CN=Chinese, ja=Japanese, etc.)")
    print()

    # Step 2: Get input from the user
    text = input("Enter the text you want to translate: ")
    source_language = input("Enter the source language code (or 'auto' to detect): ")
    target_language = input("Enter the target language code: ")

    # Step 3: Call our function to do the translation
    result = translate_text(text, source_language, target_language)

    # Step 4: Show the result
    print()
    print("Original text   :", text)
    print("Translated text :", result)


# This makes sure main() only runs when we run this file directly
if __name__ == "__main__":
    main()
