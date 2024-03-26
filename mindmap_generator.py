from anytree import Node, RenderTree
from anytree.exporter import DotExporter
import pandas as pd

# Dữ liệu bài học mẫu
lessons = [
    {'id': 1, 'title': 'Economics'},
    {'id': 2, 'title': 'Commerce P1'}
]

# Dữ liệu từ vựng mẫu
all_words = [
    {'lesson_title': 'Economics', 'content': 'project', 'trans': 'Dự án', 'sentence1': 'The project is ongoing.', 'vi_sentence1': 'Dự án đang diễn ra.'},
    {'lesson_title': 'Economics', 'content': 'economy', 'trans': 'Kinh tế', 'sentence1': 'The global economy is improving.', 'vi_sentence1': 'Kinh tế toàn cầu đang cải thiện.'},
    {'lesson_title': 'Commerce P1', 'content': 'trade', 'trans': 'Thương mại', 'sentence1': 'Trade between nations is important.', 'vi_sentence1': 'Thương mại giữa các quốc gia rất quan trọng.'}
]

# Chuyển đổi all_words thành DataFrame để sử dụng trong generate_mind_map
df_words_filtered = pd.DataFrame(all_words)

# Hàm tạo sơ đồ tư duy (mind map)
def generate_mind_map(lessons, df_words_filtered):
    root = Node("TOEIC Vocabulary")

    # Group words by lesson
    grouped = df_words_filtered.groupby('lesson_title')

    for lesson in lessons:
        # Tạo một node cho mỗi bài học
        lesson_node = Node(lesson['title'], parent=root)
        
        # Kiểm tra xem bài học có từ vựng nào không
        if lesson['title'] in grouped.groups:
            lesson_words = grouped.get_group(lesson['title'])
            
            for _, row in lesson_words.iterrows():
                # Tạo một node cho mỗi từ vựng trong bài học
                word_node = Node(f"{row['content']} ({row['trans']})", parent=lesson_node)
                # Thêm câu ví dụ làm node con của từ vựng
                example_node = Node(f"Example: {row['vi_sentence1']}", parent=word_node)

    # Xuất sơ đồ tư duy thành file hình ảnh
    DotExporter(root).to_picture("mindmap_sample.svg")
    print("Mind map generated successfully!")

# Gọi hàm để tạo mind map từ dữ liệu mẫu
generate_mind_map(lessons, df_words_filtered)
