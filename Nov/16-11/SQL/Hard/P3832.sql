WITH daily_activity AS (
    SELECT
        user_id,
        action_date,
        action,
        LAG(action_date) OVER (
            PARTITION BY user_id
            ORDER BY action_date
        ) AS prev_date,
        LAG(action) OVER (
            PARTITION BY user_id
            ORDER BY action_date
        ) AS prev_action
    FROM activity
),
streak_groups AS (
    SELECT
        user_id,
        action_date,
        action,
        SUM(
            CASE
                WHEN prev_date = DATE_SUB(action_date, INTERVAL 1 DAY)
                     AND prev_action = action
                THEN 0
                ELSE 1
            END
        ) OVER (
            PARTITION BY user_id
            ORDER BY action_date
        ) AS streak_id
    FROM daily_activity
),
streaks AS (
    SELECT
        user_id,
        action,
        COUNT(*) AS streak_length,
        MIN(action_date) AS start_date,
        MAX(action_date) AS end_date
    FROM streak_groups
    GROUP BY user_id, action, streak_id
    HAVING COUNT(*) >= 5
),
ranked_streaks AS (
    SELECT
        user_id,
        action,
        streak_length,
        start_date,
        end_date,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY
                streak_length DESC,
                action ASC,
                start_date DESC
        ) AS rn
    FROM streaks
)
SELECT
    user_id,
    action,
    streak_length,
    start_date,
    end_date
FROM ranked_streaks
WHERE rn = 1
ORDER BY
    streak_length DESC,
    user_id ASC;
