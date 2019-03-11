# Merge Integer Ranges


class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return "[" + str(self.lower_bound) + "," + str(self.upper_bound) + "]"


def merge_ranges(input_range_list):
    res = []
    r = input_range_list[0]
    i = 1
    while i < len(input_range_list):
        try:
            if r.upper_bound >= input_range_list[i].upper_bound:
                i += 1
                continue
            if r.upper_bound >= input_range_list[i].lower_bound and r.upper_bound < input_range_list[i].upper_bound:
                r.upper_bound = input_range_list[i].upper_bound
                i += 1
                continue
            res.append(r.__str__())
            r = input_range_list[i]
            i += 1
        except IndexError:
            break
    res.append(r.__str__())
    return res


if __name__ == '__main__':
    a = [Range(1, 10), Range(5, 8), Range(8, 15)]
    r = merge_ranges(a)
    print(r)
    print(merge_ranges(a) == [Range(1, 15).__str__()])
    print("-" * 30)

    a = [Range(1, 4), Range(3, 7), Range(5, 10), Range(11, 15)]
    r = merge_ranges(a)
    print(r)
    print(merge_ranges(a) == [Range(1, 10).__str__(), Range(11, 15).__str__()])
    print("-" * 30)
