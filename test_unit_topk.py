import pytest
from topk import topKFrequent

class TestTopKFrequent:
    
    def test_unique_elements(self):
        nums = [1, 2, 3, 4, 5]
        k = 2
        expected_output = [1, 2]
        assert set(topKFrequent(nums, k)) == set(expected_output)

    def test_repeated_elements(self):
        nums = [1, 1, 2, 2, 3, 3, 3]
        k = 2
        expected_output = [3, 2]
        assert set(topKFrequent(nums, k)) == set(expected_output)

    def test_same_frequency(self):
        nums = [1, 1, 1, 2, 2, 2]
        k = 1
        expected_output = [1]
        assert set(topKFrequent(nums, k)) == set(expected_output)

    def test_large_input_list(self):
        nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        k = 3
        expected_output = [1, 4, 3]
        assert set(topKFrequent(nums, k)) == set(expected_output)

    def test_empty_list(self):
        nums = []
        k = 2
        expected_output = []
        assert set(topKFrequent(nums, k)) == set(expected_output)

    def test_negative_numbers(self):
        nums = [-1, -2, -2, -3, -3, -3]
        k = 2
        expected_output = [-3, -2]
        assert set(topKFrequent(nums, k)) == set(expected_output)


    def test_all_same(self):
        nums = [1, 1, 1, 1, 1]
        k = 1
        expected_output = [1]
        assert set(topKFrequent(nums, k)) == set(expected_output)

# Run the tests
if __name__ == "__main__":
    pytest.main()
