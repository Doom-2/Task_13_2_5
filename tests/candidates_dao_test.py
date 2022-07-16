from app.candidates.dao.candidates_dao import CandidateDAO
import pytest


@pytest.fixture()
def candidates_dao():
    candidates_dao_instance = CandidateDAO("./data/candidates.json")
    return candidates_dao_instance


# Defining the keys we expect should be
keys_should_be = {"pk", "name", "position"}


class TestCandidateDAO:

    def test_get_all(self, candidates_dao):
        """ Checking whether correct list of candidates returns or not """
        candidates = candidates_dao.get_all()
        assert type(candidates) == list, "Not a list has been returned"
        assert len(candidates) > 0, "The candidates list is empty"
        assert set(candidates[0].keys()) == keys_should_be, "The keys list is wrong"

    def test_get_by_pk(self, candidates_dao):
        """ Checking whether correct candidate returns by using of get_by_pk() method """
        candidate = candidates_dao.get_by_pk(1)
        assert candidate["pk"] == 1, "Wrong candidate has been returned"
        assert set(candidate.keys()) == keys_should_be, "The keys list is wrong"
