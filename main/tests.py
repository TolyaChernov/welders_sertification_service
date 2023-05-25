##################################################
from main.views import add_application, index
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import Group, User
import os
import unittest
from http import HTTPStatus
from unittest.mock import patch

from django.conf import settings
from django.http import HttpResponse
from django.test import Client, RequestFactory, TestCase

from main.utils import fetch_pdf_resources, render_to_pdf

#####################################################


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


# Я могу попробовать написать unittest на ваш код, но я не гарантирую, что
# он будет полным и правильным. Вот примерный вариант:

# import os
# import unittest
# from unittest.mock import patch

# from django.conf import settings
# from django.http import HttpResponse
# from django.test import RequestFactory

# from .utils import render_to_pdf, fetch_pdf_resources


# class TestRenderToPdf(unittest.TestCase):

#     def setUp(self):
#         self.factory = RequestFactory()
#         self.url_template = "main/templates/pdf/invoice.html"
#         self.context = {"some": "data"}

#     def test_render_to_pdf_success(self):
#         request = self.factory.get("/")
#         response = render_to_pdf(self.url_template, self.context)
#         self.assertIsInstance(response, HttpResponse)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response["Content-Type"], "application/pdf")

#     def test_render_to_pdf_failure(self):
#         request = self.factory.get("/")
#         response = render_to_pdf("main/templates/pdf/invoice.html", self.context)
#         self.assertIsNone(response)


class TestFetchPdfResources(unittest.TestCase):
    def test_fetch_pdf_resources_media(self):
        uri = settings.MEDIA_URL + "test.pdf"
        rel = "rel"
        expected_path = os.path.join(settings.MEDIA_ROOT, "test.pdf")
        actual_path = fetch_pdf_resources(uri, rel)
        self.assertEqual(actual_path, expected_path)

    def test_fetch_pdf_resources_static(self):
        uri = settings.STATIC_URL + "test.pdf"
        rel = "rel"
        expected_path = os.path.join(settings.STATIC_ROOT, "test.pdf")
        actual_path = fetch_pdf_resources(uri, rel)
        self.assertEqual(actual_path, expected_path)

    def test_fetch_pdf_resources_other(self):
        uri = "https://example.com/test.pdf"
        rel = "rel"
        actual_path = fetch_pdf_resources(uri, rel)
        self.assertIsNone(actual_path)


##############################################################
#
#
#
#
# Я могу попробовать написать unittest на ваш код, но я не гарантирую, что
# он будет полным и правильным. Вот примерный вариант:


class TestIndex(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_anonymous(self):
        request = self.factory.get("/")
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "Главная")
        self.assertEqual(response.context["group"], "No_Group")

    def test_index_admin(self):
        request = self.factory.get("/")
        request.user = User.objects.create_superuser(
            username="admin", password="admin")
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "Главная")
        self.assertEqual(response.context["group"], "admin")

    def test_index_user(self):
        request = self.factory.get("/")
        user = User.objects.create_user(username="user", password="user")
        group = Group.objects.create(name="user_group")
        user.groups.add(group)
        request.user = user
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "Главная")
        self.assertEqual(response.context["group"], "user_group")


class TestAddApplication(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.url_template = "your_app/template.html"
        self.context = {"some": "data"}

    def test_add_application_anonymous(self):
        request = self.factory.get("/add_application/")
        response = add_application(request)
        expected_url = reverse("login") + "?next=/add_application/"
        self.assertRedirects(response, expected_url)

    @patch("main.views.render_to_pdf")
    def test_add_application_post(self, mock_render_to_pdf):
        request = self.factory.post("/add_application/", data=self.context)
        request.user = User.objects.create_user(
            username="user", password="user")
        mock_render_to_pdf.return_value = HttpResponse()
        response = add_application(request)
        mock_render_to_pdf.assert_called_once_with(
            self.url_template, self.context)
        self.assertIsInstance(response, HttpResponse)

    def test_add_application_get(self):
        request = self.factory.get("/add_application/")
        request.user = User.objects.create_user(
            username="user", password="user")
        response = add_application(request)
        self.assertEqual(response.status_code, 200)
