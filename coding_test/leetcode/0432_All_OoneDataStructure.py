import numpy as np

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = dict()
        
        self.max_key = []
        self.min_key = []

    def update_minmax_key(self, key):
        if key not in self.data.keys():
            if key in self.min_key:
                self.min_key.remove(key)
            if key in self.max_key:
                self.max_key.remove(key)
            return
        
        if len(self.max_key) < 1 or self.data[key] >= self.data[self.max_key[-1]]:

            if key in self.max_key:
                self.max_key.remove(key)
            
            if key in self.min_key:
                self.min_key.remove(key)

            self.max_key.append(key)
            self.min_key.insert(0, key)
                
        if len(self.min_key) < 1 or self.data[key] < self.data[self.min_key[-1]]:
            
            if key in self.min_key:
                self.min_key.remove(key)

            if key in self.max_key:
                self.max_key.remove(key)

            self.min_key.append(key)
            self.max_key.insert(0, key)

        if len(self.min_key) > 1 and self.data[self.min_key[-1]] > self.data[self.min_key[-2]]:
            self.min_key[-1], self.min_key[-2] = self.min_key[-2], self.min_key[1]
        if len(self.max_key) > 1 and self.data[self.max_key[-1]] < self.data[self.max_key[-2]]:
            self.max_key[-1], self.max_key[-2] = self.max_key[-2], self.max_key[1]

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.data.keys():
            self.data[key] += 1
            self.update_minmax_key(key)
        else:
            self.data[key] = 1
            self.min_key.append(key)
            self.max_key.insert(0, key)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.data.keys():
            if self.data[key] == 1:
                del self.data[key]
            else:
                self.data[key] -= 1
        else:
            return
        
        self.update_minmax_key(key)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.max_key:
            return self.max_key[-1]
        else:
            return ""
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.max_key:
            return self.min_key[-1]
        else:
            return ""

# test_fs = ["AllOne","inc","inc","inc","inc","inc","inc","dec", "dec","getMinKey","dec","getMaxKey","getMinKey"]
# test_args = [[], ["a"],["b"],["b"],["c"],["c"],["c"],["b"],["b"],[],["a"],[],[]]
# answers = [None, None,None,None,None,None,None,None,None,"a",None,"c","c"]

# test_fs = ["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]
# test_args = [[],["hello"],["hello"],[],[],["leet"],[],[]]
# answers = [None,None,None,"hello","hello",None,"hello","leet"]

test_fs = ["AllOne","inc","inc","inc","inc","inc","inc","inc","inc","inc","inc","inc","inc","getMinKey"]
test_args = [[],["a"],["b"],["c"],["d"],["a"],["b"],["c"],["d"],["c"],["d"],["d"],["a"],[]]
answers = [None,None,None,None,None,None,None,None,None,None,None,None,None,"b"]

###  Generate test set START
# cmd_list = ["inc", "inc", "inc", "inc", "inc", "inc", "inc", "inc", "dec", "dec",
#             "getMinKey", "getMaxKey"]

# cmds = np.random.randint(len(cmd_list), size=1000)
# test_fs = ["AllOne"]
# test_args = [[]]

# for cmd in cmds:
#     arg = []
#     if cmd_list[cmd] == "inc" or cmd_list[cmd] == "dec":
#         arg = ["key%02d" % (np.random.randint(10))]
    
#     test_fs.append(cmd_list[cmd])
#     test_args.append(arg)

# print("[%s]" % ",".join(["\"%s\"" % t for t in test_fs]))
# print(("[%s]" % (",".join(["%s" % arg for arg in test_args])).replace("'", "\"")))
# # exit()
###  Generate test set END

obj = None

predicts = []
for i, test in enumerate(test_fs):
    result = None

    print(i, ":", test, test_args[i], ":: ", end="")

    if test == "AllOne":
        obj = AllOne()
    if test == "inc":
        result = obj.inc(test_args[i][0])
    elif test == "dec":
        result = obj.dec(test_args[i][0])
    elif test == "getMinKey":
        result = obj.getMinKey()
    elif test == "getMaxKey":
        result = obj.getMaxKey()

    predicts.append(result)

    print(result)
    print([[key, obj.data[key]] for key in obj.min_key], "//", [[key, obj.data[key]] for key in obj.max_key])
    print("")

print(predicts)
print(answers)

print(predicts == answers)
