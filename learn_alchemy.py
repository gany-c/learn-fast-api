"""
This is not invoked from the Fast API Server, it has to be run in a standalone mode.
It will create an example.db file in the same directory.
"""

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, select, and_, insert

# Create an SQLite engine that connects to a local file called 'example.db'
engine = create_engine('sqlite:///example.db')

# Establish a connection to the database
conn = engine.connect()

# Metadata object holds schema information for table creation
metadata = MetaData()

# Define a 'Student' table with columns: Id, Name, Major, and Pass
Student = Table('Student', metadata,
                Column('Id', Integer, primary_key=True),          # Primary key column
                Column('Name', String, nullable=False),           # Name must be provided
                Column('Major', String, default="Math"),          # Default major is "Math"
                Column('Pass', Boolean, default=True))            # Default to 'Pass' is True

# Create the table in the database (if it doesn't exist already)
metadata.create_all(engine)

# Insert a single row into the Student table
stmt = insert(Student).values(Id=1, Name='Matthew', Major='English', Pass=True)
conn.execute(stmt)
conn.commit()  # Commit the transaction to persist changes

# Prepare multiple student records as a list of dictionaries
rows = [
    {'Id': 2, 'Name': 'Nisha', 'Major': 'Science', 'Pass': False},
    {'Id': 3, 'Name': 'Natasha', 'Major': 'Math', 'Pass': True},
    {'Id': 4, 'Name': 'Ben', 'Major': 'English', 'Pass': False}
]

# Insert multiple rows into the Student table using bulk insert
stmt = insert(Student)
conn.execute(stmt, rows)
conn.commit()

# Select all students from the table
query_all = select(Student)
result_all = conn.execute(query_all)
print(result_all.fetchall())  # Print all student records

# Select students whose major is 'English'
# Demonstrate the where condition.
query_english = select(Student).where(Student.c.Major == 'English')
result_english = conn.execute(query_english)
print(result_english.fetchall())  # Print English majors

# Select students majoring in English who failed (Pass != True)
# Demonstrate the 'and' condition
query_failed_english = select(Student).where(
    and_(Student.c.Major == 'English', Student.c.Pass != True)
)
result_failed_english = conn.execute(query_failed_english)
print(result_failed_english.fetchall())  # Print English majors who failed


