WITH RECURSIVE formatted AS (
    SELECT
        content_id,
        content_text,
        1 AS pos,
        1 AS word_start,
        CAST('' AS CHAR(10000)) AS converted_text
    FROM user_content

    UNION ALL

    SELECT
        content_id,
        content_text,
        pos + 1,

        CASE
            WHEN SUBSTRING(content_text, pos, 1) = ' '
            THEN pos + 1
            ELSE word_start
        END,

        CONCAT(
            converted_text,
            CASE
                -- Words starting with special characters stay unchanged
                WHEN SUBSTRING(content_text, word_start, 1)
                     NOT REGEXP '^[A-Za-z]$'
                THEN SUBSTRING(content_text, pos, 1)

                -- Capitalize the first character of each word
                WHEN pos = word_start
                THEN UPPER(SUBSTRING(content_text, pos, 1))

                -- Capitalize after hyphens only for valid hyphenated words
                WHEN SUBSTRING(content_text, pos - 1, 1) = '-'
                     AND REGEXP_LIKE(
                         SUBSTRING_INDEX(
                             SUBSTRING(content_text, word_start),
                             ' ', 1
                         ),
                         '^[A-Za-z]+(-[A-Za-z]+)+$'
                     )
                THEN UPPER(SUBSTRING(content_text, pos, 1))

                ELSE LOWER(SUBSTRING(content_text, pos, 1))
            END
        )
    FROM formatted
    WHERE pos <= CHAR_LENGTH(content_text)
)


SELECT
    content_id,
    content_text AS original_text,
    converted_text
FROM formatted
WHERE pos = CHAR_LENGTH(content_text) + 1
ORDER BY content_id ASC;
