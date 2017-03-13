from flask import Flask, make_response, request

app = Flask(__name__)

def make_pig_latin_translation(words):
    """This function does the translation"""
    VOVELS =['a','e','i','o','u']

    #case: words containing punctuations
    if not words.isalpha():
        return words

    #case: Capitalized words
    if words[0].isUpper:
        return make_pig_latin_translation(words.lower()).capitalize()

    #case : Words starting with Vovels
    if words[0].lower() in VOVELS:
        return words+'yay'

    else:
        for i,char in enumerate(words):
            if char.lower() in VOVELS:
                return words[i:].lower()+words[:i].lower()+'ay'

    #words containing no vovel
    return words+'ay'

    return words

@app.route('/translate', methods=['POST'])
def pig_latin_translate():
    """Handles the translation of English to Pig-Latin"""
    data = request.stream.read().decode('utf-8')
    if not data:
        response = make_response("POST request for translation must contains at least one word.")
        request.status_code = 400 #Bad request
        return response
    translated_data = make_pig_latin_translation(data)
    response = make_response(translated_data)
    response.status_code = 200 #HTTP_OK
    return response


if __name__ == '__main__':
    app.run(port=80, debug=True)
