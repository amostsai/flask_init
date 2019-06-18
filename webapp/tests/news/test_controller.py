from flask import url_for


class TestNews(object):
    def test_home_page(self, client):
        """ Home page should respond with a success 200. """
        response = client.get(url_for('news.news_home'))
        assert response.status_code == 200

    def test_pricing_page(self, client):
        """ Pricing page should respond with a success 200. """
        response = client.get(url_for('news.news_pricing'))
        assert response.status_code == 200
