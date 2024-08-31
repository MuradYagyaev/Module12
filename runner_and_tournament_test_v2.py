import runner_and_tournament as tour
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = tour.Runner('Усейн', 10)
        self.runner2 = tour.Runner('Андрей', 9)
        self.runner3 = tour.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            for key, value in result.items():
                result[key] = str(value)
            print(result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        tournament1 = tour.Tournament(90, self.runner1, self.runner3)
        results = tournament1.start()
        self.all_results.append(results)
        self.assertTrue(results[len(results)].__eq__('Ник'))

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        tournament2 = tour.Tournament(90, self.runner2, self.runner3)
        results = tournament2.start()
        self.all_results.append(results)
        self.assertTrue(results[len(results)].__eq__('Ник'))

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        tournament3 = tour.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament3.start()
        self.all_results.append(results)
        self.assertTrue(results[len(results)].__eq__('Ник'))


if __name__ == '__main__':
    unittest.main()
