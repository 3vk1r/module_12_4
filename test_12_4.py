import unittest
import new_runner_and_tournament as rat
import logging

logging.basicConfig(filename='runner.log', level=logging.INFO, filemode='w', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            first = rat.Runner('Igor', -2)
            for i in range (10):
                first.walk()
            self.assertEqual(first.distance, 50)
            logging.info('test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    def test_run(self):
        try:
            second = rat.Runner(122112)
            for i in range (10):
                second.run()
            self.assertEqual(second.distance, 100)
            logging.info('test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)




if __name__ == '__main__':
    unittest.main()