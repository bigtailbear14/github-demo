"""Behavioral tests for business-day arithmetic."""

from datetime import date
import unittest

from cloud_probe.business_days import add_business_days


class AddBusinessDaysTests(unittest.TestCase):
    def test_friday_to_monday(self):
        self.assertEqual(add_business_days(date(2026, 11, 6), 1), date(2026, 11, 9))

    def test_saturday_start(self):
        self.assertEqual(add_business_days(date(2026, 11, 7), 1), date(2026, 11, 9))

    def test_sunday_start(self):
        self.assertEqual(add_business_days(date(2026, 11, 8), 2), date(2026, 11, 10))

    def test_zero_preserves_weekday_and_weekend(self):
        for start in (date(2026, 11, 6), date(2026, 11, 7), date(2026, 11, 8)):
            with self.subTest(start=start):
                self.assertIs(add_business_days(start, 0), start)

    def test_crosses_year(self):
        self.assertEqual(add_business_days(date(2021, 12, 31), 1), date(2022, 1, 3))

    def test_negative_days_rejected(self):
        for days in (-1, -10):
            with self.subTest(days=days):
                with self.assertRaises(ValueError):
                    add_business_days(date(2026, 11, 7), days)

    def test_multiple_weeks(self):
        self.assertEqual(add_business_days(date(2026, 11, 2), 10), date(2026, 11, 16))

    def test_weekday_start_is_not_counted(self):
        self.assertEqual(add_business_days(date(2026, 11, 2), 1), date(2026, 11, 3))

    def test_leap_day(self):
        self.assertEqual(add_business_days(date(2024, 2, 28), 2), date(2024, 3, 1))


if __name__ == "__main__":
    unittest.main()
