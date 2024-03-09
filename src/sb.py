import os
from supabase import create_client, Client

class SupabaseClient:
    def __init__(self):
        if not os.getenv('SUPABASE_URL'):
            raise ValueError('SUPABASE_URL is not set')
        if not os.getenv('SUPABASE_KEY'):
            raise ValueError('SUPABASE_KEY is not set')
        self.client : Client = create_client(
            os.getenv('SUPABASE_URL'),
            os.getenv('SUPABASE_KEY'),
        )
    
    def fetch_token_from_cano(self, cano: str) -> str:
        query = self.client.table('KIS_TOKEN')\
                .select('*').eq('cano', cano) 
        result = query.execute()
        return result.data[0]
    
    def update_token(self, cano: str, token: str, token_expired: str) -> None:
        query = self.client.table('KIS_TOKEN')\
                .update({
                    'access_token': token,
                    'token_expired': token_expired,
                }).eq('cano', cano)
        return query.execute()
    
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    supabase = SupabaseClient()
    print(supabase.fetch_token_from_cano(os.getenv('KIS_CANO')))