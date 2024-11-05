--  creates a function SafeDiv that divides the first by the second number
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DOUBLE
DETERMINISTIC
BEGIN
  DECLARE result DOUBLE;
  IF b = 0 THEN
    RETURN 0;
  END IF;
  SET result = a / b;
  RETURN result;
END$$

DELIMITER ;
