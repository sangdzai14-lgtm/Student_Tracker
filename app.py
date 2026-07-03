"""
Flask Web Application: Student Academic Portal
Main application with all routes and web interface
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for
from database import Database
from analytics import GradeAnalytics, VisualizationData
from models import Student, WeightedGradeBook, CurvedGradeBook, PassFailGradeBook
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'student_tracker_secret_key_2024'

# Initialize database and analytics
db = Database('student_tracker.db')
analytics = GradeAnalytics(db)
viz_data = VisualizationData(analytics)

# Generate sample data if database is empty
if len(db.get_all_students()) == 0:
    from sample_data import generate_sample_data
    generate_sample_data()
    # Train prediction model
    analytics.train_prediction_model()

@app.route('/')
def index():
    """Dashboard"""
    students = db.get_all_students()
    courses = db.get_all_courses()
    at_risk = analytics.identify_at_risk_students()
    top_performers = analytics.get_top_performers(limit=5)
    
    return render_template('index.html',
                         total_students=len(students),
                         total_courses=len(courses),
                         at_risk_count=len(at_risk),
                         top_performers=top_performers)

@app.route('/students')
def students_list():
    """View all students"""
    students = db.get_all_students()
    
    # Add GPA for each student
    for student in students:
        student['gpa'] = db.get_student_gpa(student['student_id'])
    
    return render_template('students.html', students=students)

@app.route('/student/<student_id>')
def student_detail(student_id):
    """View student details"""
    student = db.get_student(student_id)
    if not student:
        return "Student not found", 404
    
    courses = db.get_student_courses(student_id)
    grades = db.get_student_grades(student_id)
    stats = analytics.get_student_statistics(student_id)
    trend = analytics.get_semester_trend(student_id)
    
    return render_template('student_detail.html',
                         student=student,
                         courses=courses,
                         grades=grades,
                         stats=stats,
                         trend=json.dumps(trend))

@app.route('/courses')
def courses_list():
    """View all courses"""
    courses = db.get_all_courses()
    
    # Add statistics for each course
    for course in courses:
        stats = analytics.get_course_statistics(course['course_id'])
        course['avg_grade'] = stats['avg_grade']
        course['student_count'] = stats['student_count']
        course['pass_rate'] = stats['pass_rate']
    
    return render_template('courses.html', courses=courses)

@app.route('/course/<course_id>')
def course_detail(course_id):
    """View course details and grades"""
    course_list = db.get_all_courses()
    course = next((c for c in course_list if c['course_id'] == course_id), None)
    
    if not course:
        return "Course not found", 404
    
    grades = db.get_course_grades(course_id)
    stats = analytics.get_course_statistics(course_id)
    correlation = analytics.analyze_correlation(course_id)
    distribution = analytics.get_grade_distribution(course_id)
    
    return render_template('course_detail.html',
                         course=course,
                         grades=grades,
                         stats=stats,
                         correlation=correlation,
                         distribution=json.dumps(distribution))

@app.route('/analytics')
def analytics_dashboard():
    """Analytics dashboard"""
    courses = db.get_all_courses()
    course_stats = []
    
    for course in courses:
        stats = analytics.get_course_statistics(course['course_id'])
        course_stats.append({
            'course_name': course['course_name'],
            'avg_grade': stats['avg_grade'],
            'student_count': stats['student_count'],
            'pass_rate': stats['pass_rate']
        })
    
    at_risk = analytics.identify_at_risk_students()
    
    return render_template('analytics.html',
                         course_stats=json.dumps(course_stats),
                         at_risk=at_risk)

@app.route('/predictions')
def predictions():
    """Grade prediction interface"""
    return render_template('predictions.html')

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for grade prediction"""
    data = request.json
    midterm = float(data.get('midterm', 0))
    assignments = float(data.get('assignments', 0))
    
    prediction = analytics.predict_final_grade(midterm, assignments)
    
    return jsonify(prediction)

@app.route('/api/grade-distribution/<course_id>')
def api_grade_distribution(course_id):
    """API endpoint for grade distribution"""
    distribution = analytics.get_grade_distribution(course_id)
    return jsonify(distribution)

@app.route('/api/student-trend/<student_id>')
def api_student_trend(student_id):
    """API endpoint for student grade trend"""
    trend = analytics.get_semester_trend(student_id)
    return jsonify(trend)

@app.route('/api/course-stats')
def api_all_course_stats():
    """API endpoint for all course statistics"""
    courses = db.get_all_courses()
    stats = []
    for course in courses:
        course_stats = analytics.get_course_statistics(course['course_id'])
        stats.append({
            'course_id': course['course_id'],
            'course_name': course['course_name'],
            'avg_grade': course_stats['avg_grade'],
            'student_count': course_stats['student_count'],
            'pass_rate': course_stats['pass_rate']
        })
    return jsonify(stats)

@app.route('/api/course-stats/<course_id>')
def api_course_stats(course_id):
    """API endpoint for course statistics"""
    stats = analytics.get_course_statistics(course_id)
    return jsonify(stats)

@app.route('/api/at-risk-students')
def api_at_risk_students():
    """API endpoint for at-risk students"""
    at_risk = analytics.identify_at_risk_students()
    return jsonify(at_risk)

@app.route('/api/top-performers')
def api_top_performers():
    """API endpoint for top performers"""
    top = analytics.get_top_performers(limit=10)
    return jsonify(top)

@app.route('/reports')
def reports():
    """Reports page"""
    students = db.get_all_students()
    courses = db.get_all_courses()
    at_risk = analytics.identify_at_risk_students()
    
    return render_template('reports.html',
                         students=students,
                         courses=courses,
                         at_risk=at_risk)

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    print("=" * 60)
    print("🎓 Student Academic Portal")
    print("=" * 60)
    print("Starting Flask server...")
    print("Open your browser at: http://localhost:5000")
    print("=" * 60)
    
    app.run(debug=True, port=5000, host='0.0.0.0')
