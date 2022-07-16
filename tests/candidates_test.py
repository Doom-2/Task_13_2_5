class TestCandidates:

    def test_all_candidates_status(self, test_client):
        """Checking whether the desired status code is obtained """
        response = test_client.get('/candidates', follow_redirects=True)
        assert response.status_code == 200, "Status code of candidates page request is wrong"

    def test_single_candidate_status(self, test_client):
        """Checking whether the desired status code is obtained """
        response = test_client.get('/candidates/1', follow_redirects=True)
        assert response.status_code == 200, "Status code of candidates page request is wrong"
