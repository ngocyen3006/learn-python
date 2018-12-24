from unittest import TestCase
import unittest


def xep_loai_hoc_tap(diem_trung_binh):
    if diem_trung_binh >= 8.0:
        return "Giỏi"
    if diem_trung_binh >= 6.5:
        return "Khá"
    if diem_trung_binh >= 5.0:
        return "Trung Bình"
    return "Yếu"


class TestDiemTrungBinh(TestCase):
    def test_loai_yeu(self):
        self.assertEqual(xep_loai_hoc_tap(3.5), "Yếu")
        self.assertEqual(xep_loai_hoc_tap(4.5), "Yếu")
        self.assertEqual(xep_loai_hoc_tap(4.9), "Yếu")

    def test_loai_trung_binh(self):
        self.assertEqual(xep_loai_hoc_tap(5.0), "Trung Bình")
        self.assertEqual(xep_loai_hoc_tap(6.4), "Trung Bình")
        self.assertEqual(xep_loai_hoc_tap(6.0), "Trung Bình")

    def test_loai_kha(self):
        self.assertEqual(xep_loai_hoc_tap(6.5), "Khá")
        self.assertEqual(xep_loai_hoc_tap(7.0), "Khá")
        self.assertEqual(xep_loai_hoc_tap(7.9), "Khá")

    def test_loai_gioi(self):
        self.assertEqual(xep_loai_hoc_tap(8.0), "Giỏi")
        self.assertEqual(xep_loai_hoc_tap(8.4), "Giỏi")
        self.assertEqual(xep_loai_hoc_tap(8.9), "Giỏi")


if __name__ == '__main__':
    unittest.main()
