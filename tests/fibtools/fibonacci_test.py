import pytest
import os

from app.fibtools import fibonacci


def setup_module(module):
    dir_path = os.path.dirname(__file__)
    fpath = os.path.join(dir_path, '../../app/fibtools/precomputed_numbers.json')

    global fib_helper
    fib_helper = fibonacci.FibonacciHelper(fpath)


def test_get_fib_seq_singleton():
    sequence = fib_helper.get_fib_seq(0, 0)
    assert len(sequence) == 1
    assert sequence == [1]


def test_get_fib_seq_sequence():
    sequence = fib_helper.get_fib_seq(0, 5)
    assert len(sequence) == 6
    assert sequence == [1, 1, 2, 3, 5, 8]


def test_get_fib_seq_bad_input_greater():
    with pytest.raises(Exception) as e_info:
        sequence = fib_helper.get_fib_seq(10, 5)
    assert "Ending index cannot be greater than starting index" in str(e_info.value)


def test_get_fib_seq_bad_input_negative():
    with pytest.raises(Exception) as e_info:
        sequence = fib_helper.get_fib_seq(-1, 5)
    assert "Negative Indexes" in str(e_info.value)


def test_get_fib_seq_bad_input_sequence_limit():
    with pytest.raises(Exception) as e_info:
        sequence = fib_helper.get_fib_seq(0, 5000)
    assert "Sequence limit reached" in str(e_info.value)


def test_get_fib_seq_bad_input_index_limit():
    with pytest.raises(Exception) as e_info:
        sequence = fib_helper.get_fib_seq(1000000000-1, 1000000000)
    assert "Index must be below" in str(e_info.value)
