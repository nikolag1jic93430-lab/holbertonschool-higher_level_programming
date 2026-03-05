-- List all records with a score >= 10 ordered by score (highest first)
Select score, name
From second_table
Where score >= 10
ORDER BY score DESC;
