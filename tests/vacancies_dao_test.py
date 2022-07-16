from app.vacancies.dao.vacancies_dao import VacanciesDAO
import pytest


@pytest.fixture()
def candidates_dao():
    vacancies_dao_instance = VacanciesDAO("./data/vacancies.json")
    return vacancies_dao_instance


# Defining the keys we expect should be
keys_should_be = {"pk", "company", "position", "salary"}


class TestVacanciesDAO:

    def test_get_all(self, vacancies_dao):
        """ Checking whether correct list of vacancies returns or not """
        vacancies = vacancies_dao.get_all()
        assert type(vacancies) == list, "Not a list has been returned"
        assert len(vacancies) > 0, "The candidates list is empty"
        assert set(vacancies[0].keys()) == keys_should_be, "The keys list is wrong"

    def test_get_by_pk(self, vacancies_dao):
        """ Checking whether correct vacancy returns by using of get_by_pk() method """
        vacancy = vacancies_dao.get_by_pk(1)
        assert vacancy["pk"] == 1, "Wrong vacancy has been returned"
        assert set(vacancy.keys()) == keys_should_be, "The keys list is wrong"
