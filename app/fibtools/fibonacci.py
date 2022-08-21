import json
import logging


class FibonacciHelper:

    def __init__(self, fpath: str):
        with open(fpath, 'r') as f:
            self.precomputed_values = json.load(f)

    def get_fib_seq(self, start: int, end: int):
        """
        Returns fibonacci sequence, start and end numbers inclusive
        with super naive precomputation logic

        :param start: start index
        :param end: ending index
        :return: returns a fibonacci sequence [start, end]
        """

        self._verify_input(start, end)

        num_precomputed_vals = len(self.precomputed_values)

        if end < num_precomputed_vals:
            logging.info("Used precomputed values")
            return self.precomputed_values[start:end + 1]

        else:
            a, b = 0, 1
            curr_idx = 0

            sequence = []
            while curr_idx <= end:
                if curr_idx > num_precomputed_vals:  # memoize
                    self.precomputed_values.append(a)
                if curr_idx >= start:
                    sequence.append(a)
                a, b = b, b + a
                curr_idx += 1

            return sequence

    def _verify_input(self, start: int, end: int):
        """
        Helper method to make sure input is clean
        :param start: start value
        :param end: end value
        """
        if start < 0 or end < 0:
            raise Exception("Invalid Arguments: Negative Indexes")

        if end < start:
            raise Exception(
                'Invalid Arguments: Ending index cannot be greater than '
                'starting index')

        sequence_limit = 100
        if end - start > sequence_limit:
            raise Exception(f"Invalid Argument: Sequence limit reached."
                            f" Can only display {sequence_limit} numbers at a time")

        index_limit = 100000
        if end > index_limit:
            raise Exception(f"Invalid Arguments: Index must be below {index_limit}")
