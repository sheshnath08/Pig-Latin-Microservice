import unittest
import requests


class PigLatinTranslationTests(unittest.TestCase):
    url = 'http://0.0.0.0/translate'

    def test_words(self):
        """Should pass for the basic test cases provided"""
        words = ['pig', 'banana', 'trash', 'happy', 'duck', 'glove',
                      'eat', 'omelet', 'are']
        expected_output_words = ['igpay', 'ananabay', 'ashtray', 'appyhay', 'uckday',
                          'oveglay', 'eatyay', 'omeletyay', 'areyay']

        responses = [requests.post(self.url, x).text for x in words]
        self.assertEqual(responses, expected_output_words)

    def test_capitalization(self):
        """testing capitalized words and should preserve"""
        test_words = ['Testing','Capitalized', 'Words']
        expected_words = ['Estingtay','Apitalizedcay', 'Ordsway']
        responses = [requests.post(self.url, x).text for x in test_words]
        self.assertEqual(responses, expected_words)




if __name__ == '__main__':
    unittest.main()