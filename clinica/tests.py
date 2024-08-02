from django.test import TestCase

from clinica.models import Contato


class ContatoTestCase(TestCase):
    def test_save(self):
        contato = Contato.objects.create(prefixo = "12", numero = "34567890")
        self.assertEqual(contato.id, 1)
