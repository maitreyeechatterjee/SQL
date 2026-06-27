# Delete Truncate

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-delete-truncate/question)

---

## 📋 Problem Description

If we want to delete all rows from a table, it is more efficient to use the TRUNCATE statement instead of the DELETE statement.

The above TRUNCATE statement deletes all rows from the users table. It is more efficient than the DELETE statement because it does not log the deleted rows and deletes all the rows in one step, rather than deleting one row at a time.

You could also delete all rows using the DROP TABLE statement discussed earlier in the course, but that will also delete the table itself, where as TRUNCATE will leave the table in place, but empty.

You can read more about TRUNCATE and DELETE in the PostgreSQL documentation.

ChallengeYou are given a table called students. Use the TRUNCATE statement to delete all rows from the students table.

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
