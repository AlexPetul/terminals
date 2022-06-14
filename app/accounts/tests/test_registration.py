import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
@pytest.mark.parametrize(
    "password",
    [
        "password",
        "WeakPasswordWithoutSpecialSymbols1",
        "strongpassword*without_uppercase",
        "StrongPassword_*WithoutNumbe@d#rs",
    ],
)
def test_weak_passwords(api_client: APIClient, password: str):
    """
    Test different kind of weak passwords. For example with missing upper or lower case letter,
    length less than 14 etc...Passwords should be complied with CIS requirements.
    """
    response = api_client.post(reverse("api-users-list"), {"email": "somerandom@email.com", "password": password})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert list(response.data.keys()).pop() == "password"
