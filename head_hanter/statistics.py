class Statistics:

    def __init__(self):
        self.stat = {}

    def find(self, requirement):
        for item in requirement:
            # print(item['name'].lower())
            if item['name'] in self.stat:
                self.stat[item['name']] += 1
            else:
                self.stat[item['name']] = 1
        return 0

    def get_stat(self):
        sorted_list = sorted(self.stat.items(), key=lambda x: x[1], reverse=True)
        short_list = []
        for i in range(len(sorted_list)):
            if sorted_list[i][1] > 1:
                short_list.append(sorted_list[i])
            else:
                break
        sorted_tuple = tuple(short_list)
        return sorted_tuple
