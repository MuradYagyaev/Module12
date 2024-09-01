import rt_with_exceptions as rt
import unittest
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner1 = rt.Runner(12345, 10)
            for i in range(10):
                runner1.walk()
            self.assertEqual(runner1.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)
        except TypeError:
            logging.warning('Неверный тип данных для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner2 = rt.Runner('Бегун 2', -11)
            for i in range(10):
                runner2.run()
            self.assertEqual(runner2.distance, 220)
            logging.info('"test_run" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)
        except TypeError:
            logging.warning('Неверный тип данных для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        try:
            runner3 = rt.Runner('Бегун 3', 12)
            runner4 = rt.Runner('Бегун 4', 13)
            for i in range(10):
                runner3.walk()
                runner4.run()
            self.assertNotEqual(runner3.distance, runner4.distance)
            logging.info('"test_challenge" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)
        except TypeError:
            logging.warning('Неверный тип данных для Runner', exc_info=True)

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')

if __name__ == '__main__':
    unittest.main()
