# 笔试题通用模板
# 陕西科技大学 陶亚凡


def _test_case_init():
    cases = '''
        This is test cases
        '''.split('\n')

    cases = list(map(lambda x: x.strip(), cases))
    cases = [case for case in cases if case]
    return cases


class GetData:
    def __init__(self, use_test_case=True):
        self._use_test_case = use_test_case
        if self._use_test_case:
            self._test_case = _test_case_init()
            self._least = len(self._test_case)

    def _get_one_row(self):
        if self._use_test_case:
            self._least -= 1
            return self._test_case[-self._least - 1]
        else:
            return input()

    def get_rows(self, rows, data_type=int, split=' '):
        data = []
        for i in range(rows):
            row_data = self._get_one_row().strip()
            row_data = row_data.split(split) if split else [row_data]
            new_data = list(map(data_type, row_data))
            data.append(new_data)

        return data if len(data) > 1 else data[0]

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

    def test(self, test):
        return test


def main():
    data = GetData(use_test_case=True)
    logger = Logging(False)
    while True:
        logger.debug('-' * 50)
        sol = Solution(logger)
        test = data.get_rows(1, str, None)

        print(sol.test(test))

        if data.least == 0:
            break


if __name__ == '__main__':
    main()
