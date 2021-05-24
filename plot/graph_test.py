import unittest
from datetime import datetime
from read_text import sort_by_date, sort_by_resource

class TestDataplot(unittest.TestCase):
    def test_sort_by_date(self):
        data = ['date, resource, count, staff_id\n', '2020-11,136,55,Rodion\n']
        result = sort_by_date(data)
        expect = [{'date': datetime.strptime("2020-11", '%Y-%m').date(), 'resource': 136, 'count': 55, 'staff_id': 'Rodion'}]
        self.assertEqual(expect, result)

    def sort_by_resource(self):
        sorted_info = [{'date': datetime.date(2020, 5, 1), 'resource': 118, 'count': 56, 'staff_id': 'Nikita'}, {'date': datetime.date(2020, 5, 1), 'resource': 122, 'count': 98, 'staff_id': 'Svyatoslav'}, {'date': datetime.date(2021, 1, 1), 'resource': 118, 'count': 29, 'staff_id': 'Alia'}]
        result = sort_by_date(sorted_info)
        expect = [[{'date': datetime.date(2020, 5, 1), 'resource': 122, 'count': 98, 'staff_id': 'Svyatoslav'}], [{'date': datetime.date(2020, 5, 1), 'resource': 118, 'count': 56, 'staff_id': 'Nikita'}, {'date': datetime.date(2021, 1, 1), 'resource': 118, 'count': 29, 'staff_id': 'Alia'}]]
        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()


