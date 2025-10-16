
import pandas as pd

def get_top_experts(project_id, similarity_df, experts_df, projects_df, top_n=5):
    if project_id not in similarity_df.index:
        return f"Проект с ID {project_id} не найден."

    scores = similarity_df.loc[project_id]

    if isinstance(scores, pd.DataFrame):
        scores = scores.iloc[0]

    top_experts = scores.sort_values(ascending=False).head(top_n)

    result = []
    project_row = projects_df[projects_df['id'] == project_id]
    project_description = project_row['Краткое описание проекта'].iloc[
        0] if not project_row.empty else "Описание не найдены"

    for expert_id, score in top_experts.items():
        expert_row = experts_df[experts_df['id'] == expert_id]
        qualifications = expert_row['text_for_analysis'].iloc[0] if not expert_row.empty else 'Данные не найдены'
        result.append({
            'expert_id': expert_id,
            'score': score,
            'qualifications': qualifications
        })

    return result, project_description


def get_top_projects(similarity_df, projects_df, top_n=5):
    avg_scores = similarity_df.mean(axis=1)
    top_projects = avg_scores.sort_values(ascending=False).head(top_n)

    result = []
    for project_id, avg_score in top_projects.items():
        project_row = projects_df[projects_df['id'] == project_id]
        description = project_row['Краткое описание проекта'].iloc[
            0] if not project_row.empty else 'Описание не найдено'
        result.append({
            'project_id': project_id,
            'avg_score': avg_score,
            'description': description
        })

    return result


def run_interface(similarity_df, experts_df, projects_df):
    while True:
        project_id = input("Введите ID проекта (или '-' для выхода): ")
        if project_id == '-':
            print("Выход из программы.")
            break
        try:
            project_id = int(project_id)
            top_experts, project_description = get_top_experts(project_id, similarity_df, experts_df, projects_df)
            if isinstance(top_experts, str):
                print(top_experts)
            else:
                print(f"\nТоп-{len(top_experts)} экспертов для проекта {project_id}:")
                print(f"Краткое описание проекта: {project_description}")
                for expert in top_experts:
                    print(f"Эксперт ID: {expert['expert_id']}")
                    print(f"Компетентность: {expert['score']:.2f}%")
                    print(f"Квалификации: {expert['qualifications']}")
                    print("-" * 50)
        except ValueError:
            print("ID должен быть числом.")

    # Вывод топ-5 проектов
    print("\nТоп-5 проектов с самыми высокими оценками:")
    top_projects = get_top_projects(similarity_df, projects_df)
    for project in top_projects:
        print(f"Проект ID: {project['project_id']}")
        print(f"Средняя компетентность: {project['avg_score']:.2f}%")
        print(f"Описание: {project['description']}")
        print("-" * 50)