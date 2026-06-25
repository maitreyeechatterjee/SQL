# Select Limit

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-select-limit/question)

---

## 📋 Problem Description

It can be costly and often unnecessary to return all rows from a table. We can use the LIMIT keyword to return a subset of rows.

The above query will return the first 10 rows from the cities table.

The LIMIT clause can also be combined with the WHERE and ORDER BY clauses.

The above query will return the first 5 rows from the cities table where the population is greater than 1000000, ordered by the population in descending order.

You can think of it as a 3 step process: Filter the rows using the WHERE clause.

Order the rows using the ORDER BY clause.

Limit the rows using the LIMIT clause. ChallengeYou are given a table called flights. Return the 2 cheapest flights, ordered by the price column in ascending order, where the origin is 'London' and the destination is 'Paris'. You should return all columns.

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
