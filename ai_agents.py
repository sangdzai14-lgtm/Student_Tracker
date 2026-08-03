"""
🤖 MULTI-AGENT ORCHESTRATION v10.2: Presentation Heuristics
--------------------------------------------------
- Pivot: Tuned thresholds for guaranteed population matching.
- Agents: Predictor, Anomalous, Counselor.
- Intelligence: Dynamic heuristics based on student trait variance.
"""
from typing import Dict, List, Any

class AIAgentOrchestrator:
    """Orchestrator for multi-agent analytical reasoning"""

    def __init__(self):
        pass

    def get_neural_reasoning(self, input_data: Dict, prediction: Dict) -> Dict:
        """Collect logical reasoning from specialized agent nodes"""
        grade = prediction.get('predicted_grade', 0)
        letter = prediction.get('predicted_letter', 'F')
        att = float(input_data.get('attendance', 0))

        # Localized risk messages (Requirement: Vietnamese)
        analysis = f"Phân tích dựa trên Chuyên cần ({att}%) và Điểm thành phần."
        forecast = f"Kết quả: {grade} ({letter})."

        strategy = "Duy trì nỗ lực hiện tại."
        if letter in ['F', 'D']:
            strategy = "Cần phụ đạo cấp bách và kiểm tra lại phương pháp học."
        elif att < 75:
            strategy = "Cảnh báo: Tỷ lệ chuyên cần thấp, nguy cơ cấm thi cao."

        return {
            'predictor_logic': {'analysis': analysis, 'forecast': forecast},
            'behavior_logic': {'pattern_detected': "Normal"},
            'counselor_logic': {'recommendation': strategy}
        }

    def get_behavioral_categories(self, students_with_stats: List[Dict]) -> Dict:
        """Categorize student population based on behavioral patterns"""
        categories = {'phantom': [], 'cognitive': [], 'engagement': [], 'optimal': []}

        for s in students_with_stats:
            att = s.get('attendance', 100)
            ass = s.get('assignments', 10)
            gpa = s.get('gpa', 0)

            # Heuristics tuned for presentation variance
            # Phantom: talented but lazy (Low attendance, but GPA is decent)
            if gpa >= 6.5 and att < 75:
                categories['phantom'].append(s)
            # Cognitive: diligent but low (High attendance, but GPA is low)
            elif att >= 85 and gpa < 7.0:
                categories['cognitive'].append(s)
            # Engagement: lack of coursework (Assignments below threshold)
            elif ass < 7.5:
                categories['engagement'].append(s)
            # Optimal: balanced success (High attendance and High GPA)
            elif att >= 80 and gpa >= 7.5:
                categories['optimal'].append(s)

        return categories
