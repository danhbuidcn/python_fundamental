# TOEIC Vocabulary MindMap Generator

## Giới thiệu

**TOEIC Vocabulary MindMap Generator** là một ứng dụng Python giúp tự động hóa việc lấy dữ liệu từ API chứa các từ vựng TOEIC và tạo sơ đồ tư duy (mind map) cho các từ vựng theo từng chủ đề. Sơ đồ tư duy sẽ giúp bạn dễ dàng học và ghi nhớ các từ vựng và câu ví dụ đi kèm.

## Các tính năng chính

- Lấy dữ liệu từ API bao gồm danh sách bài học và các từ vựng tương ứng.
- Lọc và xử lý dữ liệu để tổ chức các từ vựng theo chủ đề.
- Tạo sơ đồ tư duy cho từng bài học với các từ vựng và câu ví dụ.
- Xuất sơ đồ tư duy thành hình ảnh định dạng PNG.

## Cài đặt

### Yêu cầu

- Python 3.6+
- `pip` để quản lý thư viện Python
- Các thư viện Python:
  - `requests`
  - `pandas`
  - `anytree`
  - `graphviz`
- Phần mềm Graphviz (tải tại [Graphviz.org](https://graphviz.org/download/))

### Hướng dẫn cài đặt

1. **Clone project từ GitHub**:

   ```bash
   git clone https://github.com/your-username/toeic-vocabulary-mindmap-generator.git
   cd mindmap_generator
   ```

2. **Cài đặt các thư viện yêu cầu**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Cài đặt phần mềm Graphviz** (nếu tạo mind map):

  Tải Graphviz tại [Graphviz Download](https://graphviz.org/download/) và cài đặt theo hướng dẫn.
  run `dot -V` to verify

## Hướng dẫn sử dụng

1. Tạo sơ đồ tư duy (Mind Map)
   ```bash
   python mindmap_generator.py
   ```

2. Xuất dữ liệu từ vựng ra file Excel
   ```bash
   python xlsx_generator.py
   ```
