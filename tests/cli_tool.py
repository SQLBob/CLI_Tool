import unittest
#from ..cli_tool.cli_tool import __version__

class test_cli_tool(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    #def test_version():
    #   assert __version__ == '0.1.0'

if __name__ == '__main__':
    unittest.main()