class MainTest:

    def test_root_status(self, test_client) -> None:
        """ Checking whether the desired status code is obtained """
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, "Status code is wrong"

    def test_root_content(self, test_client) -> None:
        """ Checking the content of main page """
        response = test_client.get('/', follow_redirects=True)
        assert "This is a main page" in response.data.decode("utf-8"), "Main page content is wrong"
