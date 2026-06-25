# Update Where

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-update-where/question)

---

## 📋 Problem Description

We can also specify which rows to update using a WHERE clause. It works similarly to the WHERE clause in a SELECT statement.

The above statement updates the email column, only for the row where id is 1. If the id is the primary key, then we can expect this to only update a single row.

In some cases, an UPDATE statement can also be used to clean up corrupted data. For example, the below statement will update any negative score values to 0.

ChallengeYou are given a table called users with the following columns: id of type INTEGER

username of type TEXT Your task is to update the username column to anonymous for the rows where the username is NULL.

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
