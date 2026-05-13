# Friendships Assignment

This project focuses on many-to-many relationships within a SQL database, specifically modeling a social network "friendships" system.

## Contents
- **`friendships-quires.sql`**: Contains schema creation, data insertion, and relationship queries.

## Database Schema
- **`users`**: Stores user profiles (first name, last name).
- **`friendships`**: A self-referencing join table that links users to their friends.

## Implemented Queries
- **Schema Setup**: Creating the database and tables with proper foreign keys.
- **Data Seeding**: Inserting initial users and establishing friendship links.
- **Relationship Display**: A query to show which users are friends with whom.
- **Ninja Challenges**:
  - Finding all friends of a specific user.
  - Counting the total number of friendships in the system.
  - Identifying the user with the most friends.
  - Sorting a user's friends alphabetically.
