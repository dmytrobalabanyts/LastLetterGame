import unittest 
import Utils

class Utils_test (unittest.TestCase):
    def test_format_notification(self):
        self.assertEqual(Utils.format_notification('com', 'dat'), '{"command": "com", "data": "dat"}')

if __name__ == '__main__':
    unittest.main()