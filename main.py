from data_loader import load_projects, load_experts
from preprocessor import preprocess_text
from embedder import get_embeddings
from similarity_calculator import calculate_similarity, apply_filters, visualization
from interface import run_interface
import pandas as pd

# Загрузка данных
projects_df = load_projects('project_report_1.csv')
experts_df = load_experts('users_report.csv')

# Предобработка
projects_df['processed_text'] = projects_df['text_for_analysis'].apply(preprocess_text)
experts_df['processed_text'] = experts_df['text_for_analysis'].apply(preprocess_text)

# Экспорт в CSV для анализа
projects_df[['id', 'processed_text']].to_csv('aftermath/processed_projects.csv', index=False)
experts_df[['id', 'processed_text']].to_csv('aftermath/processed_experts.csv', index=False)

# Векторизация
project_embeddings = get_embeddings(projects_df)
expert_embeddings = get_embeddings(experts_df)

# Сходство
similarities = calculate_similarity(project_embeddings, expert_embeddings)
similarity_df = pd.DataFrame(similarities * 100, index=projects_df['id'], columns=experts_df['id'])

visualization(similarity_df, 'Компетентность экспертов для проектов (без фильтра) (%)')

# Фильтры
similarity_df = apply_filters(similarity_df, projects_df, experts_df)
visualization(similarity_df, 'Компетентность экспертов для проектов с применением фильтра (%)')

# Запуск интерфейса
run_interface(similarity_df, experts_df, projects_df)