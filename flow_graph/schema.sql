DROP TABLE IF EXISTS form_data;

CREATE TABLE form_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    'date' TEXT NOT NULL,
    'activity' TEXT NOT NULL,
    'category' TEXT NOT NULL,
    'difficulty' INTEGER(4) NOT NULL,
    'skill' INTEGER(4) NOT NULL,
    'skill_feel' INTEGER(4) NOT NULL,
    'immersed' INTEGER(4) NOT NULL,
    'objective' INTEGER(4) NOT NULL,
    'control' INTEGER(4) NOT NULL,
    'other' INTEGER(4) NOT NULL,
    'time' INTEGER(4) NOT NULL,
    'fail' INTEGER(4) NOT NULL,
    'learn' INTEGER(4) NOT NULL,
    'want' INTEGER(1) NOT NULL,
    'happiness' INTEGER(4) NOT NULL,
    'social' TEXT NOT NULL
);