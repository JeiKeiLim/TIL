from tester import Tester  # Assuming you have a Tester class for running tests

"""
901. Online Stock Span
Medium

Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

### Example 1:
Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation:
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4
stockSpanner.next(85);  // return 6

### Constraints:
- 1 <= price <= 10^5
- At most 10^4 calls will be made to `next()`.
"""


class StockSpanner:

    def __init__(self):
        pass  # To be implemented

    def next(self, price: int) -> int:
        pass  # To be implemented


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


if __name__ == "__main__":
    # Test cases
    tests = [
        (
            ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"],
            [[], [100], [80], [60], [70], [60], [75], [85]],
        ),  # Example 1
    ]
    answers = [
        [None, 1, 1, 1, 2, 1, 4, 6],  # Expected output for Example 1
    ]

    tester = Tester(
        StockSpanner
    )  # Assuming Tester is available for testing class-based problems
    tester.test(tests, answers)
