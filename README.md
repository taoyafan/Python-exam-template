## python笔试题模板
包含标准输入、Test case输入，Logging

## 使用说明
### 数据输入
GetData(use_test_case) 输入参数为True说明使用 Test case 测试程序，为 False 则通过标准输入获得数据。
Test case 在 test_cases() 中定义，与标准输入格式相同。

data.get_rows(rows, data_type=int, split=' ') 中的参数 rows 为获取的行数，data_type 表示将输入的目标数据类型，split 为一行数据的分割方法，默认按照空格分割。

### 调试信息打印
logger = Logging(enable)输入为 True 则打印调试信息，否则屏蔽所有打印信息
logger.debug(str) 打印 str 

### 算法实现
在class Solution中定义算法函数并完成，返回值将在 main 函数中打印出来。