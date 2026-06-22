1SELECT name AS Customers FROM Customers
2WHERE id NOT IN(
3    SELECT CustomerId FROM Orders
4)