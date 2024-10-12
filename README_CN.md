# SelectByWeight

[English Edition Please Press Here](./README.md)

这是一个Python脚本，可以从包含项目和对应权重的文本文件中随机选择一个项。

## 使用方法

1. 使用指定格式编辑 `select.txt` 文件中的项目及其权重。您可以使用 `#` 注释掉一些项目。
2. 运行 `select.py` 脚本。它将输出所有可选项及其对应的权重范围。
3. 脚本将随机选择一个项并输出选择结果，然后等待用户按任意键继续。

## 特性

- 可以按权重随机选择一个项。
- 可以排除不需要选择的项目。
- 可以输出所有可用项目及其对应的权重范围。
- 可以处理某些错误。
- 此脚本适用于需要基于权重进行随机选择的情况，如抽奖、随机推荐等。

## 文件格式

`select.txt` 文件应按以下格式进行格式化：

```
ItemA [WeightA]
ItemB [WeightB]
# Commented Item
ItemC [WeightC]
```

每行表示一个项目及其权重。
使用 `#` 注释掉一些项目。
权重用方括号 `[]` 括起来。
权重必须是整数（包括 0）。

## 示例

以下是 `select.txt` 文件的示例：

```
Apple [5]
Banana [3]
# Commented Item
Orange [2]
Grape [0]
```

当您运行 `select.py` 脚本时，它将输出如下内容：

```
Excluded: ' Commented Ite# Commented Item'

All Selections:

'Apple' Weight: 50.0% Range: [0, 5)
'Banana' Weight: 30.0% Range: [5, 8)
'Orange' Weight: 20.0% Range: [8, 10)
'Grape' Weight: 0.0% Range: [10, 10)
Total Weight: 10

Random Selected (4): Apple

Press any key to continue . . .
```

在此示例中，脚本基于其权重（4）随机选择了 Apple。

```
Play [10]
Sleep [20]

Study [0]
Can handle weight missing mistakes [10
Can handle NaN mistakes [1a]
Can handle return line and space
# Can comment temporarily [100]

This is last Selection [1]
```

当您运行 `select.py` 脚本时，它将输出如下内容：

```
Invalid Weight Error: 'Can handle weight missing mistakesCan handle weight missing mistakes[10'
Invalid Weight Error: 'Can handle NaN mistakes'
Invalid Weight Error: 'Can handle return line and spacCan handle return line and space'
Excluded: 'Can comment temporarily'

All Selections:

'Play' Weight: 32.26% Range: [0, 10)
'Sleep' Weight: 64.52% Range: [10, 30)
'Study' Weight: 0.0% Range: [30, 30)
'This is last Selection' Weight: 3.23% Range: [30, 31)
Total Weight: 31

Random Selected (13): Sleep

Press any key to continue . . .
```

在此示例中，脚本基于其权重（13）随机选择了 Sleep。
