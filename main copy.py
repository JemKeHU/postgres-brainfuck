import psycopg2

def main():
    conn = None
    cur = None

    try:
        # Connect to your database
        conn = psycopg2.connect(database="datacamp_courses",
                                user="postgres",  # Your PostgreSQL username
                                host='localhost',
                                password="password",  # Your PostgreSQL password
                                port=5432)
        
        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Drop the table if it exists
        cur.execute("DROP TABLE IF EXISTS datacamp_courses;")

        # Create table if it does not exist
        cur.execute("""CREATE TABLE IF NOT EXISTS datacamp_courses(
                    course_id SERIAL PRIMARY KEY,
                    course_name VARCHAR (50) UNIQUE NOT NULL,
                    course_instructor VARCHAR (100) NOT NULL,
                    topic VARCHAR (20) NOT NULL);
                    """)

        # Insert data into the table
        cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Introduction to SQL','Izzy Weber','Julia');")
        cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Analyzing Survey Data in Python','EbunOluwa Andrew','Python');")
        cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Introduction to ChatGPT','James Chapman','Theory');")
        cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Introduction to Statistics in R','Maggie Matsui','R');")
        cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Hypothesis Testing in Python','James Chapman','Python');")

        # Commit the inserts
        conn.commit()

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the cursor and connection
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    main()
