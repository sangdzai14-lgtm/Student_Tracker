import os
import sys
from pathlib import Path

# Thêm thư mục gốc vào PYTHONPATH để có thể import các module
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

def main():
    print("=" * 70)
    print("🌟 KHỞI ĐỘNG DỰ ÁN STUDENT TRACKER PORTAL (LIVE EDITION)")
    print("=" * 70)

    # 1. Thiết lập biến môi trường để xóa và tải lại dữ liệu mới
    os.environ['RELOAD_DATA'] = '1'

    print("\n[1/2] Đang khởi động Server Flask...")
    print("      Lưu ý: Quá trình này sẽ tự động chạy Pipeline để đào dữ liệu mới.")
    print("      Vui lòng chờ trong giây lát...\n")

    # 2. Chạy file app.py (Tắt reloader để tránh lỗi socket WinError 10038)
    try:
        from app import app
        app.run(debug=True, port=5000, host='0.0.0.0', use_reloader=False)
    except ImportError as e:
        print(f"❌ Lỗi: Không tìm thấy module cần thiết. {e}")
        print("💡 Hãy đảm bảo bạn đã cài đặt các thư viện trong requirements.txt")
    except Exception as e:
        print(f"❌ Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    main()
