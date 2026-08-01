"""
🚀 LOCAL CORE ENGINE v10.2: longitudinal Analysis Node
--------------------------------------------------
- Pivot: Replaced Supabase with Local SQLite.
- Evolution: Multi-year subject tracking and Cohort mapping.
- Visuals: On-demand Matplotlib generation for course details.
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for, send_file
from database import Database
from analytics import GradeAnalytics, VisualizationData
from ai_agents import AIAgentOrchestrator
from pipeline import DataPipeline
from data_persistence import DataPersistence
import json
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'local_academic_intel_2026'

db = Database('student_tracker.db')
analytics = GradeAnalytics(db)
agents = AIAgentOrchestrator()
viz_data = VisualizationData(analytics)
pipeline = DataPipeline()
persistence = DataPersistence()

@app.route('/')
def index():
    students = db.get_all_students()
    all_courses = db.get_all_courses()
    unique_subject_names = list(set(c['course_name'].split(' (')[0] for c in all_courses))
    total_subjects = len(unique_subject_names)
    has_data = len(students) > 0
    at_risk = analytics.identify_at_risk_students() if has_data else []
    top_performers = analytics.get_top_performers(limit=5) if has_data else []
    years = sorted(list(set(c['academic_year'] for c in all_courses))) if has_data else []
    return render_template('index.html', total_students=len(students), total_courses=total_subjects, at_risk_count=len(at_risk), top_performers=top_performers, has_data=has_data, available_years=years)

@app.route('/students')
def students_list():
    students = db.get_all_students()
    for s in students: s['gpa'] = db.get_student_gpa(s['student_id'])
    return render_template('students.html', students=students)

@app.route('/student/<student_id>')
def student_detail(student_id):
    student = db.get_student(student_id)
    if not student: return "Entity missing", 404
    grades = db.get_student_grades(student_id)
    stats = analytics.get_student_statistics(student_id)
    trend = analytics.get_semester_trend(student_id)
    return render_template('student_detail.html', student=student, grades=grades, stats=stats, trend=json.dumps(trend))

@app.route('/courses')
def courses_list():
    sel_year = request.args.get('year')
    sel_sem = request.args.get('semester', type=int)
    all_raw = db.get_all_courses()
    unique_years = sorted(list(set(c['academic_year'] for c in all_raw)), reverse=True)
    display_courses = []
    seen = set()
    if not sel_year and not sel_sem:
        for c in sorted(all_raw, key=lambda x: (x['academic_year'], x['semester']), reverse=True):
            base = c['course_name'].split(' (')[0]
            if base not in seen:
                st = analytics.get_course_statistics(c['course_id'])
                c_copy = dict(c)
                c_copy.update({'avg_grade': st['avg_grade'], 'student_count': st['student_count'], 'pass_rate': st['pass_rate'], 'display_name': base})
                display_courses.append(c_copy)
                seen.add(base)
    else:
        filtered = db.get_all_courses(sel_year, sel_sem)
        for c in filtered:
            st = analytics.get_course_statistics(c['course_id'])
            c_copy = dict(c)
            # Ensure display_name is present even when filtered
            base = c['course_name'].split(' (')[0]
            c_copy.update({'avg_grade': st['avg_grade'], 'student_count': st['student_count'], 'pass_rate': st['pass_rate'], 'display_name': base})
            display_courses.append(c_copy)
    return render_template('courses.html', courses=display_courses, years=unique_years, sel_year=sel_year, sel_sem=sel_sem)

@app.route('/course/<course_id>')
def course_detail(course_id):
    all_c = db.get_all_courses()
    target = next((c for c in all_c if c['course_id'] == course_id), None)
    if not target: return "Module missing", 404

    # 🔑 FIX: Robust historical mapping (Match by Code or Base Name)
    # Extracts 'AI101' from 'AI101_K21_2021_2022_S1'
    subject_code = target['course_id'].split('_')[0]
    base_name = target['course_name'].split(' (')[0]

    # Match courses that share the same subject code OR name prefix
    history = [c for c in all_c if c['course_id'].startswith(subject_code) or c['course_name'].startswith(base_name)]

    history_stats = []
    for h in history:
        st = analytics.get_course_statistics(h['course_id'])
        history_stats.append({
            'year': h['academic_year'],
            'semester': h['semester'],
            'avg': st['avg_grade'],
            'id': h['course_id'],
            'cohort': h['course_name'].split('(')[1].split(')')[0] if '(' in h['course_name'] else '?'
        })

    # Sort history chronologically
    history_stats.sort(key=lambda x: (x['year'], x['semester']))

    # 📊 NEW: Generate Course Distribution Chart (Matplotlib)
    dist_img = analytics.generate_course_distribution_chart(course_id)

    return render_template('course_detail.html',
                         course=target,
                         grades=db.get_course_grades(course_id),
                         stats=analytics.get_course_statistics(course_id),
                         correlation=analytics.analyze_correlation(course_id),
                         distribution_json=json.dumps(analytics.get_grade_distribution(course_id)),
                         history_json=json.dumps(history_stats),
                         history_stats=history_stats,
                         matplotlib_chart=dist_img)

@app.route('/analysis')
def analytics_dashboard():
    at_risk = analytics.identify_at_risk_students()
    return render_template('analytics.html', at_risk=at_risk)

@app.route('/intelligence')
def intelligence_dashboard(): return render_template('behavior_analysis.html')

@app.route('/predictions')
def predictions(): return render_template('predictions.html')

@app.route('/presentation')
def presentation(): return render_template('presentation.html')

@app.route('/scraper')
def scraper_page(): return render_template('scraper.html')

@app.route('/api/scrape', methods=['POST'])
def api_scrape():
    try:
        results = pipeline.run_complete_pipeline(sync_to_db=True)
        if results['success']:
            analytics.train_advanced_model()
            analytics.create_visualizations()
            return jsonify({'status': 'success', 'processed_records': results.get('processed_records_count', 0)}), 200
        return jsonify({'status': 'error', 'message': results.get('error')}), 400
    except Exception as e: return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        data = request.json
        prediction = analytics.predict_with_neural_risk(float(data.get('midterm', 7.0)), float(data.get('attendance', 100)), float(data.get('assignments', 8.0)))
        return jsonify({**prediction, **agents.get_neural_reasoning(data, prediction)})
    except Exception as e: return jsonify({'error': str(e)}), 500

@app.route('/api/at-risk-report', methods=['GET'])
def api_at_risk_report(): return jsonify(analytics.identify_at_risk_students())

@app.route('/api/intelligence/behavioral', methods=['GET'])
def api_intelligence_behavioral():
    all_s = db.get_all_students()
    proc = []
    for s in all_s:
        st = analytics.get_student_statistics(s['student_id'])
        s_d = dict(s); s_data = dict(s); s_d.update({'gpa': st['gpa'], 'attendance': st['attendance'], 'assignments': st.get('assignments', 8)})
        proc.append(s_d)
    return jsonify(agents.get_behavioral_categories(proc))

@app.route('/static/visualizations/<filename>')
def serve_viz(filename):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'visualizations', filename)
    if os.path.exists(path): return send_file(path)
    return "File Missing", 404

if __name__ == '__main__':
    os.makedirs('static/visualizations', exist_ok=True)
    app.run(debug=True, port=5000, host='0.0.0.0', use_reloader=False)
