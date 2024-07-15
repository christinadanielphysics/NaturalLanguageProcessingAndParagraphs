from separate import separate_skills
from parse import parse_skills
from condense import condense_skills
from clean import clean_skills
from summarize import summarize_skills
from group import group_skills
from repetition import remove_repetition
from education import remove_education
from numerical import remove_numbers
from generic import remove_generic

def transform_posting(posting):
    summarized_skills = summarize_skills(posting)
    pure_skills = remove_education(summarized_skills)
    skills_without_numbers = remove_numbers(pure_skills)
    grouped_skills = group_skills(skills_without_numbers)
    distinct_skills = remove_repetition(grouped_skills)
    specific_skills = remove_generic(distinct_skills)
    separated_skills = separate_skills(specific_skills)
    parsed_skill_sets = parse_skills(separated_skills)
    condensed_skill_sets = condense_skills(parsed_skill_sets)
    cleaned_skill_sets = clean_skills(condensed_skill_sets)
    return cleaned_skill_sets