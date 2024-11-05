-- Create trigger to decrease item quantity after adding a new order
CREATE TRIGGER IF NOT EXISTS update_quantity
AFTER INSERT
ON orders FOR EACH ROW
-- Update the quantity of the item in the items table
UPDATE items SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;