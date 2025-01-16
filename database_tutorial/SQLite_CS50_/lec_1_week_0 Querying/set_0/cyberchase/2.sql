-- SQl That is Wrong!
SELECT "season" , "title" 
FROM "episodes" AS e1
WHERE e1."season" = (
    SELECT MIN("season")  
    FROM "episodes" AS e2 
    WHERE e2.season = e1.season
)
ORDER BY "season"  
;
