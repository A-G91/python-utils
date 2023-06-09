import arrays
import random


def test_get_weights_no_remainder():
    assert arrays.get_weights(1000000, 100000) == [.1] * 10


def test_get_weights_with_remainder():
    # TODO: revisit this case to see if we can always have equal weights
    assert arrays.get_weights(1000000, 70000) == [
        0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.02]


def test_get_weights_with_remainder_01():
    assert arrays.get_weights(3, 1) == [0.25] * 4


def test_get_weights_no_remainder_02():
    assert arrays.get_weights(100, 21) == [0.2] * 5


def test_get_weights_when_partition_size_is_large_than_dataframe():
    assert arrays.get_weights(10000, 100000) == [1]


def test_weights_sum_to_one():

    num_tests = 1000

    for _ in range(num_tests):
        dataframe_size = random.randint(1000, 1000000)
        partition_size = random.randint(1000, dataframe_size - 1)

        weights = arrays.get_weights(dataframe_size, partition_size)
        assert round(sum(weights), 2) == 1
