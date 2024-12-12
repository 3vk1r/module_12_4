import unittest
import new_runner_and_tournament as rat
import logging
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            logging.info('test_walk" выполнен успешно')
            first = rat.Runner('Igor', -2)
            for i in range (10):
                first.walk()
            self.assertEqual(first.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner')


    def test_run(self):
        try:
            second = rat.Runner(122112)
            for i in range (10):
                second.run()
            self.assertEqual(second.distance, 100)
            logging.info('test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')



if __name__ == '__main__':
    logging.basicConfig(filename='py.log', level=logging.INFO, filemode='w', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    unittest.main()