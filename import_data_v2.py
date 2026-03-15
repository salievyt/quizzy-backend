import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from questions.models import Category, Question

categories_data = [
    {
        "id": 1,
        "name": "Логическая",
        "description": "Это не просто вопросы - это челлендж для твоего интеллекта. Проверь, насколько ты умеешь анализировать, сравнивать и находить скрытые решения.",
        "icon_url": "/assets/icons/LOGIC_ICON.png",
        "image_url": "https://i.ibb.co/k2fJzLgx/logic.jpg"
    },
    {
        "id": 2,
        "name": "Geeks",
        "description": "Тут вопросы про нашу академию - На сколько ты знаешь академию Geeks и разные направления IT",
        "icon_url": "/assets/icons/GEEKS_ICON.png",
        "image_url": "https://i.ibb.co/TxcY9GVk/Geeks.jpg"
    },
    {
        "id": 3,
        "name": "Для детей",
        "description": "Весёлые задачки, которые помогут тебе думать быстрее и находить правильные решения!",
        "icon_url": "/assets/icons/JUNIOR_ICON.png",
        "image_url": "https://i.ibb.co/zWPLDptZ/jun.jpg"
    },
    {
        "id": 4,
        "name": "Основы ислама",
        "description": "Думаешь, знаешь всё про пять столпов, пророков и важные события? Проверим. Эта категория не скучная теория, а лёгкий и понятный квиз.",
        "icon_url": "/assets/icons/ISLAM_ICON.png",
        "image_url": "assets/images/islam.jpg"
    },
    {
        "id": 5,
        "name": "Дизайнер века",
        "description": "Эта категория про культовых дизайнеров, бренды, креатив, стиль и решения, которые изменили визуальный мир.",
        "icon_url": "/assets/icons/DESIGNER_ICON.png",
        "image_url": "assets/images/designer.jpg"
    },
    {
        "id": 6,
        "name": "Космос",
        "description": "Любишь звёзды, планеты и всё, что летает быстрее интернета? Проверим, космический ли у тебя мозг?",
        "icon_url": "/assets/icons/COSMOS_ICON.png",
        "image_url": "assets/images/cosmos.jpg"
    },
    {
        "id": 7,
        "name": "Наука",
        "description": "Наука - это не скучные формулы, а способ понимать реальность. Проверим, насколько ты будущий учёный.",
        "icon_url": "/assets/icons/SCIENCE_ICON.png",
        "image_url": "assets/images/science.jpg"
    },
    {
        "id": 8,
        "name": "Социальные сети",
        "description": "Скроллишь каждый день? Тогда пора узнать, что стоит за лайками и алгоритмами.",
        "icon_url": "/assets/icons/SOCIALMEDIA_ICON.png",
        "image_url": "assets/images/socialMedia.jpg"
    },
    {
        "id": 9,
        "name": "История",
        "description": "Провери, насколько хорошо ты знаешь прошлое человечества — от древних цивилизаций до современных событий.",
        "icon_url": "/assets/icons/HISTORY_ICON.png",
        "image_url": "assets/images/history.jpg"
    },
    {
        "id": 10,
        "name": "Музыка",
        "description": "Узнай, насколько ты шаришь в хитах, артистах и музыкальных трендах.",
        "icon_url": "/assets/icons/MUSIC_ICON.png",
        "image_url": "assets/images/music.jpg"
    },
    {
        "id": 11,
        "name": "География",
        "description": "Проверь, сможешь ли ты найти любую точку на карте без Google Maps.",
        "icon_url": "/assets/icons/GEOGRAPHY_ICON.png",
        "image_url": "assets/images/geography.jpg"
    },
    {
        "id": 12,
        "name": "Speed RUN",
        "description": "SPEED RUN MODE",
        "icon_url": "/assets/icons/SPEED_RUN.png",
        "image_url": "assets/images/speedRun.png"
    }
]

questions_data = [
    {"cat_id": 1, "text": "Что будет следующим числом: 2, 4, 8, 16, ?", "options": ["32", "24", "18", "30"], "correct_index": 0},
    {"cat_id": 1, "text": "Продолжи ряд: 1, 1, 2, 3, 5, ?", "options": ["8", "6", "7", "10"], "correct_index": 0},
    {"cat_id": 1, "text": "У Маши 5 яблок, а у Пети на 2 больше. Сколько яблок у Пети?", "options": ["7", "3", "10", "5"], "correct_index": 0},
    {"cat_id": 2, "text": "Где находится главный офис Geeks в Бишкеке?", "options": ["Ибраимова 103", "Чуй 12", "Манаса 5", "Киевская 77"], "correct_index": 0},
    {"cat_id": 2, "text": "Какое направление НЕ преподают в Geeks?", "options": ["Алхимия", "Frontend", "Backend", "iOS"], "correct_index": 0},
    {"cat_id": 3, "text": "Какого цвета небо в солнечный день?", "options": ["Голубое", "Зеленое", "Красное", "Черное"], "correct_index": 0},
    {"cat_id": 3, "text": "Сколько лапок у паука?", "options": ["8", "6", "4", "10"], "correct_index": 0},
    {"cat_id": 4, "text": "Сколько столпов ислама?", "options": ["5", "3", "7", "1"], "correct_index": 0},
    {"cat_id": 6, "text": "Какая планета самая большая в Солнечной системе?", "options": ["Юпитер", "Марс", "Земля", "Сатурн"], "correct_index": 0},
    {"cat_id": 7, "text": "Сколько в среднем зубов у взрослого человека?", "options": ["32", "28", "36", "24"], "correct_index": 0},
    {"cat_id": 9, "text": "Кто был первым человеком в космосе?", "options": ["Юрий Гагарин", "Нил Армстронг", "Илон Маск", "Валентина Терешкова"], "correct_index": 0},
    {"cat_id": 11, "text": "Какая страна самая большая в мире по территории?", "options": ["Россия", "Канада", "Китай", "США"], "correct_index": 0},
]

# Cleanup existing
Question.objects.all().delete()
Category.objects.all().delete()

# Create Categories
cat_map = {}
for c_data in categories_data:
    cat = Category.objects.create(
        id=c_data["id"],
        name=c_data["name"],
        description=c_data["description"],
        icon_url=c_data["icon_url"],
        image_url=c_data["image_url"]
    )
    cat_map[c_data["id"]] = cat

# Create Questions
for q_data in questions_data:
    Question.objects.create(
        category=cat_map[q_data["cat_id"]],
        text=q_data["text"],
        options=q_data["options"],
        correct_index=q_data["correct_index"]
    )

print(f"Successfully imported {len(categories_data)} categories and {len(questions_data)} questions.")
