# Delete Constraints

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-delete-constraints/question)

---

## 📋 Problem Description

Table constraints, such as the UNIQUE, NOT NULL, and PRIMARY KEY constraints also apply when we delete rows from a table.

For example, if we had two tables with this structure:

users table id

name

school_id 1

Alice

1 2

Bob

2 schools table id

name 1

MIT 2

Stanford If we try to delete a row from the schools table, we will get an error because the users table has a foreign key constraint that references the schools table.

In this simple example, the easiest way to fix this would be to delete all rows from the users table that reference the schools table. Or simply delete all rows from the users table and then delete all rows from the schools table.

ChallengeYou are given three tables: students, classes, and enrollments.

We are currently trying to delete all of the tables, but currently, we violate a foreign key constraint. Reorder the three DELETE statements so that the DELETE statements are executed in the correct order.

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
