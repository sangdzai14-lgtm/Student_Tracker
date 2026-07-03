"""
Database Module: SQLite Database Management
Handles all database operations for students, courses, grades, and enrollments
"""
import sqlite3
from datetime import datetime
from typing import List, Dict, Tuple
import os

class Database:
    """SQLite Database Manager"""
    
    def __init__(self, db_path: str = 'student_tracker.db'):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database schema"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Students table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                major TEXT,
                gpa REAL DEFAULT 0.0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Instructors table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS instructors (
                instructor_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                department TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Courses table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                course_id TEXT PRIMARY KEY,
                course_name TEXT NOT NULL,
                credits INTEGER,
                instructor_id TEXT,
                grading_scheme TEXT DEFAULT 'weighted',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
            )
        ''')
        
        # Enrollments table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS enrollments (
                enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                course_id TEXT NOT NULL,
                enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (student_id) REFERENCES students(student_id),
                FOREIGN KEY (course_id) REFERENCES courses(course_id),
                UNIQUE(student_id, course_id)
            )
        ''')
        
        # Grades table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                course_id TEXT NOT NULL,
                midterm REAL,
                final REAL,
                assignments REAL,
                final_grade REAL,
                letter_grade TEXT,
                recorded_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (student_id) REFERENCES students(student_id),
                FOREIGN KEY (course_id) REFERENCES courses(course_id),
                UNIQUE(student_id, course_id)
            )
        ''')
        
        # Assignments table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS assignments (
                assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_id TEXT NOT NULL,
                assignment_name TEXT NOT NULL,
                due_date TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (course_id) REFERENCES courses(course_id)
            )
        ''')
        
        # Assignment submissions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS assignment_submissions (
                submission_id INTEGER PRIMARY KEY AUTOINCREMENT,
                assignment_id INTEGER NOT NULL,
                student_id TEXT NOT NULL,
                submission_date TIMESTAMP,
                score REAL,
                FOREIGN KEY (assignment_id) REFERENCES assignments(assignment_id),
                FOREIGN KEY (student_id) REFERENCES students(student_id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_student(self, student_id: str, name: str, email: str, major: str = ""):
        """Add a new student"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO students (student_id, name, email, major)
                VALUES (?, ?, ?, ?)
            ''', (student_id, name, email, major))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()
    
    def add_course(self, course_id: str, course_name: str, credits: int, instructor_id: str, grading_scheme: str = 'weighted'):
        """Add a new course"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO courses (course_id, course_name, credits, instructor_id, grading_scheme)
                VALUES (?, ?, ?, ?, ?)
            ''', (course_id, course_name, credits, instructor_id, grading_scheme))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()
    
    def add_instructor(self, instructor_id: str, name: str, email: str, department: str = ""):
        """Add a new instructor"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO instructors (instructor_id, name, email, department)
                VALUES (?, ?, ?, ?)
            ''', (instructor_id, name, email, department))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()
    
    def enroll_student(self, student_id: str, course_id: str) -> bool:
        """Enroll a student in a course"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO enrollments (student_id, course_id)
                VALUES (?, ?)
            ''', (student_id, course_id))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()
    
    def record_grade(self, student_id: str, course_id: str, midterm: float, final: float, assignments: float, final_grade: float, letter_grade: str):
        """Record student grade"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT OR REPLACE INTO grades 
                (student_id, course_id, midterm, final, assignments, final_grade, letter_grade)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (student_id, course_id, midterm, final, assignments, final_grade, letter_grade))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error recording grade: {e}")
            return False
        finally:
            conn.close()
    
    def get_student(self, student_id: str) -> Dict:
        """Get student information"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return dict(row)
        return None
    
    def get_all_students(self) -> List[Dict]:
        """Get all students"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM students ORDER BY name')
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def get_all_courses(self) -> List[Dict]:
        """Get all courses"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM courses ORDER BY course_name')
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def get_student_courses(self, student_id: str) -> List[Dict]:
        """Get courses enrolled by a student"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT c.* FROM courses c
            INNER JOIN enrollments e ON c.course_id = e.course_id
            WHERE e.student_id = ?
            ORDER BY c.course_name
        ''', (student_id,))
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def get_student_grades(self, student_id: str) -> List[Dict]:
        """Get all grades for a student"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT g.*, c.course_name FROM grades g
            INNER JOIN courses c ON g.course_id = c.course_id
            WHERE g.student_id = ?
            ORDER BY g.recorded_date DESC
        ''', (student_id,))
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def get_course_grades(self, course_id: str) -> List[Dict]:
        """Get all grades for a course"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT g.*, s.name FROM grades g
            INNER JOIN students s ON g.student_id = s.student_id
            WHERE g.course_id = ?
            ORDER BY s.name
        ''', (course_id,))
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def get_class_statistics(self, course_id: str) -> Dict:
        """Get statistics for a course"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT 
                COUNT(*) as student_count,
                AVG(final_grade) as avg_grade,
                MAX(final_grade) as max_grade,
                MIN(final_grade) as min_grade
            FROM grades
            WHERE course_id = ?
        ''', (course_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                'student_count': row[0] or 0,
                'avg_grade': round(row[1] or 0, 2),
                'max_grade': row[2] or 0,
                'min_grade': row[3] or 0
            }
        return {'student_count': 0, 'avg_grade': 0, 'max_grade': 0, 'min_grade': 0}
    
    def get_student_gpa(self, student_id: str) -> float:
        """Calculate student GPA"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT AVG(final_grade) FROM grades
            WHERE student_id = ?
        ''', (student_id,))
        row = cursor.fetchone()
        conn.close()
        
        gpa = row[0] if row and row[0] else 0.0
        return round(gpa, 2)
    
    def get_at_risk_students(self, threshold: float = 70) -> List[Dict]:
        """Get students with grades below threshold"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT DISTINCT s.student_id, s.name, s.email, AVG(g.final_grade) as avg_grade
            FROM students s
            INNER JOIN grades g ON s.student_id = g.student_id
            GROUP BY s.student_id
            HAVING AVG(g.final_grade) < ?
            ORDER BY avg_grade
        ''', (threshold,))
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def clear_all_data(self):
        """Clear all data from database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        tables = ['assignment_submissions', 'assignments', 'grades', 'enrollments', 'courses', 'instructors', 'students']
        for table in tables:
            cursor.execute(f'DELETE FROM {table}')
        
        conn.commit()
        conn.close()
