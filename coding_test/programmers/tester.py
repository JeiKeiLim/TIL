import time
import random

from typing import List
from copy import deepcopy


def generate_random_char(start: str = "a", end: str = "z") -> str:
    return chr(random.randint(ord(start), ord(end)))


def generate_random_string(
    min_n: int, max_n: int = -1, start_char: str = "a", end_char: str = "z"
) -> str:
    if max_n < min_n:
        max_n = min_n
    n = random.randint(min_n, max_n)
    return "".join([generate_random_char(start_char, end_char) for _ in range(n)])


def generate_random_int_array(
    min_n: int, max_n: int = -1, start_n: int = 0, end_n: int = 1000
) -> List[int]:
    if max_n < min_n:
        max_n = min_n
    n = random.randint(min_n, max_n)

    return [random.randint(start_n, end_n) for _ in range(n)]


class Tester:
    def __init__(self, test_func, exact_match=False, verbose=1):
        self.test_func = test_func
        self.verbose = verbose
        self.exact_match = exact_match

    def is_correct(self, predict, answer):
        if answer is None:
            return False

        if type(predict) == list:
            # if len(predict) != len(answer):
            # 	return False

            is_correct = True
            if self.exact_match:
                is_correct = predict == answer
                incorrect_list = [p for i, p in enumerate(predict) if p != answer[i]]
                answer = [a for i, a in enumerate(answer) if a != predict[i]]
            else:
                incorrect_list = []
                for p in predict:
                    if p in answer:
                        answer.remove(p)
                    else:
                        incorrect_list.append(p)
                        is_correct = False

            if self.verbose > 0 and (incorrect_list or answer):
                print("--- Wrong case")
                print("------ Predict : %s" % incorrect_list)
                print("------ Answer : %s" % answer)

            return is_correct and len(answer) == 0
        else:
            return predict == answer

    def test(self, tests, answers, exact_match=False):

        predict = [[]] * len(tests)
        for i, test_vals in enumerate(tests):
            test_args = deepcopy(test_vals)
            s_time = time.time()

            predict[i] = self.test_func(*test_args)

            e_time = time.time()
            run_time = e_time - s_time

            print("Case #%d" % (i + 1))
            for j in range(len(test_vals)):
                n_vals = 1
                try:
                    n_vals = len(test_vals[j])
                except Exception:
                    pass
                print("    Arg #%d - " % (j+1), end="")
                if self.verbose > 0 or n_vals < 20:
                    print("%s" % (test_vals[j]))
                else:
                    print("Too long, skip printing")

            if self.verbose > 0 or type(predict[i]) != list or len(predict[i]) < 10:
                print("--- Result :", predict[i])

            if answers:
                if (
                    self.verbose > 0
                    or type(answers[i]) != list
                    or (answers[i] and len(answers[i]) < 10)
                ):
                    print("--- Answer :", answers[i])

                print("--- Is correct ?", self.is_correct(predict[i], answers[i]))

            if run_time < 0.001:
                print(
                    "Took %.3f micro seconds" % (run_time * 1000 * 1000)
                )
            elif run_time < 1:
                print("Took %.3f milli seconds" % (run_time * 1000))
            else:
                print("Took %.3fseconds" % run_time)
            print("")
