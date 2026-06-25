# Select Order By

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-select-order-by/solution)

---

## 📋 Problem Description

We can use the ORDER BY clause to sort the results of a query in ascending or descending order.

This would return the rows sorted by the population column in descending order. The ORDER BY clause is applied after the WHERE clause. If we had not included the WHERE clause, all rows would be sorted by the population column in descending order. name

population

country Tokyo

37400068

Japan Mumbai

20660000

India Cairo

20010000

Egypt New Delhi

19640000

India If we want to sort the results in ascending order, we can use the ASC keyword or simply omit it.

The output might look like this: name

population

country New Delhi

19640000

India Cairo

20010000

Egypt Mumbai

20660000

India Tokyo

37400068

Japan ChallengeYou are given a table called comments. Return all author, body and created_at columns sorted by the created_at column in descending order.

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
