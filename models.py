"""
OOP Module: Grade Management System
Implements abstract classes, inheritance, and polymorphism for student grade management
"""
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict
import json

class Person(ABC):
    """Abstract base class for all persons in the system"""
    
    def __init__(self, person_id: str, name: str, email: str):
        self.person_id = person_id
        self.name = name
        self.email = email
        self.created_at = datetime.now()
    
    @abstractmethod
    def get_role(self) -> str:
        """Return the role of the person"""
        pass
    
    def __str__(self):
        return f"{self.name} ({self.get_role()})"


class Student(Person):
    """Student class inheriting from Person"""
    
    def __init__(self, student_id: str, name: str, email: str, major: str = ""):
        super().__init__(student_id, name, email)
        self.major = major
        self.gpa = 0.0
        self.courses: List[str] = []
        self.total_credits = 0
    
    def get_role(self) -> str:
        return "Student"
    
    def add_course(self, course_id: str):
        if course_id not in self.courses:
            self.courses.append(course_id)
    
    def calculate_gpa(self, grades_dict: Dict[str, float]):
        """Calculate GPA from grade dictionary"""
        if not grades_dict:
            return 0.0
        
        gpa = sum(grades_dict.values()) / len(grades_dict)
        self.gpa = round(gpa, 2)
        return self.gpa
    
    def to_dict(self):
        return {
            'student_id': self.person_id,
            'name': self.name,
            'email': self.email,
            'major': self.major,
            'gpa': self.gpa,
            'courses': self.courses
        }


class Instructor(Person):
    """Instructor class inheriting from Person"""
    
    def __init__(self, instructor_id: str, name: str, email: str, department: str = ""):
        super().__init__(instructor_id, name, email)
        self.department = department
        self.courses_teaching: List[str] = []
    
    def get_role(self) -> str:
        return "Instructor"
    
    def add_teaching_course(self, course_id: str):
        if course_id not in self.courses_teaching:
            self.courses_teaching.append(course_id)


class Course:
    """Course class for managing course information"""
    
    def __init__(self, course_id: str, course_name: str, credits: int, instructor_id: str):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.instructor_id = instructor_id
        self.enrolled_students: List[str] = []
        self.created_at = datetime.now()
    
    def enroll_student(self, student_id: str):
        if student_id not in self.enrolled_students:
            self.enrolled_students.append(student_id)
    
    def get_enrolled_count(self) -> int:
        return len(self.enrolled_students)
    
    def to_dict(self):
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'credits': self.credits,
            'instructor_id': self.instructor_id,
            'enrolled_students': len(self.enrolled_students)
        }


class GradeBook(ABC):
    """Abstract GradeBook class - base for different grading schemes"""
    
    def __init__(self, course_id: str):
        self.course_id = course_id
        self.grades: Dict[str, Dict] = {}
    
    @abstractmethod
    def calculate_final_grade(self, midterm: float, final: float, assignments: float) -> float:
        """Calculate final grade based on grading scheme"""
        pass
    
    @abstractmethod
    def get_letter_grade(self, score: float) -> str:
        """Convert numeric score to letter grade"""
        pass
    
    def add_grade(self, student_id: str, midterm: float, final: float, assignments: float):
        """Add student grades"""
        final_grade = self.calculate_final_grade(midterm, final, assignments)
        letter_grade = self.get_letter_grade(final_grade)
        
        self.grades[student_id] = {
            'midterm': midterm,
            'final': final,
            'assignments': assignments,
            'final_grade': final_grade,
            'letter_grade': letter_grade
        }
        return final_grade
    
    def get_grade(self, student_id: str) -> Dict:
        return self.grades.get(student_id, {})


class WeightedGradeBook(GradeBook):
    """Weighted grading scheme: Midterm 30%, Final 40%, Assignments 30%"""
    
    def __init__(self, course_id: str, weights: Dict[str, float] = None):
        super().__init__(course_id)
        if weights is None:
            weights = {'midterm': 0.3, 'final': 0.4, 'assignments': 0.3}
        self.weights = weights
    
    def calculate_final_grade(self, midterm: float, final: float, assignments: float) -> float:
        """Calculate weighted final grade"""
        weighted_grade = (
            midterm * self.weights['midterm'] +
            final * self.weights['final'] +
            assignments * self.weights['assignments']
        )
        return round(weighted_grade, 2)
    
    def get_letter_grade(self, score: float) -> str:
        """Convert score to letter grade using 4.0 scale"""
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"


class CurvedGradeBook(GradeBook):
    """Curved grading scheme"""
    
    def __init__(self, course_id: str, curve_factor: float = 1.05):
        super().__init__(course_id)
        self.curve_factor = curve_factor
    
    def calculate_final_grade(self, midterm: float, final: float, assignments: float) -> float:
        """Calculate curved grade"""
        base_grade = (midterm + final + assignments) / 3
        curved_grade = min(base_grade * self.curve_factor, 100)
        return round(curved_grade, 2)
    
    def get_letter_grade(self, score: float) -> str:
        if score >= 95:
            return "A+"
        elif score >= 90:
            return "A"
        elif score >= 85:
            return "B+"
        elif score >= 80:
            return "B"
        elif score >= 75:
            return "C+"
        elif score >= 70:
            return "C"
        else:
            return "F"


class PassFailGradeBook(GradeBook):
    """Pass/Fail grading scheme"""
    
    def __init__(self, course_id: str, passing_score: float = 70):
        super().__init__(course_id)
        self.passing_score = passing_score
    
    def calculate_final_grade(self, midterm: float, final: float, assignments: float) -> float:
        """Calculate average for pass/fail determination"""
        return round((midterm + final + assignments) / 3, 2)
    
    def get_letter_grade(self, score: float) -> str:
        if score >= self.passing_score:
            return "PASS"
        else:
            return "FAIL"
