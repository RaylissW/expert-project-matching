import pandas as pd
import csv

def load_projects(file1):
    projects_df = pd.read_csv(file1, encoding='utf-8', sep=';', quoting=csv.QUOTE_ALL)
    project_columns = [
        'id', 'Название', 'Направление', 'Краткое описание проекта',
        'Комментарий модератора', 'Наименование места работы / учебы, должность',
        'Напишите наименование конкурсов и год участия', 'Город'
    ]
    projects_df = projects_df[project_columns].dropna(subset=['Краткое описание проекта'])
    projects_df['text_for_analysis'] = (
        projects_df['Название'].fillna('') + ' ' +
        projects_df['Направление'].fillna('') + ' ' +
        projects_df['Краткое описание проекта'].fillna('') + ' ' +
        projects_df['Комментарий модератора'].fillna('') + ' ' +
        projects_df['Наименование места работы / учебы, должность'].fillna('') + ' ' +
        projects_df['Напишите наименование конкурсов и год участия'].fillna('')
    )
    print(projects_df.columns)
    print("Проекты:")
    print(projects_df[['id', 'text_for_analysis']].head())
    print(f"Количество проектов: {len(projects_df)}")
    return projects_df

def load_experts(file):
    experts_df = pd.read_csv(file, encoding='utf-8', sep=';')
    experts_columns = [
        'id', 'Опыт и квалификация', 'Область научных и профессиональных интересов',
        'Достижения', 'Специальность', 'Должность', 'Опыт экспертной деятельности',
        'Опыт трекерского сопровождения', 'Опыт предпренимательской и проектной деятельности',
        'Опыт преподавательской деятельности', 'Знание специализированных программ',
        'Населенный пункт', 'Компания'
    ]
    experts_df = experts_df[experts_columns]
    experts_df['text_for_analysis'] = (
        experts_df['Опыт и квалификация'].fillna('') + ' ' +
        experts_df['Область научных и профессиональных интересов'].fillna('') + ' ' +
        experts_df['Достижения'].fillna('') + ' ' +
        experts_df['Специальность'].fillna('') + ' ' +
        experts_df['Должность'].fillna('') + ' ' +
        experts_df['Опыт экспертной деятельности'].fillna('') + ' ' +
        experts_df['Опыт трекерского сопровождения'].fillna('') + ' ' +
        experts_df['Опыт предпренимательской и проектной деятельности'].fillna('') + ' ' +
        experts_df['Опыт преподавательской деятельности'].fillna('') + ' ' +
        experts_df['Знание специализированных программ'].fillna('')
    )
    # Фильтр по длине текста
    experts_df = experts_df[experts_df['text_for_analysis'].str.len() >= 30]
    # Проверяем результат
    print(experts_df.columns)
    print("\nЭксперты:")
    print(experts_df[['id', 'text_for_analysis']].head())
    print(f"Количество экспертов: {len(experts_df)}")
    return experts_df

