# 🌊 Luồng xử lý dữ liệu (Data Workflow)

Hệ thống của bạn hiện đã chuyển sang mô hình **Dữ liệu Sống (Live Data)**. Dưới đây là cách dữ liệu di chuyển từ trang web PTIT vào ứng dụng của bạn:

## 1. Bắt đầu: Đào dữ liệu (Scraping)
- **File**: `scraper.py`
- **Hành động**: Kết nối tới trang thông báo điểm của Đại học Bắc Duy.
- **Đầu ra**: Danh sách các thông báo thô (Raw text) và link đính kèm.

## 2. Làm đẹp: Lọc & Xử lý (Processing)
- **File**: `data_processor.py`
- **Hành động**: Sử dụng Regex để tách mã môn học, tên lớp và điểm số từ văn bản thô. Chuyển đổi điểm từ dạng chữ sang dạng số (Float).
- **Đầu ra**: Dữ liệu cấu trúc (Structured data).

## 3. Lưu trữ: Persistence
- **File**: `data_persistence.py`
- **Hành động**: Lưu kết quả vào `scraped_data/scraped_data.json` và `.csv`.
- **Mục đích**: Để bạn có thể mở bằng Excel hoặc dùng cho các bước phân tích sau này.

## 4. Tích hợp: Database Sync
- **File**: `pipeline.py` (Mở rộng)
- **Hành động**: Đưa dữ liệu đã lọc vào file `student_tracker.db`. 
- **Đầu ra**: Cập nhật danh sách Students và Grades trong ứng dụng.

## 5. Phân tích: Pandas Analysis
- **File**: `analysis.py`
- **Hành động**: Đọc dữ liệu từ Database/JSON, thực hiện tính toán thống kê (Mean, Median, Max) và tạo biểu đồ.

## 6. Hiển thị: Flask UI
- **File**: `app.py`
- **Hành động**: Lấy dữ liệu từ Database và các biểu đồ đã tạo để hiển thị lên trình duyệt tại `http://localhost:5000`.

---

### 🚀 Cách chạy nhanh:
1. Chạy `app.py` -> Truy cập trình duyệt.
2. Nhấn nút **"Start Scraping Pipeline"** trên giao diện Web.
3. Toàn bộ các bước trên sẽ tự động thực hiện.
