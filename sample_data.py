"""
Sample Data Generator
Creates demo data for testing the system
"""
import random
from database import Database
from models import Student, Instructor, Course, WeightedGradeBook, CurvedGradeBook, PassFailGradeBook

def generate_sample_data():
    """Generate and populate sample data"""
    db = Database('student_tracker.db')
    
    # Clear existing data
    db.clear_all_data()
    
    # Sample instructors
    instructors = [
        ('INS001', 'Dr. John Smith', 'john.smith@university.edu', 'Computer Science'),
        ('INS002', 'Prof. Sarah Johnson', 'sarah.johnson@university.edu', 'Mathematics'),
        ('INS003', 'Dr. Michael Chen', 'michael.chen@university.edu', 'Physics'),
        ('INS004', 'Dr. Emily Davis', 'emily.davis@university.edu', 'Chemistry'),
    ]
    
    for inst_id, name, email, dept in instructors:
        db.add_instructor(inst_id, name, email, dept)
    
    # Sample courses
    courses = [
        ('CS101', 'Introduction to Programming', 3, 'INS001', 'weighted'),
        ('CS201', 'Data Structures', 3, 'INS001', 'weighted'),
        ('MATH101', 'Calculus I', 4, 'INS002', 'curved'),
        ('MATH201', 'Linear Algebra', 3, 'INS002', 'weighted'),
        ('PHY101', 'Physics I', 4, 'INS003', 'weighted'),
        ('CHEM101', 'Chemistry Fundamentals', 3, 'INS004', 'curved'),
    ]
    
    for course_id, name, credits, inst_id, grading in courses:
        db.add_course(course_id, name, credits, inst_id, grading)
    
    # Generate 243 random students
    first_names = [
        'Alice', 'Bob', 'Carol', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack',
        'Karen', 'Leo', 'Maria', 'Nathan', 'Olivia', 'Paul', 'Quinn', 'Rachel', 'Samuel', 'Tina',
        'Uma', 'Victor', 'Wendy', 'Xavier', 'Yara', 'Zoe', 'Aaron', 'Bella', 'Chris', 'Diana',
        'Eric', 'Fiona', 'George', 'Hannah', 'Isaac', 'Julia', 'Kevin', 'Laura', 'Michael', 'Nina',
        'Oscar', 'Patricia', 'Quincy', 'Rebecca', 'Steven', 'Tara', 'Ulysses', 'Victoria', 'Walter', 'Ximena'
    ]
    
    last_names = [
        'Johnson', 'Smith', 'White', 'Lee', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
        'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Rodriguez', 'Garcia', 'Martinez', 'Hernandez',
        'Lopez', 'Gonzalez', 'Clark', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 'King', 'Wright',
        'Scott', 'Torres', 'Peterson', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins', 'Reeves',
        'Stewart', 'Morris', 'Rogers', 'Morgan', 'Peterson', 'Cooper', 'Reed', 'Bell', 'Gomez', 'Murray'
    ]
    
    majors = ['Computer Science', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Engineering', 
              'Business', 'Psychology', 'History', 'English']
    
    students = []
    for i in range(1, 244):  # 243 students
        student_id = f'STU{i:03d}'
        first = random.choice(first_names)
        last = random.choice(last_names)
        name = f'{first} {last}'
        email = f'{first.lower()}.{last.lower()}{i}@student.edu'
        major = random.choice(majors)
        students.append((student_id, name, email, major))
    
    for stu_id, name, email, major in students:
        db.add_student(stu_id, name, email, major)
    
    # Enroll students in courses and assign grades
    course_ids = ['CS101', 'CS201', 'MATH101', 'MATH201', 'PHY101', 'CHEM101']
    student_ids = [s[0] for s in students]
    
    random.seed(42)  # For reproducible results
    
    for course_id in course_ids:
        # Randomly enroll 30-60 students per course
        enrolled_students = random.sample(student_ids, random.randint(30, 60))
        
        for student_id in enrolled_students:
            db.enroll_student(student_id, course_id)
            
            # Generate realistic grades with some at-risk students
            # 85% of students have normal/passing grades
            # 15% of students are at-risk (below 70)
            is_at_risk = random.random() < 0.15
            
            if is_at_risk:
                # At-risk students: low grades
                midterm = random.randint(35, 65) + random.random()
                assignments = random.randint(40, 65) + random.random()
                final = random.randint(30, 60) + random.random()
            else:
                # Normal/passing students
                midterm = random.randint(55, 100) + random.random()
                assignments = random.randint(60, 100) + random.random()
                final = random.randint(50, 100) + random.random()
                
                # Create correlation: higher midterm usually means higher final
                if midterm > 85:
                    final = min(100, final + random.randint(5, 15))
                elif midterm < 65:
                    final = max(50, final - random.randint(5, 10))
            
            # Round to 2 decimals
            midterm = round(midterm, 2)
            assignments = round(assignments, 2)
            final = round(final, 2)
            
            # Calculate final grade using weighted average (30%, 40%, 30%)
            final_grade = round(midterm * 0.3 + final * 0.4 + assignments * 0.3, 2)
            
            # Determine letter grade
            if final_grade >= 90:
                letter_grade = 'A'
            elif final_grade >= 80:
                letter_grade = 'B'
            elif final_grade >= 70:
                letter_grade = 'C'
            elif final_grade >= 60:
                letter_grade = 'D'
            else:
                letter_grade = 'F'
            
            db.record_grade(student_id, course_id, midterm, final, assignments, final_grade, letter_grade)
    
    print("✓ Sample data generated successfully!")
    print(f"  - {len(instructors)} instructors added")
    print(f"  - {len(courses)} courses added")
    print(f"  - {len(students)} students added")
    print(f"  - At-risk students: ~{int(len(students) * 0.15 * (len(courses)/6))} (15% of enrollments)")
    print(f"  - Total enrollments: {sum(len(random.sample([s[0] for s in students], random.randint(30, 60))) for _ in courses)}")
    
    return db

if __name__ == '__main__':
    generate_sample_data()
