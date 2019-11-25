import unittest

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    unittest.TextTestRunner().run(suite)
