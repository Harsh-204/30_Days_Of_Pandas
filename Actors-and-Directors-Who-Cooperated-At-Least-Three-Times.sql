1# Write your MySQL query statement below
2select actor_id, director_id from ActorDirector
3group by actor_id, director_id
4having count(*) > 2