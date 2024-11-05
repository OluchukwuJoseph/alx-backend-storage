-- Creates a procedure AddBonus that adds a new correction for a student.
DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
  DECLARE project_id INT;
  IF project_name NOT IN (SELECT name FROM projects) THEN
    INSERT INTO projects (name) VALUES (project_name);
    SET project_id = LAST_INSERT_ID();
  ELSE
    SET project_id = (SELECT id FROM projects WHERE name = project_name);
  END IF;
  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END$$

DELIMITER ;
