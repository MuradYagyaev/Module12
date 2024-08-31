import unittest
import runner_test_v2
import runner_and_tournament_test_v2

runnerTS = unittest.TestSuite()
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_test_v2.RunnerTest))
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_and_tournament_test_v2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerTS)