# -*- coding: utf-8 -*-

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from .models import RegistroFechas
from .views import new


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

    def test_registro_fechas_renderiza_el_formulario_de_fechas(self):
        found = resolve('/registro_fechas/new')
        self.assertEqual(found.func, new)

    def test_registro_fechas_carga_el_template_correcto(self):
        request = HttpRequest()
        request.method = 'GET'
        response = new(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Registro de Fechas - Nuevo</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

    def test_veo_nombre_en_formulario(self):
        request = HttpRequest()
        request.method = 'GET'
        response = new(request)
        self.assertIn(b'<form method="POST">', response.content)
        self.assertIn(b'<label for="id_nombre"> Nombre </label>', response.content)
        self.assertIn(b'<input id="id_nombre">', response.content)
        self.assertIn(b'</form>', response.content)

    def test_al_guardar_formulario_guardo_nombre(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {'nombre': 'Jaimito'}
        new(request)

        # Se ha guardado en el modelo?
        registro = RegistroFechas.objects.first()
        self.assertEqual(registro.nombre, 'Jaimito')




