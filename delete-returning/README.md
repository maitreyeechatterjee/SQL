# Delete Returning

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-delete-returning/solution)

---

## 📋 Problem Description

Just like with UPDATE statements, we can also use the RETURNING clause to return the rows that were deleted.

The above statement deletes all rows from the users table where the username column is NULL and returns all rows that were deleted.

We can also return specific columns rather than all columns.

The above will return only the id, username, and email columns for all rows that were deleted.

ChallengeYou are given a table called bank_accounts with the following columns: id of type INTEGER

name of type TEXT

balance of type INTEGER

last_transaction_date of type DATE Your task is to delete all rows from the bank_accounts table where the balance column is less than 0 and the last_transaction_date column is before '2024-01-01'. Return the id and name columns for all rows that were deleted.

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
