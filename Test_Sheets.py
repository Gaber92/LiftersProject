import unittest
import Sheets

suite = unittest.TestLoader().loadTestsFromModule(Sheets)
unittest.TextTestRunner(verbosity=2).run(suite)

