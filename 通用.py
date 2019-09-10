# 笔试题通用模板
# 陕西科技大学 陶亚凡
import time


def cases_for_test():
    cases = '''
        5
        33956 27538
        79731 91415
        25288 33956
        33956 84925
        79731 25288
        
        1
        5 6
        '''.split('\n')

    cases = list(map(lambda x: x.strip(), cases))
    cases = [case for case in cases if case]
    return cases


class GetData:
    def __init__(self, use_test_case=True):
        self._use_test_case = use_test_case
        if self._use_test_case:
            self._test_case = cases_for_test()
            self._least = len(self._test_case)

    def _get_one_row(self):
        if self._use_test_case:
            self._least -= 1
            return self._test_case[-self._least - 1]
        else:
            return input()

    # 注意返回的一定是一个 list，若只有一个数据记得 get_rows()[0]
    def get_rows(self, rows=1, data_type=int, split=' ', is_2dim=False):
        assert rows == 1 or (rows > 1 and is_2dim is True), "If rows>1, is_2dim must be True. Or rows can be 1"

        data = []
        for i in range(rows):
            row_data = self._get_one_row().strip()
            row_data = row_data.split(split) if split else [row_data]
            new_data = list(map(data_type, row_data))
            data.append(new_data)

        return data if is_2dim else data[0]

    @property
    def least(self):
        if self._use_test_case:
            return self._least
        else:
            return 0


class Logging:
    def __init__(self, enable=True):
        self._enable = enable

    def debug(self, name, var=None):
        if self._enable:
            if var:
                for n, v in zip(name, var):
                    print(n + ': {}'.format(v), end=' ')
                print()
            else:
                print(name)


class Solution:
    def __init__(self, logger=Logging(False)):
        self._logger = logger

    def sol(self, data):
        return data


def main():
    data = GetData(use_test_case=True)
    logger = Logging(True)
    while True:
        logger.debug('-' * 50)
        start_time = time.time()
        sol = Solution(logger)
        nums = data.get_rows()[0]
        all_data = data.get_rows(nums, is_2dim=True)

        print(sol.sol(all_data))
        logger.debug(['Consumed time'], [time.time() - start_time])

        if data.least == 0:
            break


if __name__ == '__main__':
    main()
