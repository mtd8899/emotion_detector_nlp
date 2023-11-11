import unittest
from EmotionDetection.emotion_detection import emotion_detector  

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection(self):
        text1 = "I am glad this happened"
        result1 = emotion_detector(text1)
        self.assertEqual(result1['dominant_emotion'], 'joy')

        text2 = "I am really mad about this"
        result2 = emotion_detector(text2)
        self.assertEqual(result2['dominant_emotion'], 'anger')

        text3 = "I feel disgusted just hearing about this"
        result3 = emotion_detector(text3)
        self.assertEqual(result3['dominant_emotion'], 'disgust')

        text4 = "I am so sad about this"
        result4 = emotion_detector(text4)
        self.assertEqual(result4['dominant_emotion'], 'sadness')

        text5 = "I am really afraid that this will happen"
        result5 = emotion_detector(text5)
        self.assertEqual(result5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
