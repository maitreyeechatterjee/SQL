# Select Like

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/sql-select-like/question)

---

## 📋 Problem Description

PostgreSQL provides the LIKE operator to filter strings based on patterns rather than exact string matching.

The LIKE operator uses the following wildcard characters: %: Matches any sequence of characters.

_: Matches any single character. For example, if we want to return all rows from the comments table where the author column starts with an N, we can use the following query:

This will return all rows where the author column starts with N, where the % wildcard matches any sequence of characters. The comparison is case-sensitive, so it will only return rows where the author column starts with N and not an n.

If we want to return all rows where the author column starts with an N and has at least 3 characters, we can use the following query:

The N__% has three components: N: The first character must be N.

__%: The second and third characters can be any characters.

%': The rest of the string can be any characters, or nothing at all. ChallengeYou are given a table called cities. Return the name of all cities where the name column contains the substring ai. Hint: You can use the % wildcard multiple times in your pattern.

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
