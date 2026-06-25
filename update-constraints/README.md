# Update Constraints

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-update-constraints/question)

---

## 📋 Problem Description

Earlier in the course, we learned about constraints, such as the UNIQUE, NOT NULL, and PRIMARY KEY constraints.

These constraints apply not only when we insert new rows, but also when we update existing rows.

For example, if we had a table with this structure:

We would not be able to run the following update:

We can not set the name column to NULL because the NOT NULL constraint prevents it.

ChallengeYou are given a table called bank_accounts with the following columns: id of type INTEGER

balance of type INTEGER

name of type TEXT

account_status of enum type status There is an existing UPDATE statement, but it has a bug. It currently updates 3 columns, but it violates a constraint for one of them. Fix the bug by changing the statement so that it only updates 2 columns, and does not violate any constraints. Hint: You can run the code to see the error message. It may help you understand what the bug is.

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
