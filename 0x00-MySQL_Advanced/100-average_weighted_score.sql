-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN input_user_id INT)
BEGIN
  DECLARE weighted_sum FLOAT DEFAULT 0;
  DECLARE weight_total INT DEFAULT 0;
  DECLARE average_weighted_score FLOAT DEFAULT 0;

  -- Calculate the sum of (score * weight) and the sum of weights for the user
  SELECT SUM(c.score * p.weight), SUM(p.weight)
  INTO weighted_sum, weight_total
  FROM corrections AS c
  JOIN projects AS p ON c.project_id = p.id
  WHERE c.user_id = input_user_id;

  -- Check if the total weight is not zero to avoid division by zero
  IF weight_total > 0 THEN
    SET average_weighted_score = weighted_sum / weight_total;
  ELSE
    SET average_weighted_score = 0; -- or NULL if preferred
  END IF;

  -- Update the user's average_score in the users table
  UPDATE users
  SET average_score = average_weighted_score
  WHERE id = input_user_id;

END $$

DELIMITER ;
