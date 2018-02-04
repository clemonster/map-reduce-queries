# map-reduce-queries
Python MapReduce encoding of (very) basic SQL queries

Consider the following simple relational schema containing informations about clients and orders they made. Both files are in the **Data** folder

Customer(cid, startDate, name) 
Order(#cid, total)

Note that, for the sake of simplicity, we do not have any primary key for Order. Also assume that all the fields are mandatory.
We provide the Pyhton MapReduce encoding of the following SQL queries:


• query1 : `SELECT name FROM Customer WHERE month(startDate)=7`  
• query2 : `SELECT DISTINCT name FROM Customer WHERE month(startDate)=7`  
• query3 : `O.cid, SUM(total), COUNT(DISTINCT total) FROM Order O GROUP BY O.cid`   
• query4 : `SELECT C.cid, O.total FROM Customer C, Order O WHERE C.cid=O.cid`  
