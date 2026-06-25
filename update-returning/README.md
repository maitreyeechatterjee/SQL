# Update Returning

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-update-returning/question)

---

## 📋 Problem Description

Within an UPDATE statement, we can use the RETURNING clause to return the rows that were updated. This is useful if we want to see the results of the update.

The RETURNING * clause returns all columns for the rows that were updated.

We can also specify which columns to return by listing them in the clause.

ChallengeYou are given a table called bank_accounts with the following columns: id of type INTEGER

balance of type INTEGER

name of type TEXT

status of type TEXT Your task is to update the status column to VIP for all rows where the balance is greater than 10000 and less than 100000. Return the id, balance and status columns for the rows that were updated.

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
