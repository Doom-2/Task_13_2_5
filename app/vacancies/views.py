from flask import Blueprint, render_template
from .dao.vacancies_dao import VacanciesDAO

# Creating a blueprint
vacancies_blueprint = Blueprint('vacancies_blueprint', __name__, template_folder="templates")

# Creating a DAO instance
vacancies_dao = VacanciesDAO("./data/vacancies.json")


# Creating a view for all vacancies
@vacancies_blueprint.get('/vacancies')
def page_vacancies_all():
    vacancies = vacancies_dao.get_all()
    return render_template('vacancies_index.html', vacancies=vacancies)


# Creating a view for one vacancy
@vacancies_blueprint.get('/vacancies/<int:pk>')
def page_vacancy(pk):
    vacancy = vacancies_dao.get_by_pk(pk)
    return render_template('vacancy_single.html', vacancy=vacancy)
