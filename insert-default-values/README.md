# Insert Default Values

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-insert-default-values/question)

---

## 📋 Problem Description

When inserting rows into a table, we can omit columns:

In the above example, we inserted 3 rows into the users table, but we only specified the id column. The name column was omitted. The resulting table is: id

name 1

NULL 2

NULL 3

NULL The name column was omitted, so the default value for name is NULL. Since the id column is a PRIMARY KEY, it is not allowed to be NULL and thus can't be omitted. Recall that if a table column is given a DEFAULT value, then that column can be omitted when inserting rows. ChallengeYou are given a table products with the following columns: id of type INTEGER as the primary key

name of type TEXT

stock of type INTEGER with a DEFAULT value of 0 Insert the following rows into the table in the order given: id

name

stock 1

'Apple'

0 2

'Banana'

0 3

'Orange'

0 You can explicitly set the stock column to 0 but it is more simple in this case to omit it since it has a DEFAULT value of 0.

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
