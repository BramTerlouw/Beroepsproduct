# Define the SQL command to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS fracture_incidents (
      id SERIAL PRIMARY KEY,
      incident_date TIMESTAMP,
      incident_location VARCHAR(255),
      description TEXT NOT NULL,
      scan_image BYTEA,
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
INSERT INTO fracture_incidents (description, incident_status)
VALUES (%s, %s);
"""

data_to_insert = [
    ('In Amsterdam heeft een fietser op 24 januari 2024 rond 19:00 een ernstig ongeluk gehad terwijl hij door een drukke straat reed. De fietser raakte een gladde plek op de weg en kwam ongelukkig ten val. Na de val klaagde de fietser over hevige pijn in de pols, die direct begon op te zwellen. Omstanders hielpen de fietser overeind en alarmeerden een ambulance. In het ziekenhuis werd een röntgenfoto gemaakt, en de arts vermoedt een breuk in de pols. Het slachtoffer is opgenomen voor verdere observatie en behandeling.', 'unprocessed'),
    ('Een 38-jarige vrouw uit Rotterdam is vanmorgen op 24 januari 2024 van een trap gevallen in haar woning. Ze miste een trede terwijl ze haastig naar beneden liep om de deur te openen voor een pakketbezorger. Tijdens de val landde ze ongelukkig op haar rechterenkel, waardoor ze hevige pijn ervoer en niet meer op haar voet kon staan. Na telefonisch overleg met de huisartsenpost werd besloten om haar met spoed naar het ziekenhuis te brengen voor een röntgenonderzoek. De artsen vermoeden een complexe enkelbreuk en er wordt momenteel nagedacht over mogelijke chirurgische ingrepen.','unprocessed'),
    ('In Den Haag vond een ernstig verkeersongeval plaats waarbij een manndelijke bejaarde fietser rond de 70 jaar werd aangereden door een auto op een druk kruispunt op 24 januari 2024 rond 13:30. De automobilist kon niet op tijd remmen toen de fietser plotseling overstak. De fietser werd van de fiets geslingerd en landde hard op de grond. Omstanders belden meteen een ambulance. Het slachtoffer klaagde over hevige pijn in de schouder en kon zijn arm niet meer bewegen. De artsen hebben de breuk schouder gestabiliseerd en verdere behandeling zal nodig zijn om het herstel te bevorderen.', 'unprocessed')
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
    
    print("Contents of the 'employees' table:")
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