import re

from flask import Flask, make_response, request

app = Flask(__name__)

def word_pig_latin_translation(word):
    """This function does the translation for word"""

    VOVELS =['a','e','i','o','u']

    #case: words containing punctuations
    if not word.isalpha():
        return word

    #case: Capitalized words
    if word[0].isupper():
        return word_pig_latin_translation(word.lower()).capitalize()

    #case : Words starting with Vovels
    if word[0].lower() in VOVELS:
        return word + 'yay'

    else:
        for i,char in enumerate(word):
            if char.lower() in VOVELS:
                return word[i:].lower() + word[:i].lower() + 'ay'

    #words containing no vovel
    return word + 'ay'

def pig_latin_translation(data):
    words = re.split('(\W)', data)
    return ''.join([word_pig_latin_translation(word) for word in words])

    return translated_sentance

@app.route('/translate', methods=['POST'])
def pig_latin_translate():
    """Handles the translation of English to Pig-Latin"""
    data = request.stream.read().decode('utf-8')
    if not data:
        response = make_response("POST request must contains at least one word.")
        response.status_code = 400 #Bad request
        return response
    translated_data = pig_latin_translation(data)
    response = make_response(translated_data)
    response.status_code = 200 #HTTP_OK
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
