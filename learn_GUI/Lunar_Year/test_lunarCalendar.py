from unittest import TestCase
from lunarCalendar import can, chi

testCase = {2018: 'Mau Tuat',
            2019: 'Ky Hoi',
            1986: 'Binh Dan',
            1993: 'Quy Dau',
            1927: 'Dinh Mao'}


class TestLunarYear(TestCase):
    def test_year_in_testCase(self):
        for year in testCase.keys():
            self.assertEqual(testCase[year], can(year) + " " + chi(year))


if __name__ == '__main__':
    main()
