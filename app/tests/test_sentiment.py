import unittest
from app.sentiment import sent_analysis

class TestSentimentAnalysis(unittest.TestCase):
    """
    Test cases for the sentiment analysis function.
    """
    def test_positve(self):
        """
        Test sentiment analysis for positive text.
        """
        text = "loving it"
        result = sent_analysis(text)
        self.assertEqual(result['classification'],'positive')
        self.assertGreater(result['polarity_score'], 0)

    def test_negative(self):
        """
        Test sentiment analysis for negative text.
        """
        text = "angry, hate this!"
        result = sent_analysis(text)
        self.assertEqual(result['classification'],'negative')
        self.assertLess(result['polarity_score'],0)

if __name__ == '__main__':
    unittest.main()
