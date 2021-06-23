class Queue:
    def __init__(self):
        self.__value = []
        self.__pt = 0
        
    def q_add(self, element):
        self.__value.append(element)

    def q_remove(self):
        if not self.is_empty():
            tmp = self.__value[self.__pt]
            self.__pt += 1
            if self.__pt > len(self.__value) / 2:
                self.__value = self.__value[self.__pt:]
                self.__pt = 0
            return tmp
        else:
            return -1

    def q_rem_by_index(self, arg):
        return self.__value.pop(self.__pt + arg)

    def get_value(self):
        return self.__value[self.__pt:]

    def is_empty(self):
        return not self.__value

    def __str__(self):
        return str(self.__value[self.__pt:])

    def __getitem__(self, item):
        return self.__value[item]

    def __len__(self):
        return len(self.__value)
