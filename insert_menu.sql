USE cafeteria_db;

CREATE TABLE menu(
  item_id INT AUTO_INCREMENT PRIMARY KEY,
  item_name VARCHAR(100),
  category VARCHAR(50),
  price DECIMAL(8,2)
);
INSERT INTO menu (item_name, category, price) VALUES
('Tea', 'Beverage', 15.00),
('Coffee', 'Beverage', 20.00),
('Veg Burger', 'Snacks', 50.00),
('Paneer Sandwich', 'Snacks', 45.00),
('Brownie', 'Dessert', 70.00);

select * from menu;

insert into menu(item_id,item_name,category,price)
values(6,"Cold Coffee","Beverage",40);

