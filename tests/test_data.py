import unittest
import reports
from tablib import Dataset


class TestDataTools(unittest.TestCase):
    data = Dataset(*[('Matteo', 'Guadrini', 35), ('Arthur', 'Dent', 42), ('Ford', 'Prefect', 42)])
    data.headers = ['name', 'surname', 'age']

    def test_average(self):
        self.assertEqual(int(reports.average(self.data, 'age')), 39)

    def test_most_common(self):
        self.assertEqual(reports.most_common(self.data, 'age'), 42)

    def test_percentage(self):
        self.assertEqual(int(reports.percentage(self.data, 42)), 66)

    def test_counter(self):
        c = reports.counter(self.data, 2)
        self.assertEqual(list(c.keys()), [35, 42])
        self.assertEqual(c.most_common(1), [(42, 2)])


if __name__ == '__main__':
    unittest.main()