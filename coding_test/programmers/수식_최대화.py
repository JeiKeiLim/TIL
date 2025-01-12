from tester import Tester

"""
참가자에게 주어진 연산 수식이 담긴 문자열 expression이 매개변수로 주어질 때, 우승 시 받을 수 있는 가장 큰 상금 금액을
return 하세요.

제한사항
- expression은 길이가 3 이상 100 이하인 문자열입니다.
- expression은 숫자와 3가지 연산자(+, -, *) 만으로 이루어져 있으며, 잘못된 수식은 주어지지 않습니다.
- 피연산자는 0 이상 999 이하의 숫자입니다.
- expression은 적어도 1개 이상의 연산자를 포함하고 있습니다.

입출력 예
expression               result
"100-200*300-500+20"     60420
"50*6-3*2"               300

+ - *
+ * -
- + *
- * +
* + -
* - +

20000, 20
+

-:
*:
+: 0

"""


def solution(expression: str) -> int:
    nums = []
    ops = []

    num_str = ""
    str_num_set = set([str(i) for i in range(10)])
    for expr in expression:
        if expr in str_num_set:
            num_str += expr
        else:
            nums.append(int(num_str))
            num_str = ""
            ops.append(expr)
    nums.append(int(num_str))

    ops_order = ["+-*", "+*-", "-+*", "-*+", "*+-", "*-+"]
    ops_idx = {}
    for i, op in enumerate(ops):
        ops_idx[op] = ops_idx.get(op, []) + [i]

    max_prize = 0
    for order in ops_order:
        ops_idx_ = {key: value.copy() for key, value in ops_idx.items()}
        ops_ = ops.copy()
        nums_ = nums.copy()

        for op in order:
            if op not in ops_idx_.keys():
                continue

            while len(ops_idx_[op]) > 0:
                idx = ops_idx_[op].pop(0)
                num1 = nums_.pop(idx)
                num2 = nums_.pop(idx)
                ops_.pop(idx)

                if op == "+":
                    right = num1 + num2
                elif op == "*":
                    right = num1 * num2
                else:
                    right = num1 - num2

                nums_.insert(idx, right)
                for key in ops_idx_.keys():
                    for i in range(len(ops_idx_[key])):
                        if idx < ops_idx_[key][i]:
                            ops_idx_[key][i] -= 1
        max_prize = max(max_prize, abs(nums_[0]))

    return max_prize


if __name__ == "__main__":
    tests = [
        ["100-200*300-500+20"],
        ["50*6-3*2"],
    ]
    answers = [
        60420,
        300,
    ]

    tester = Tester(solution)
    tester.test(tests, answers)
