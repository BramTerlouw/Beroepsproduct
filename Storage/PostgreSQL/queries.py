# Define the SQL command to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS fracture_incidents (
      id SERIAL PRIMARY KEY,
      patient_name VARCHAR(50),
      incident_date VARCHAR(50),
      incident_location VARCHAR(255),
      patient_complaints TEXT,
      description TEXT NOT NULL,
      scan_image VARCHAR(50) NOT NULL,
      fracture_classification VARCHAR(50),
      incident_status process_status DEFAULT 'unprocessed'
    );
"""

try:
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    cursor.execute(create_table_query)
    
    conn.commit()
    print("Table 'fracture_incidents' created successfully.")

except psycopg2.DatabaseError as e:
    print(f"Error: {e}")
    conn.rollback()
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Database connection closed.")



# Define the SQL command to insert data
insert_data_query = """
INSERT INTO fracture_incidents (description, scan_image)
VALUES (%s, %s);
"""

data_to_insert = [
    ('Op 27 augustus 2024 omstreeks 14:30 uur heeft er een ongeval plaatsgevonden op de fietsroute langs de Schouwseweg, vlakbij het park aan de rand van het dorp. De betrokken persoon, Mark Jansen, een 35-jarige man, is gevallen terwijl hij op zijn fiets reed. Bij aankomst van de hulpdiensten klaagde Mark over ernstige pijn in zijn zij en had hij moeite met ademhalen. Er zijn geen verdere details over de aard van de verwondingen op dit moment, maar de hulpdiensten hebben hem met spoed naar het ziekenhuis vervoerd voor nader onderzoek en behandeling.', 'accident_0001'),
    ('Vandaag, op 28 augustus 2024 omstreeks 11:15 uur, heeft er een ongeval plaatsgevonden voor het plaatselijke café aan de Hoofdstraat 45. De betrokken persoon is Lisa de Vries, een 42-jarige vrouw. Lisa was bezig met het uitladen van boodschappen uit haar auto toen een voorbijrijdende bestelwagen haar aanstootte. Bij aankomst van de hulpdiensten bleek Lisa ernstige pijn in haar onderrug en nek te hebben. Ze had ook moeite met bewegen en klaagde over duizeligheid. De hulpdiensten hebben ter plaatse eerste hulp verleend en Lisa is met spoed naar het ziekenhuis gebracht voor nader onderzoek en behandeling. De exacte aard van haar verwondingen wordt nog vastgesteld.', 'accident_0002'),
    ('Op 29 augustus 2024 omstreeks 16:45 uur heeft er een ongeval plaatsgevonden op het parkeerterrein bij Winkelcentrum De Zonnebaan. De betrokken persoon is Tom Peters, een 29-jarige man. Tom was bezig met het inladen van zijn winkelmand in zijn auto toen hij uitgleed op een natte plek op het asfalt en hard tegen de autodeur viel. Bij aankomst van de hulpdiensten klaagde Tom over scherpe pijn in zijn schouder en had hij moeite met bewegen. De hulpdiensten hebben ter plaatse eerste hulp verleend en Tom is met spoed naar het ziekenhuis vervoerd voor verder onderzoek en behandeling. Het is momenteel niet duidelijk hoe ernstig de verwondingen zijn.', 'accident_0003' )
]

try:
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    cursor.executemany(insert_data_query, data_to_insert)
    
    conn.commit()
    print("Data inserted successfully.")

except psycopg2.DatabaseError as e:
    print(f"Error: {e}")
    conn.rollback()
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Database connection closed.")



# Define the SQL command to retrieve data
select_data_query = "SELECT * FROM fracture_incidents;"

try:
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    cursor.execute(select_data_query)
    rows = cursor.fetchall()
    
    print("Contents of the table:")
    for row in rows:
        print(row)

except psycopg2.DatabaseError as e:
    print(f"Error: {e}")
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Database connection closed.")



# Define the SQL command to update a record
update_record_query = """
UPDATE fracture_incidents
SET 
    incident_location = %s, 
    description = %s, 
    scan_image = %s, 
    fracture_classification = %s,
    incident_status = %s
WHERE 
    id = %s;
"""

record_id = 1
update_data = (
    'Updated Location',
    'Updated description with additional details.',
    None,
    'Updated Classification',
    'in_progress',
    record_id
)

try:
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    cursor.execute(update_record_query, update_data)
    
    conn.commit()
    print(f"Record with ID {record_id} updated successfully.")

except psycopg2.DatabaseError as e:
    print(f"Error: {e}")
    conn.rollback()
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Database connection closed.")



# Define the SQL command to retrieve a record by ID
select_record_by_id_query = """
SELECT * 
FROM fracture_incidents
WHERE id = %s;
"""

record_id = 1  # Replace this with the ID of the record you want to retrieve

try:
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    cursor.execute(select_record_by_id_query, (record_id,))
    record = cursor.fetchone()
    
    if record:
        print("Retrieved record:")
        print(record)
    else:
        print(f"No record found with ID {record_id}.")

except psycopg2.DatabaseError as e:
    print(f"Error: {e}")
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Database connection closed.")



# Define the SQL command to drop a table
drop_table_query = "DROP TABLE IF EXISTS fracture_incidents;"

try:
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    cursor.execute(drop_table_query)
    
    conn.commit()
    print("Table 'fracture_incidents' dropped successfully.")

except psycopg2.DatabaseError as e:
    print(f"Error: {e}")
    conn.rollback()
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Database connection closed.")