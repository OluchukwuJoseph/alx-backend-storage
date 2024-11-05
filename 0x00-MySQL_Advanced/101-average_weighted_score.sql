--  creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  DECLARE done INT DEFAULT 0;
  DECLARE current_user_id INT;
  DECLARE weighted_sum FLOAT;
  DECLARE weight_total INT;
  DECLARE average_weighted_score FLOAT;

  -- Cursor to iterate over each user in the users table
  DECLARE user_cursor CURSOR FOR
    SELECT id FROM users;

  -- Handler to set `done` to 1 when there are no more rows in the cursor
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

  -- Open the cursor
  OPEN user_cursor;

  -- Loop through all users
  user_loop: LOOP
    FETCH user_cursor INTO current_user_id;

    -- Exit the loop if there are no more rows
    IF done = 1 THEN
      LEAVE user_loop;
    END IF;

    -- Calculate the weighted sum and total weight for the current user
    SELECT SUM(C.score * P.weight), SUM(P.weight)
    INTO weighted_sum, weight_total
    FROM corrections AS C
    JOIN projects AS P
    ON C.project_id = P.id
    WHERE C.user_id = current_user_id;

    -- Check if the total weight is not zero to avoid division by zero
    IF weight_total > 0 THEN
      SET average_weighted_score = weighted_sum / weight_total;
    ELSE
      SET average_weighted_score = 0;
    END IF;

    UPDATE users SET average_score = average_weighted_score
    WHERE id = current_user_id;

  END LOOP;

  CLOSE user_cursor;
END$$

DELIMITER ;