import src.merge_sort as ms


class TestMyMergeSort:

    def test_merge(self):
        cases = [[5, 9, 45, 36], [-95, -65, 38, -1, 0]]
        assert ms.merge_sort(cases[0]) == [5, 9, 36, 45]
        assert ms.merge_sort(cases[1]) == [-95, -65, -1, 0, 38]
