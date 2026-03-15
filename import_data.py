import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from questions.models import Question

questions_data = [
    {"category_id": 1, "text": "Что будет следующим числом: 2, 4, 8, 16, ?", "options": ["32", "24", "18", "30"], "correct_index": 0},
    {"category_id": 1, "text": "Продолжи ряд: 1, 1, 2, 3, 5, ?", "options": ["8", "6", "7", "10"], "correct_index": 0},
    {"category_id": 2, "text": "Где находится главный офис Geeks?", "options": ["Бишкек", "Алматы", "Нур-Султан", "Ош"], "correct_index": 0},
    {"category_id": 3, "text": "Сколько будет 2+2?", "options": ["4", "5", "3", "6"], "correct_index": 0},
]

for q in questions_data:
    Question.objects.create(**q)

print(f"Successfully imported {len(questions_data)} dummy questions.")
