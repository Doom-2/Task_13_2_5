class TestVacancies:

    def test_all_vacancies_status(self, test_client):
        """Checking whether the desired status code is obtained """
        response = test_client.get('/vacancies', follow_redirects=True)
        assert response.status_code == 200, "Status code of vacancies page request is wrong"

    def test_single_vacancy_status(self, test_client):
        """Checking whether the desired status code is obtained """
        response = test_client.get('/vacancies/1', follow_redirects=True)
        assert response.status_code == 200, "Status code of vacancy page request is wrong"
