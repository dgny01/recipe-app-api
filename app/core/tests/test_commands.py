from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

class CommandTests(SimpleTestCase):
    """Test commands."""

    @patch('core.management.commands.wait_for_db.Command.check')  # check metodunu patch'liyoruz
    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready."""
        patched_check.return_value = True  # Veritabanı hazır olduğunda True dönüyor

        call_command('wait_for_db')  # Komutu çalıştırıyoruz

        patched_check.assert_called_once_with(databases=['default'])  # databases parametresi çoğul olmalı

    @patch('time.sleep')  # sleep fonksiyonunu patch'liyoruz
    @patch('core.management.commands.wait_for_db.Command.check')  # check metodunu patch'liyoruz
    def test_wait_for_db_delay(self, patched_check, patched_sleep):
        """Test waiting for database when getting OperationalError"""
        patched_check.side_effect = [Psycopg2Error] * 2 + [OperationalError] * 3 + [True]  # Hata simülasyonu

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)  # 6 kez kontrol yapılacak
        patched_check.assert_called_with(databases=['default'])  # databases parametresi çoğul olmalı
