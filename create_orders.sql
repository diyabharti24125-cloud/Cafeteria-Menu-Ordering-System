CREATE TABLE orders(
  order_id INT AUTO_INCREMENT PRIMARY KEY,
  item_name VARCHAR(100),
  quantity INT,
  total_price DECIMAL(10,2),
  order_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

select * from orders;
