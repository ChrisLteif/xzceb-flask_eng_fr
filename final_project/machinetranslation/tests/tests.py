import unittest
from translator import englishToFrench
from translator import frenchToEnglish

class TestTranslation(unittest.TestCase):
    def test_englishToFrench(self):
        # Test that the translation function works as expected
        result = englishToFrench('Hello')
        self.assertEqual(result, 'Bonjour')

        with self.assertRaises(ValueError):
            result = englishToFrench(None)

    def test_frenchToEnglish(self):
        # Test that the translation function works as expected
        result = frenchToEnglish('Bonjour')
        self.assertEqual(result, 'Hello')

        with self.assertRaises(ValueError):
            result = frenchToEnglish(None)

if __name__ == '__main__':
    unittest.main()
