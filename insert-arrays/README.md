# Insert Arrays

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-insert-array/solution)

---

## 📋 Problem Description

To insert an array of values, you can use the ARRAY constructor.

This would create the following rows: id

owners

balance

open_date 1

['Alice', 'Bob', 'Charlie']

1000

'2021-01-01' 2

['Jane', 'John']

2000

'2021-01-02' ChallengeYou are given a table stocks with the following columns: id of type INTEGER as the primary key

name of type TEXT

transaction_dates of type DATE[] Insert the following rows into the table in the order given: id

name

transaction_dates 1

'AAPL'

['2007-02-09', '2007-02-10', '2007-02-11'] 2

'GOOG'

['2004-12-15', '2004-12-16'] Tip: The syntax to insert an array of dates is ARRAY['YYYY-MM-DD', 'YYYY-MM-DD']::DATE[]

---

## 💡 Solution

Check the `solution.py` file in this directory for the complete implementation.

---

## 📊 Complexity Analysis

*Add your complexity analysis here after solving*

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

<sub>This problem was automatically synced from NeetCode using [NeetCode GitHub Pusher](https://github.com/)</sub>
