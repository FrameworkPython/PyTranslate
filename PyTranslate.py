from deep_translator import GoogleTranslator
from googletrans import LANGUAGES
from functools import lru_cache

LANGUAGE_NAMES = {code: name.capitalize() for code, name in LANGUAGES.items()}

def display_languages():
    languages = list(LANGUAGE_NAMES.values())
    for idx, language in enumerate(languages, 1):
        print(f"{idx}. {language}")
    return languages

def get_language_choice(languages):
    while True:
        try:
            choice = int(input("Enter the number of the language you want to translate to: "))
            if 1 <= choice <= len(languages):
                return list(LANGUAGE_NAMES.keys())[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

@lru_cache(maxsize=10000)
def translate_text(text, lang_code):
    try:
        translator = GoogleTranslator(source='auto', target=lang_code)
        translated_lines = [translator.translate(line) for line in text.splitlines()]
        return '\n'.join(translated_lines)
    except Exception as e:
        return f"Error: {e}"

def main():
    while True:
        print("Enter the text you want to translate (type 'end' on a new line to finish):")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'end':
                break
            lines.append(line)
        text = '\n'.join(lines)

        if text.lower() == 'exit':
            print("Goodbye!")
            break

        languages = display_languages()
        lang_code = get_language_choice(languages)
        translation = translate_text(text, lang_code)

        print(f"\nTranslated text ({LANGUAGE_NAMES.get(lang_code, 'Unknown')}):\n{translation}\n")

main()
