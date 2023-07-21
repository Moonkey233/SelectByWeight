# SelectByWeight

[中文教程请点击此处](./README_CN.md)

A Python script that RANDOM SELECT an item from a text file that contains a list of items and their corresponding weights.

## Usage

1. Edit the `select.txt` file with the items and their weights in the specified format. You can use `#` to comment out some items.
2. Run the `select.py` script. It will output all the items and their corresponding weight ranges.
3. The script will randomly select an item and output the selection result. It will then wait for the user to press any key to continue.

## Features

- Can randomly select an item based on its weight.
- Can exclude some items that do not need to be selected.
- Can output all the available items and their corresponding weight ranges.
- Can handle some mistakes.

This script is suitable for scenarios where random selection is required based on weights, such as lottery, random recommendation, etc.

## File Format

The `select.txt` file should be formatted as follows:

```
ItemA [WeightA]
ItemB [WeightB]
# Commented Item
ItemC [WeightC]
```

- Each line represents an item and its weight.
- Use `#` to comment out some items.
- The weight is enclosed in square brackets `[]`.
- The weight must be a integer(include 0).

## Example

Here is an example of the `select.txt` file:

```
Apple [5]
Banana [3]
# Commented Item
Orange [2]
Grape [0]
```

When you run the `select.py` script, it will output the following:

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

In this example, the script randomly selected `Apple` based on its weight (`4`).

```
Play[10]
Sleep [20]

 Study[0]
Can handle weight missing mistakes[10
Can handle NaN mistakes[1a]
Can handle return line and space
 #Can commet temporarily[100]


 This is last Selection      [1]


```

When you run the `select.py` script, it will output the following:

```
Invaild Weight Error: 'Can handle weight missing mistakesCan handle weight missing mistakes[10'
Invaild Weight Error: 'Can handle NaN mistakes'
Invaild Weight Error: 'Can handle return line and spacCan handle return line and space'
Excluded: 'Can commet temporarily'

All Selections:

'Play' Weight: 32.26% Range: [0, 10)
'Sleep' Weight: 64.52% Range: [10, 30)
'Study' Weight: 0.0% Range: [30, 30)
'This is last Selection' Weight: 3.23% Range: [30, 31)
Total Weight: 31

Random Selected (13): Sleep

Press any key to continue . . .
```

In this example, the script randomly selected `Sleep` based on its weight (`13`).
