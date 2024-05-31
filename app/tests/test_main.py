import unittest
from unittest.mock import patch
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

class TestAPI(unittest.TestCase):
    """
    Test cases for the sentiment_feddit API endpoint.
    """

    @patch('app.main.requests.get')
    def test_sentiment_feddit(self,mock_get):
        """
        Test the sentiment_feddit API endpoint.

        This test mocks the HTTP GET request to the external service
        and verifies the behavior of the API endpoint.

        :param mock_get: Mock object for requests.get function.
        """
        mock_response = {
             "comments": [
                     {  "id": 67463,
                        "text": "Awesome.",
                    },
                    {
                         "id": 67464,
                        "text": "Well done!", }]}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        resp = client.get("/comment/?subfeddit_id=1&skip=0&limit=2")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(len(data),2)
        self.assertEqual(data[0]["classification"],"positive")
        self.assertEqual(data[1]["classification"],"neutral")

if __name__ == "__main__":
    unittest.main()