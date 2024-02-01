CREATE TABLE IF NOT EXISTS user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS payee (
    payee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NULL
);

CREATE TABLE IF NOT EXISTS employer (
    employer_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL,
    description TEXT NULL
);

CREATE TABLE IF NOT EXISTS bank_account (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    bank_name TEXT NOT NULL,
    CONSTRAINT fk_bank_account_user FOREIGN KEY (user_id) REFERENCES user (user_id)
);

CREATE TABLE IF NOT EXISTS in_payment (
    in_payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER NOT NULL,
    employer_id INTEGER NOT NULL,
    date DATE NOT NULL,
    net_amount DECIMAL(10, 2) NOT NULL,
    gross_amount DECIMAL(10, 2) NULL,
    next_payment_id INTEGER NULL,
    prev_payment_id INTEGER NULL,
    CONSTRAINT fk_in_payment_bank_account FOREIGN KEY (account_id) REFERENCES bank_account (account_id),
    CONSTRAINT fk_in_payment_employer FOREIGN KEY (employer_id) REFERENCES employer (employer_id),
    CONSTRAINT fk_in_payment_next_payment FOREIGN KEY (next_payment_id) REFERENCES in_payment (in_payment_id),
    CONSTRAINT fk_in_payment_prev_payment FOREIGN KEY (prev_payment_id) REFERENCES in_payment (in_payment_id)  
);

CREATE TABLE IF NOT EXISTS out_payment (
    out_payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_account_id INTEGER NOT NULL,
    payee_id INTEGER NOT NULL,
    date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    next_payment_id INTEGER NULL,
    prev_payment_id INTEGER NULL,
    CONSTRAINT fk_out_payment_bank_account FOREIGN KEY (source_account_id) REFERENCES bank_account (account_id),
    CONSTRAINT fk_out_payment_payee FOREIGN KEY (payee_id) REFERENCES payee (payee_id),
    CONSTRAINT fk_out_payment_next_payment FOREIGN KEY (next_payment_id) REFERENCES out_payment (out_payment_id),
    CONSTRAINT fk_out_payment_prev_payment FOREIGN KEY (prev_payment_id) REFERENCES out_payment (out_payment_id)
);

