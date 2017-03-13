import unittest
import requests


class PigLatinTranslationTests(unittest.TestCase):
    url = 'http://localhost/translate'

    def test_words(self):
        words = ['pig', 'banana', 'trash', 'happy', 'duck', 'glove',
                      'eat', 'omelet', 'are']
        expected_output_words = ['igpay', 'ananabay', 'ashtray', 'appyhay', 'uckday',
                          'oveglay', 'eatyay', 'omeletyay', 'areyay']

        responses = [requests.post(self.url, word).text for word in words]
        self.assertEqual(responses, expected_output_words)

    def test_capitalized_words(self):
        words = ['Testing','Capitalized', 'Words']
        expected_output_words = ['Estingtay','Apitalizedcay', 'Ordsway']
        responses = [requests.post(self.url, word).text for word in words]
        self.assertEqual(responses, expected_output_words)

    def test_long__sentences(self):
        long_sentence = ('Testing Long sentance, with punctuation !!')
        expected_output = ('Estingtay Onglay entencessay, ithway unctuationpay !!')
        response = requests.post(self.url, long_sentence).text
        self.assertEqual(response, expected_output)

    def test_word_without_vovel(self):
        test_word = 'bdc'
        expected_result = 'bdcay'
        response = requests.post(self.url, test_word).text
        self.assertEqual(response, expected_result)

    def test_empty_string(self):
        self.assertEqual(requests.post(self.url, '').status_code, 400)







if __name__ == '__main__':
    unittest.main()