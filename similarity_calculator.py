from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def calculate_similarity(project_embeddings, expert_embeddings):
    similarities = cosine_similarity(project_embeddings, expert_embeddings)
    similarities = np.clip(similarities, 0, 1)
    return similarities


def apply_filters(similarity_df, projects_df, experts_df):
    for project_id in similarity_df.index:
        project_city = projects_df.loc[projects_df['id'] == project_id, 'Город'].iloc[0]
        project_company = \
        projects_df.loc[projects_df['id'] == project_id, 'Наименование места работы / учебы, должность'].iloc[0]
        project_text = projects_df.loc[projects_df['id'] == project_id, 'processed_text'].iloc[0]

        for expert_id in similarity_df.columns:
            expert_city = experts_df.loc[experts_df['id'] == expert_id, 'Населенный пункт'].iloc[0]
            expert_company = experts_df.loc[experts_df['id'] == expert_id, 'Компания'].iloc[0]
            expert_software = experts_df.loc[experts_df['id'] == expert_id, 'Знание специализированных программ'].iloc[
                0]

            if pd.notna(project_company) and pd.notna(expert_company):
                if project_company.lower() in expert_company.lower() or expert_company.lower() in project_company.lower():
                    similarity_df.loc[project_id, expert_id] = 0

            if pd.notna(project_city) and pd.notna(expert_city) and project_city == expert_city:
                similarity_df.loc[project_id, expert_id] *= 1.05

            if pd.notna(
                    expert_software) and 'нейросеть' in expert_software.lower() and 'нейросеть' in project_text.lower():
                similarity_df.loc[project_id, expert_id] *= 1.10
    return similarity_df

def visualization(similarity_df, caption):
    plt.figure(figsize=(10, 8))
    sns.heatmap(similarity_df, cmap='YlGnBu')
    plt.title(caption)
    plt.xlabel('ID эксперта')
    plt.ylabel('ID проекта')
    plt.show()