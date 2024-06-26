from attributes_extractor.hebrew.data_extraction.education_extractor import extract_education
from attributes_extractor.hebrew.data_extraction.name_extractor import extract_name
from attributes_extractor.general_methods.data_extraction.birth_extractor import extract_birth
from attributes_extractor.general_methods.data_extraction.link_extractor import extract_link
from attributes_extractor.general_methods.data_extraction.mail_extractor import extract_mail
from attributes_extractor.general_methods.data_extraction.phone_extractor import extract_phone


def extract_hebrew(cv_text, nlp):
    cv_holder_name = extract_name(cv_text, nlp)
    birth = extract_birth(cv_text)
    numbers = extract_phone(cv_text)
    mails = extract_mail(cv_text)
    links = extract_link(cv_text)
    education = extract_education(cv_text)
    return cv_holder_name, birth, numbers, mails, links, education
