"""
🕷️ INTELLIGENCE EXTRACTOR v8.0: Final Unified Data Node
--------------------------------------------------
- Pivot: Solidifies 5 distinct cohorts (K21 -> K25).
- Structure: Guaranteed unique subject naming (No duplication).
- Reality: Fixed student population with persistent academic traits.
"""
import random
import unicodedata
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

class BacDuyUniversityScraper:
    """Scraper node for generating high-fidelity academic datasets"""

    def __init__(self):
        self.base_url = "https://truong-dai-hoc-bac-duy-thai-nguyen-diem.lovable.app/"
        self.subjects_meta = [
            {"code": "AI101", "name": "Toán cho AI (Đại số & Giải tích)"},
            {"code": "AI102", "name": "Xác suất & Thống kê ứng dụng"},
            {"code": "AI103", "name": "Lập trình Python cho Khoa học dữ liệu"},
            {"code": "AI104", "name": "Cấu trúc dữ liệu & Giải thuật"},
            {"code": "AI201", "name": "Machine Learning (Học máy)"},
            {"code": "AI202", "name": "Deep Learning (Học sâu)"},
            {"code": "AI203", "name": "Computer Vision (Thị giác máy tính)"},
            {"code": "AI204", "name": "Natural Language Processing (NLP)"},
            {"code": "AI301", "name": "Reinforcement Learning"},
            {"code": "AI302", "name": "Big Data & Cloud Computing"},
            {"code": "AI303", "name": "Đạo đức & Pháp luật trong AI"},
            {"code": "AI401", "name": "Đồ án chuyên ngành AI (MLOps)"}
        ]

        self.cohorts = {
            "K21": self._generate_cohort("BD21AI", 40),
            "K22": self._generate_cohort("BD22AI", 40),
            "K23": self._generate_cohort("BD23AI", 40),
            "K24": self._generate_cohort("BD24AI", 40),
            "K25": self._generate_cohort("BD25AI", 40)
        }
        self.fixed_student_pool = []
        for c in self.cohorts.values():
            self.fixed_student_pool.extend(c)

    def _remove_accents(self, input_str):
        """Normalize string to remove Vietnamese accents for technical fields"""
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

    def _generate_cohort(self, prefix: str, count: int) -> List[Dict]:
        """Generate a unique set of student identities for a specific cohort"""
        pool = []
        v_first = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ", "Võ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý"]
        v_middle = ["Văn", "Thị", "Minh", "Đức", "Thanh", "Anh", "Xuân", "Hải", "Tuấn", "Thành", "Quang", "Ngọc", "Kim", "Hữu"]
        v_last = ["An", "Bình", "Cường", "Dũng", "Hùng", "Kiên", "Linh", "Minh", "Nam", "Phúc", "Quân", "Sơn", "Tùng", "Vinh", "Hà", "Lợi"]
        for i in range(count):
            sid = f"{prefix}{i+1:03d}"
            name = f"{random.choice(v_first)} {random.choice(v_middle)} {random.choice(v_last)}"
            clean = self._remove_accents(name).lower().replace(" ", "")
            email = f"{clean}{sid.lower()}@gmail.com"
            pool.append({
                'student_id': sid,
                'name': name,
                'email': email,
                'major': f"Khoa AI - Khóa {prefix[2:4]}",
                'trait': random.choice(['excellent', 'talented_but_lazy', 'diligent_but_low', 'struggling', 'average'])
            })
        return pool

    def scrape_all_academic_records(self) -> List[Dict[str, Any]]:
        """Map curriculum structure to academic years and semesters"""
        all_records = []
        years = ["2021/2022", "2022/2023", "2023/2024", "2024/2025", "2025/2026"]

        for year in years:
            y_start = int(year.split('/')[0])
            for cohort_name, students in self.cohorts.items():
                c_start = int(f"20{cohort_name[1:3]}")
                level = y_start - c_start + 1

                if 1 <= level <= 4:
                    level_subjects = [s for s in self.subjects_meta if s['code'].startswith(f"AI{level}")]
                    for sem in [1, 2]:
                        # Balance subjects across semesters
                        sub_pool = level_subjects[:len(level_subjects)//2] if sem == 1 else level_subjects[len(level_subjects)//2:]

                        for sub in sub_pool:
                            course_id = f"{sub['code']}_{cohort_name}_{year.replace('/', '_')}_S{sem}"
                            all_records.append({
                                'course_id': course_id,
                                'course_code': sub['code'],
                                'course_name': f"{sub['name']} ({cohort_name})",
                                'year': year,
                                'semester': sem,
                                'students': self._generate_grades(students)
                            })
        return all_records

    def _generate_grades(self, student_pool: List[Dict]) -> List[Dict]:
        """Synthesize performance data based on individual student traits"""
        students = []
        for stu in student_pool:
            t = stu['trait']
            if t == 'excellent':
                att, ass, mid, final = random.uniform(94,100), random.uniform(9.4,10), random.uniform(9,10), random.uniform(9,10)
            elif t == 'talented_but_lazy':
                att, ass, mid, final = random.uniform(40,65), random.uniform(7,9.2), random.uniform(8.5,10), random.uniform(8.5,10)
            elif t == 'diligent_but_low':
                att, ass, mid, final = random.uniform(96,100), random.uniform(9,10), random.uniform(3,5.5), random.uniform(3,5.5)
            elif t == 'struggling':
                att, ass, mid, final = random.uniform(40,75), random.uniform(2,5), random.uniform(1.5,4.5), random.uniform(1,4.5)
            else:
                att, ass, mid, final = random.uniform(70,95), random.uniform(6.5,8.8), random.uniform(5.5,8), random.uniform(5,8)

            fg = round(((att/10)*0.2) + (ass*0.3) + (final*0.5), 1)
            letter = 'F'
            if fg >= 8.5: letter = 'A'
            elif fg >= 7.0: letter = 'B'
            elif fg >= 5.5: letter = 'C'
            elif fg >= 4.0: letter = 'D'

            rec = stu.copy()
            rec.update({'midterm': round(mid,1), 'final': round(final,1), 'assignments': round(ass,1), 'attendance': round(att,1), 'final_grade': fg, 'letter_grade': letter})
            students.append(rec)
        return students

# Deprecated/Compatibility Wrappers
class PTITScraper(BacDuyUniversityScraper): pass
class BacSonScraper(BacDuyUniversityScraper): pass
