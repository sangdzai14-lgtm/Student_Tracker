"""
🧠 ACADEMIC INTELLIGENCE ENGINE: Behavioral Logic & Analysis
------------------------------------------------------------
Module này định nghĩa các quy tắc (heuristics) để hệ thống nhận diện
thái độ và hành vi học tập của sinh viên dựa trên dữ liệu đa chiều.
"""

from typing import Dict, List

def analyze_student_behavior(data: Dict) -> Dict:
    """
    Phân tích hành vi dựa trên sự tương quan giữa Chuyên cần, Bài tập và Điểm số.
    """
    # 1. Nhận diện "Nghịch lý năng lực" (High Score, Low Effort)
    # Dành cho những học sinh có tư duy tốt nhưng thái độ chưa chuyên cần.
    is_talented_but_lazy = data['predicted_grade'] > 8.0 and data['attendance'] < 70

    # 2. Nhận diện "Lỗ hổng nỗ lực" (High Attendance, Low Results)
    # Dành cho học sinh chăm chỉ nhưng phương pháp học chưa hiệu quả.
    is_hardworking_struggler = data['attendance'] > 90 and data['predicted_grade'] < 5.0

    # 3. Nhận diện "Nguy cơ bỏ học/Burnout" (Drop in all metrics)
    is_critical_engagement = data['assignments'] < 3.0 and data['attendance'] < 50

    # Tổng hợp phân tích
    analysis = {
        "behavior_tags": [],
        "risk_assessment": "Stable",
        "strategy": "Duy trì lộ trình hiện tại."
    }

    if is_talented_but_lazy:
        analysis["behavior_tags"].append("PHANTOM_EXCELLENCE")
        analysis["risk_assessment"] = "Observation Required"
        analysis["strategy"] = "Kiểm tra tính trung thực hoặc dấu hiệu chủ quan."

    elif is_hardworking_struggler:
        analysis["behavior_tags"].append("COGNITIVE_BARRIER")
        analysis["risk_assessment"] = "Support Recommended"
        analysis["strategy"] = "Thay đổi phương pháp học tập, bổ trợ kiến thức nền."

    elif is_critical_engagement:
        analysis["behavior_tags"].append("DISENGAGEMENT_CRITICAL")
        analysis["risk_assessment"] = "High Alert"
        analysis["strategy"] = "Can thiệp tâm lý hoặc liên hệ trực tiếp gia đình."

    return analysis

# --- Phân tích xu hướng (Trend Analysis) ---
def evaluate_performance_pulse(history: List[float]) -> str:
    """Đánh giá 'nhịp xung' phong độ qua các kỳ học."""
    if len(history) < 2: return "Initial State"

    diff = history[-1] - history[0]
    if diff > 1.5: return "Strong Growth"
    if diff < -1.5: return "Significant Decline"
    return "Consistently Stable"
