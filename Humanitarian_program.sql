-- SQLite
CREATE TABLE jurisdiction_hierarchy (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name VARCHAR(30) NOT NULL UNIQUE,

    level VARCHAR(20) NOT NULL
    CHECK (level IN ('County', 'Sub-County', 'Village')),

    parent VARCHAR(30),

    FOREIGN KEY (parent)
    REFERENCES jurisdiction_hierarchy(name)
    ON DELETE CASCADE,

);
INSERT INTO jurisdiction_hierarchy (name, level, parent)
VALUES
('Nairobi', 'County', NULL),
('Kiambu', 'County', NULL),
('Mombasa', 'County', NULL);





SELECT * FROM jurisdiction_hierarchy

 CREATE TABLE village_locations (
    village_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Village VARCHAR(30) NOT NULL UNIQUE,
    TOTAL_POPULATION INTEGER NOT NULL CHECK (TOTAL_POPULATION >= 0),
    FOREIGN KEY (sub-county) 
        REFERENCES jurisdiction_hierarchy(name)
        ON DELETE CASCADE,
);
INSERT INTO village_locations(name,level ,parent)
('Westlands, 'Nairobi');
('kasarani,'sub-county',Nairobi);
('Lari,'sub-county','kiambu,);
('Gatundu south' sub-county','kiambu,);


 CREATE TABLE beneficiary_partner_data(
    partner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    partner  VARCHAR(30) NOT NULL,
    village  VARCHAR(30) NOT NULL,

    beneficiaries INTEGER NOT NULL,
     CHECK(beneficiaries>=0),

    beneficiary_type VARCHAR(30) NOT NULL,
    CHECK(beneficiary_type IN('individuals','Households')),
    FOREIGN KEY (Village) ,
     REFERENCES village_locations (Village),
     ON DELETE CASCADE
    );