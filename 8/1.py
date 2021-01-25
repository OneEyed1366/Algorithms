from collections import Counter, deque

class Encode_by_Haffman():
    def __init__(self, to_convert, code_table=dict()):
        self.to_convert = to_convert
        self.count = Counter(to_convert)
        self.sorted_elems = deque(sorted(self.count.items(), key = lambda item: item[1]))
        self.code_table = code_table

        if len(self.sorted_elems) != 1:
            while len(self.sorted_elems) > 1:
                weights = self.sorted_elems[0][1] + self.sorted_elems[1][1]
                combinations = {
                    0: self.sorted_elems.popleft()[0],
                    1: self.sorted_elems.popleft()[0]
                }

                for i, __count in enumerate(self.sorted_elems):
                    if weights > __count[1]:
                        continue
                    else:
                        self.sorted_elems.insert(i, (combinations, weights))

                        break
                else:
                    self.sorted_elems.append((combinations, weights))
            
        else:
            weights = self.sorted_elems[0][1]
            combinations = {0: self.sorted_elems.popleft()[0], 1: None}
            self.sorted_elems.append((combinations, weights))


    def __str__(self):
        self.haffman_encode(self.sorted_elems[0][0])
        
        return " ".join([self.code_table[i] for i in self.to_convert])

    def haffman_encode(self, value, path=''):
        if not isinstance(value, dict):
            self.code_table[value] = path
        else:
            self.haffman_encode(value[0], path=f'{path}0')
            self.haffman_encode(value[1], path=f'{path}1')

print(Encode_by_Haffman("beep boop beer!"))