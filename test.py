# -*- coding: utf-8 -*-
import cyrillictools
import unittest

class TestMyFunctions(unittest.TestCase):
    knownLowToUp = (
        (u'ПРИВЕТ мир!!!', u'ПРИВЕТ МИР!!!'),
        (u'абвгд', u'АБВГД'),
        )
    knownUpToLow = (
        (u'ПРИВЕТ мир!!!', u'привет мир!!!'),
        (u'АБВГД', u'абвгд'),
        )
    knownCapitalize = (
        (u'ПРИВЕТ мир!!!', u'Привет Мир!!!'),
        (u'АБВГД', u'Абвгд'),
        )
        

    def testLowString(self):
        for a, b in self.knownUpToLow:
            result = cyrillictools.low_string(a)
            self.assertEqual(b, result)
            
    def testUpString(self):
        for a, b in self.knownLowToUp:
            result = cyrillictools.up_string(a)
            self.assertEqual(b, result)

    def testCapitalize(self):
        for a, b in self.knownCapitalize:
            result = cyrillictools.capitalize(a)
            self.assertEqual(b, result)
            
if __name__ == '__main__':
    unittest.main()
    
#print cyrillictools.low_string(u'ПРИВЕТ мир!!!')
#print cyrillictools.up_string(u'ПРИВЕТ мир!!!')

