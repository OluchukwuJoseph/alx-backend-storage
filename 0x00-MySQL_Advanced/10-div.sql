--  creates a function SafeDiv that divides the first by the second number
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
  IF b = 0 THEN
    RETURN 0;
  END IF;
  RETURN a / b;
END$$

DELIMITER ;