# Create your tests here.
from django.urls import reverse_lazy


def test_landing_page_view(client):
    response = client.get(reverse_lazy('home:landing_page'))
    assert response.status_code == 200
