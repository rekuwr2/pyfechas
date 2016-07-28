# -*- coding: utf-8 -*-

from django.core.urlresolvers import resolve, reverse_lazy, reverse
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

from registro_fechas.views import new, home


class RegistroFechasTest(TestCase):

    def setUp(self):
        """
        Método que se ejecuta antes de cada test
        :return:
        """
        # TODO
        pass

    def tearDown(self):
        """
        Método que se ejecuta después de cada test
        :return:
        """
        # TODO
        pass

    def test_url_registro_new_fecha_to_new_view(self):
        found = resolve(reverse_lazy('new'))
        self.assertEqual(found.func, new)

    def test_url_home_to_home_view(self):
        found = resolve(reverse_lazy('home'))
        self.assertEqual(found.func, home)

    def test_new_view_get_render_new_template(self):
        request = HttpRequest()
        request.method = 'GET'
        response = new(request)
        expected_html = render_to_string('new.html', request=request)
        self.assertHTMLEqual(response.content, expected_html)

    def test_search_view_get_render_search_template(self):
        request = HttpRequest()
        request.method = 'GET'
        response = home(request)
        expected_html = render_to_string('home.html', request=request)
        self.assertHTMLEqual(response.content, expected_html)

    def test_new_view_post_redirects_to_home_template(self):
        response = self.client.post(reverse_lazy('new'))
        self.assertRedirects(response, reverse('home'))

