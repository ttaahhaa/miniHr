CREATE TABLE miniHR.usersApplications
(
    first_name        varchar(100)       NOT NULL,
    last_name         varchar(100)       NOT NULL,
    upload_date       DATETIME           NOT NULL,
    bdate             DATE               NOT NULL,
    upload_cv         varchar(400)       NOT NULL,
    email             varchar(150)       NOT NULL,
    departmentID      varchar(75)        NOT NULL,
    yearsOfExperience INT                NOT NULL,
    ID                INT auto_increment NOT NULL,
    PRIMARY KEY (ID)
)
    ENGINE = InnoDB
    DEFAULT CHARSET = utf8
    COLLATE = utf8_general_ci;