# Enum

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-enum/question)

---

## 📋 Problem Description

PostgreSQL also supports the concept of an ENUM, which is a data type that restricts a column to a set of predefined values. It is similar to using a CHECK constraint, but it is a data type rather than a constraint. This makes it easier to reuse across multiple tables and columns.

In the above example, we created an ENUM called status with values active, inactive, or pending. To create an ENUM, we use the CREATE TYPE statement.

The status column in the users table can only have the values active, inactive, or pending.

ChallengeCreate an ENUM called account_type with values 'checking', 'savings', 'cd', 'money_market'.

Then, create a table called bank_accounts with the following columns: id of type INTEGER as the primary key

account_type of type account_type

balance of type INTEGER

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
