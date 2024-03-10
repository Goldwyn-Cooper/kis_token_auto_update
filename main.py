if __name__ == "__main__":
    import logging
    import warnings
    logging.basicConfig(level=logging.WARNING)
    warnings.filterwarnings('ignore')

    import requests
    from dotenv import load_dotenv
    load_dotenv()
    
    from src.sb import SupabaseClient
    from src.kis import KISClient
    from src.telegram import TelegramBot

    bot = TelegramBot()
    bot.send_message(f'📌 KIS_TOKEN_AUTO_UPDATE')
    try:
        supabase = SupabaseClient()
        kis = KISClient()
        data = kis.get_access_token()
        supabase.update_token(kis.cano,
                              data['access_token'],
                              data['token_expired'])
        bot.send_message(
            f'Token refreshed ({kis.cano})\n'
            + data['token_expired'])
    except requests.exceptions.RequestException as e:
        print(e.response.status_code)
        print(e.response.reason)
    except Exception as e:
        print(type(e))
        print(e)
        bot.send_message(f'{type(e)}\n{e}')