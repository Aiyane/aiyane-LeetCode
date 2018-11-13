/*
编写一个 SQL 查询来实现分数排名。如果两个分数相同，则两个分数排名（Rank）相同。请注意，平分后的下一个名次应该是下一个连续的整数值。换句话说，名次之间不应该有“间隔”。
+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+

例如，根据上述给定的 Scores 表，你的查询应该返回（按分数从高到低排列）：
+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
*/
/*
SELECT Score, CONVERT ( CASE 
    WHEN @preValue = Score THEN @preRank
    WHEN (@preValue := Score) >= 0 THEN @preRank := @preRank + 1
END, UNSIGNED) AS Rank
FROM Scores, (SELECT @preValue := NULL) p, (SELECT @preRank := 0) v
ORDER BY Score DESC;
*/
SELECT Score, 
    (select count(distinct(Score)) 
    from Scores
    where Score >= s.Score) 
        AS Rank
FROM Scores AS s order by Score DESC;
