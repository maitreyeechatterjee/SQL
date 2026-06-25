# Select Between

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-select-between/question)

---

## 📋 Problem Description

We can use the BETWEEN keyword to filter rows based on a range of values.

This will return all rows from the comments table where the id column is between 1 and 3 inclusive, or 1 <= id <= 3. We use BETWEEN to filter for a range of values and we use the AND operator to specify both a lower and upper bound.

We can do the same for strings and other data types.

This will return all rows from the comments table where the author column is between 'Eat' and 'Neet' inclusive, or 'Eat' <= author <= 'Neet'.

This will return all rows from the comments table where the posted_at is between '2024-01-01' and '2024-01-31' inclusive. You can assume the posted_at column is a DATE data type.

ChallengeYou are given a table called cities. Return all unique countries from the country column that have a population between 1,000,000 and 10,000,000 inclusive.

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
