"""
Analytics Module: Statistical Analysis and Predictions
Performs grade analysis, correlations, and grade predictions
"""
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from database import Database
from sklearn.linear_model import LinearRegression
import pickle
import os

class GradeAnalytics:
    """Analytics engine for grade data analysis"""
    
    def __init__(self, db: Database):
        self.db = db
        self.model = None
        self.model_path = 'grade_prediction_model.pkl'
    
    def get_course_statistics(self, course_id: str) -> Dict:
        """Get comprehensive statistics for a course"""
        grades_data = self.db.get_course_grades(course_id)
        
        if not grades_data:
            return {
                'course_id': course_id,
                'student_count': 0,
                'avg_grade': 0,
                'median_grade': 0,
                'std_dev': 0,
                'pass_rate': 0,
                'fail_rate': 0
            }
        
        df = pd.DataFrame(grades_data)
        final_grades = df['final_grade'].dropna()
        
        if len(final_grades) == 0:
            return {
                'course_id': course_id,
                'student_count': 0,
                'avg_grade': 0,
                'median_grade': 0,
                'std_dev': 0,
                'pass_rate': 0,
                'fail_rate': 0
            }
        
        pass_count = len(df[df['final_grade'] >= 70])
        total_count = len(df)
        
        return {
            'course_id': course_id,
            'student_count': len(df),
            'avg_grade': round(final_grades.mean(), 2),
            'median_grade': round(final_grades.median(), 2),
            'std_dev': round(final_grades.std(), 2),
            'pass_rate': round((pass_count / total_count * 100) if total_count > 0 else 0, 2),
            'fail_rate': round(((total_count - pass_count) / total_count * 100) if total_count > 0 else 0, 2),
            'min_grade': float(final_grades.min()),
            'max_grade': float(final_grades.max())
        }
    
    def get_student_statistics(self, student_id: str) -> Dict:
        """Get statistics for a student"""
        grades_data = self.db.get_student_grades(student_id)
        
        if not grades_data:
            return {
                'student_id': student_id,
                'gpa': 0,
                'course_count': 0,
                'best_grade': 0,
                'worst_grade': 0,
                'average_grade': 0
            }
        
        df = pd.DataFrame(grades_data)
        final_grades = df['final_grade'].dropna()
        
        return {
            'student_id': student_id,
            'gpa': round(final_grades.mean(), 2),
            'course_count': len(df),
            'best_grade': float(final_grades.max()) if len(final_grades) > 0 else 0,
            'worst_grade': float(final_grades.min()) if len(final_grades) > 0 else 0,
            'average_grade': round(final_grades.mean(), 2) if len(final_grades) > 0 else 0
        }
    
    def get_grade_distribution(self, course_id: str) -> Dict[str, int]:
        """Get grade distribution for a course"""
        grades_data = self.db.get_course_grades(course_id)
        
        distribution = {
            'A': 0,  # 90-100
            'B': 0,  # 80-89
            'C': 0,  # 70-79
            'D': 0,  # 60-69
            'F': 0   # < 60
        }
        
        for grade in grades_data:
            score = grade['final_grade']
            if score >= 90:
                distribution['A'] += 1
            elif score >= 80:
                distribution['B'] += 1
            elif score >= 70:
                distribution['C'] += 1
            elif score >= 60:
                distribution['D'] += 1
            else:
                distribution['F'] += 1
        
        return distribution
    
    def analyze_correlation(self, course_id: str) -> Dict[str, float]:
        """Analyze correlation between midterm and final grades"""
        grades_data = self.db.get_course_grades(course_id)
        
        if len(grades_data) < 2:
            return {'correlation': 0, 'r_squared': 0}
        
        df = pd.DataFrame(grades_data)
        
        # Remove rows with missing values
        df_clean = df[['midterm', 'final']].dropna()
        
        if len(df_clean) < 2:
            return {'correlation': 0, 'r_squared': 0}
        
        correlation = df_clean['midterm'].corr(df_clean['final'])
        
        return {
            'correlation': round(correlation, 3) if not np.isnan(correlation) else 0,
            'r_squared': round(correlation ** 2, 3) if not np.isnan(correlation) else 0,
            'sample_size': len(df_clean)
        }
    
    def train_prediction_model(self):
        """Train grade prediction model on all available data"""
        all_students = self.db.get_all_students()
        
        X_list = []  # Features: [midterm, assignments, course_difficulty]
        y_list = []  # Target: final_grade
        
        for student in all_students:
            student_id = student['student_id']
            grades_data = self.db.get_student_grades(student_id)
            
            for grade in grades_data:
                if grade['midterm'] is not None and grade['assignments'] is not None and grade['final_grade'] is not None:
                    # Use midterm and assignments as features
                    X_list.append([grade['midterm'], grade['assignments']])
                    y_list.append(grade['final_grade'])
        
        if len(X_list) < 3:
            print("Not enough data to train model")
            return False
        
        X = np.array(X_list)
        y = np.array(y_list)
        
        self.model = LinearRegression()
        self.model.fit(X, y)
        
        # Save model
        try:
            with open(self.model_path, 'wb') as f:
                pickle.dump(self.model, f)
        except Exception as e:
            print(f"Error saving model: {e}")
        
        return True
    
    def predict_final_grade(self, midterm: float, assignments: float) -> Dict:
        """Predict final grade based on midterm and assignments scores"""
        # Load model if not already loaded
        if self.model is None:
            if os.path.exists(self.model_path):
                try:
                    with open(self.model_path, 'rb') as f:
                        self.model = pickle.load(f)
                except Exception as e:
                    print(f"Error loading model: {e}")
                    return {'predicted_grade': 0, 'confidence': 0}
            else:
                # Train new model
                self.train_prediction_model()
                if self.model is None:
                    return {'predicted_grade': 0, 'confidence': 0}
        
        try:
            predicted = self.model.predict([[midterm, assignments]])[0]
            predicted_grade = max(0, min(100, predicted))  # Clamp between 0-100
            
            return {
                'predicted_grade': round(predicted_grade, 2),
                'confidence': 0.85,  # Simplified confidence
                'midterm_weight': round(self.model.coef_[0], 3) if len(self.model.coef_) > 0 else 0,
                'assignments_weight': round(self.model.coef_[1], 3) if len(self.model.coef_) > 1 else 0
            }
        except Exception as e:
            print(f"Error making prediction: {e}")
            return {'predicted_grade': 0, 'confidence': 0}
    
    def identify_at_risk_students(self, threshold: float = 70) -> List[Dict]:
        """Identify students at risk of failing"""
        at_risk = self.db.get_at_risk_students(threshold)
        
        result = []
        for student in at_risk:
            result.append({
                'student_id': student['student_id'],
                'name': student['name'],
                'email': student['email'],
                'current_avg': round(student['avg_grade'], 2),
                'risk_level': 'High' if student['avg_grade'] < 60 else 'Medium'
            })
        
        return result
    
    def get_top_performers(self, course_id: str = None, limit: int = 10) -> List[Dict]:
        """Get top performing students"""
        if course_id:
            grades_data = self.db.get_course_grades(course_id)
        else:
            # Get top students across all courses
            all_students = self.db.get_all_students()
            grades_data = []
            for student in all_students:
                student_grades = self.db.get_student_grades(student['student_id'])
                # Add student name to each grade record
                for grade in student_grades:
                    grade['name'] = student['name']
                grades_data.extend(student_grades)
        
        if not grades_data:
            return []
        
        df = pd.DataFrame(grades_data)
        df_sorted = df.sort_values('final_grade', ascending=False).head(limit)
        
        result = []
        for _, row in df_sorted.iterrows():
            result.append({
                'student_id': row['student_id'],
                'name': row['name'],
                'grade': float(row['final_grade']),
                'course': row.get('course_name', 'N/A')
            })
        
        return result
    
    def get_semester_trend(self, student_id: str) -> List[Dict]:
        """Get grade trend over courses/time"""
        grades_data = self.db.get_student_grades(student_id)
        
        if not grades_data:
            return []
        
        df = pd.DataFrame(grades_data)
        df = df.sort_values('recorded_date')
        
        result = []
        for _, row in df.iterrows():
            result.append({
                'course': row['course_name'],
                'grade': float(row['final_grade']),
                'date': str(row['recorded_date'])
            })
        
        return result


class VisualizationData:
    """Prepare data for visualizations"""
    
    def __init__(self, analytics: GradeAnalytics):
        self.analytics = analytics
    
    def get_grade_distribution_data(self, course_id: str) -> Dict:
        """Prepare data for grade distribution chart"""
        distribution = self.analytics.get_grade_distribution(course_id)
        
        return {
            'labels': list(distribution.keys()),
            'data': list(distribution.values()),
            'type': 'bar'
        }
    
    def get_gpa_trend_data(self, student_id: str) -> Dict:
        """Prepare data for GPA trend chart"""
        trend = self.analytics.get_semester_trend(student_id)
        
        if not trend:
            return {'labels': [], 'data': []}
        
        labels = [t['course'] for t in trend]
        data = [t['grade'] for t in trend]
        
        return {
            'labels': labels,
            'data': data,
            'type': 'line'
        }
    
    def get_class_comparison_data(self) -> Dict:
        """Prepare data for class difficulty comparison"""
        all_courses = self.analytics.db.get_all_courses()
        
        course_names = []
        avg_grades = []
        
        for course in all_courses:
            stats = self.analytics.get_course_statistics(course['course_id'])
            course_names.append(course['course_name'])
            avg_grades.append(stats['avg_grade'])
        
        return {
            'labels': course_names,
            'data': avg_grades,
            'type': 'bar'
        }
