from tester import Tester

from typing import List

"""
You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw).

The bank has n accounts numbered from 1 to n. The initial balance of each account is stored in a 0-indexed integer array `balance`, 
with the (i + 1)th account having an initial balance of balance[i].

Execute all the valid transactions. A transaction is valid if:
- The given account number(s) are between 1 and n, and
- The amount of money withdrawn or transferred from is less than or equal to the balance of the account.

Implement the Bank class:

• Bank(long[] balance) 
    Initializes the object with the 0-indexed integer array balance.

• boolean transfer(int account1, int account2, long money)
    Transfers money dollars from the account numbered account1 to the account numbered account2. 
    Return true if the transaction was successful, false otherwise.

• boolean deposit(int account, long money)
    Deposit money dollars into the account numbered account. 
    Return true if the transaction was successful, false otherwise.

• boolean withdraw(int account, long money)
    Withdraw money dollars from the account numbered account. 
    Return true if the transaction was successful, false otherwise.

Example 1:

Input
["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
Output
[null, true, true, true, false, false]

Explanation
Bank bank = new Bank([10, 100, 20, 50, 30]);
bank.withdraw(3, 10);    // return true
bank.transfer(5, 1, 20); // return true
bank.deposit(5, 20);     // return true
bank.transfer(3, 4, 15); // return false
bank.withdraw(10, 50);   // return false

Constraints:
- n == balance.length
- 1 <= n, account, account1, account2 <= 10^5
- 0 <= balance[i], money <= 10^12
- At most 10^4 calls will be made to each function transfer, deposit, withdraw.
"""


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def _sanity_check(self, account: int) -> bool:
        if account < 1 or account > len(self.balance):
            return False
        return True

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._sanity_check(account1) or not self._sanity_check(account2):
            return False

        if money > self.balance[account1 - 1]:
            return False

        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._sanity_check(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._sanity_check(account):
            return False

        if money > self.balance[account - 1]:
            return False

        self.balance[account - 1] -= money
        return True


if __name__ == "__main__":
    # actions = ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
    inputs = [
        [
            ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"],
            [
                [[10, 100, 20, 50, 30]],
                [3, 10],
                [5, 1, 20],
                [5, 20],
                [3, 4, 15],
                [10, 50],
            ],
        ],
        [
            ["Bank","deposit","deposit","transfer","transfer","transfer","deposit","transfer","withdraw","deposit","withdraw","transfer","transfer"],
            [[[767,653,252,849,480,187,761,243,408,385,334,732,289,886,149,320,827,111,315,155,695,110,473,585,83,936,188,818,33,984,66,549,954,761,662,212,208,215,251,792,956,261,863,374,411,639,599,418,909,208,984,602,741,302,911,616,537,422,61,746,206,396,446,661,48,156,725,662,422,624,704,143,94,702,126,76,539,83,270,717,736,393,607,895,661]],
             [68,668],[25,978],[8,31,924],[2,6,857],[20,43,59],[71,307],[11,46,577],[37,377],[72,835],[82,574],[67,9,939],[24,49,251]]
        ]
    ]
    expected = [
        [None, True, True, True, False, False],
        [None,True,True,False,False,True,True,False,False,True,False,False,True]
    ]

    tester = Tester(Bank, verbose=1)
    tester.test(inputs, expected)
