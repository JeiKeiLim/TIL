def find_dot(seq):
    for i, s in enumerate(seq):
        if s == '.':
            return i
    return -1

class Solution:
    def subdomainVisits(self, cpdomains):
        visit_cnt = dict()
        
        for cpdom in cpdomains:
            sub_cp = cpdom.split(" ")
            cnt = int(sub_cp[0])
            
            domain = sub_cp[1]
            
            # idx = domain.find(".")
            idx = find_dot(domain)
            while idx > -1:
                if domain in visit_cnt.keys():
                    visit_cnt[domain] += cnt
                else:
                    visit_cnt[domain] = cnt

                # idx = domain.find(".")
                idx = find_dot(domain)
                domain = domain[idx+1:]

        return ["%d %s" % (visit_cnt[key], key) for key in visit_cnt.keys()]


tests = [["9001 discuss.leetcode.com"],
        ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]]
answers = [["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"],
            ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]]

tester = Solution()

predicts = [[]] * len(tests)
for i, test in enumerate(tests):
    predicts[i] = tester.subdomainVisits(test)
    
for predict, answer in zip(predicts, answers):
    print(predict)
    print(answer)
    
    if predict == answer:
        print(True)
    else:
        for p in predict:
            if p in answer:
                answer.remove(p)

        print(len(answer) == 0)
