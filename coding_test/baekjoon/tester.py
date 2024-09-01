import time


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
        for i, test in enumerate(tests):
            s_time = time.time()

            predict[i] = self.test_func(*test)

            print("Case #%d" % (i + 1), end="")
            if self.verbose > 0 or len(test[0]) < 10:
                print(" ::%s" % (test))
            else:
                print("")

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

            p_time = time.time() - s_time
            if p_time < 0.001:
                print(
                    "Took %.3f micro seconds" % ((time.time() - s_time) * 1000 * 1000)
                )
            elif p_time < 1:
                print("Took %.3f milli seconds" % ((time.time() - s_time) * 1000))
            else:
                print("Took %.3fseconds" % (time.time() - s_time))
            print("")
