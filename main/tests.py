from http import HTTPStatus

from django.test import Client, TestCase


class URLTests(TestCase):
    def setUp(self) -> None:
        self.guest_client = Client()

    def test_url_ok(self) -> None:
        """Страница доступка по URL."""
        pages: tuple = ("/", "/user/register/", "/user/login/")
        for page in pages:
            response = self.guest_client.get(page)
            error_name: str = f"Ошибка: нет доступа до страницы {page}"
            self.assertEqual(response.status_code, HTTPStatus.OK, error_name)

    def test_url_302(self) -> None:
        page = "/all_applications_give/"
        response = self.guest_client.get(page)
        print(response)
        error_name: str = f"Ошибка: нет доступа до страницы {page}"
        self.assertEqual(response.status_code, HTTPStatus.FOUND, error_name)

    def test_urls_html(self) -> None:
        templates_url_names: dict = {
            "/": "main/index.html",
        }
        for adress, template in templates_url_names.items():
            with self.subTest(adress=adress):
                response = self.guest_client.get(adress)
                error_name: str = f"Ошибка: {adress} ожидал шаблон {template}"
                self.assertTemplateUsed(response, template, error_name)
