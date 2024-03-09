from unittest import TestCase, main, skip
import os

from dotenv import load_dotenv
load_dotenv()

class MainTests(TestCase):
    def test_update_token(self):
        from src.sb import SupabaseClient
        from src.kis import KISClient
        supabase = SupabaseClient()
        kis = KISClient()
        data = kis.get_access_token()
        supabase.update_token(
            os.getenv('KIS_CANO'),
            data['access_token'],
            data['token_expired'])

class SupabaseTests(TestCase):
    def test_url(self):
        url = os.getenv('SUPABASE_URL')
        self.assertIsInstance(url, str)

    def test_key(self):
        key = os.getenv('SUPABASE_KEY')
        self.assertIsInstance(key, str)

    def test_fetch_token_from_cano(self):
        from src.sb import SupabaseClient
        supabase = SupabaseClient()
        token = supabase.fetch_token_from_cano(os.getenv('KIS_CANO'))
        self.assertIsInstance(token, dict)
        self.assertIn('access_token', token)
        self.assertIn('token_expired', token)
    
class KISTests(TestCase):
    def test_app_key(self):
        app_key = os.getenv('KIS_APP_KEY')
        self.assertIsInstance(app_key, str)

    def test_app_secret(self):
        app_secret = os.getenv('KIS_APP_SECRET')
        self.assertIsInstance(app_secret, str)
    
    @skip('403 Forbidden')
    def test_get_access_token(self):
        from src.kis import get_access_token
        access_token = get_access_token()
        self.assertIsInstance(access_token, dict)
        self.assertIn('access_token', access_token)
        self.assertIn('token_expired', access_token)

class TelegramTests(TestCase):        
    def test_bot_token(self):
        bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.assertIsInstance(bot_token, str)

    def test_chat_id(self):
        chat_id = os.getenv('TELEGRAM_CHAT_ID')
        self.assertIsInstance(chat_id, str)

    def test_send_message(self):
        from src.telegram import TelegramBot
        bot = TelegramBot()
        bot.send_message('Hello World!')

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.WARNING)
    main()