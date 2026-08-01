"""
🌊 DATA ORCHESTRATOR v9.0: Local Intelligence Sync
--------------------------------------------------
- Pivot: Offline University Data Sync.
- Features: Automatic Matplotlib chart generation on setup.
- Population: Fixed 100 students of Bac Duy University.
"""
import logging
from typing import List, Dict, Any
from scraper import BacDuyUniversityScraper
from data_persistence import DataPersistence
from database import Database
from analytics import GradeAnalytics

logger = logging.getLogger(__name__)

class DataPipeline:
    def __init__(self, db_path: str = 'student_tracker.db'):
        self.scraper = BacDuyUniversityScraper()
        self.persistence = DataPersistence()
        self.db = Database(db_path)
        self.analytics = GradeAnalytics(self.db)

    def run_complete_pipeline(self, url: str = None, sync_to_db: bool = True) -> Dict:
        results = {'success': False}
        try:
            # 1. Scrape
            all_subject_nodes = self.scraper.scrape_all_academic_records()
            results['raw_records_count'] = len(all_subject_nodes)

            # 2. Local Sync
            if sync_to_db:
                self.db.clear_all_data()
                self.db.batch_upsert_students(self.scraper.fixed_student_pool)

                total = 0
                all_flat = []

                for node in all_subject_nodes:
                    self.db.add_course(node['course_id'], node['course_name'], 4, "INST_BD", node['year'], node['semester'])
                    node_grades = []
                    for stu in node['students']:
                        g = {"student_id": stu['student_id'], "course_id": node['course_id'], "midterm": stu['midterm'], "final": stu['final'], "assignments": stu['assignments'], "attendance": stu['attendance'], "final_grade": stu['final_grade'], "letter_grade": stu['letter_grade']}
                        node_grades.append(g)
                        row = stu.copy(); row.update({'course_name': node['course_name'], 'course_id': node['course_id'], 'academic_year': node['year'], 'semester': node['semester']})
                        all_flat.append(row); total += 1
                    self.db.batch_upsert_grades(node_grades)

                results['processed_records_count'] = total
                self.persistence.save_both(all_flat)

                # 3. AI & Visual Training
                self.analytics.train_advanced_model()
                self.analytics.create_visualizations()

                results['success'] = True
            return results
        except Exception as e:
            logger.error(f"Local Sync Error: {e}")
            results['error'] = str(e); return results
