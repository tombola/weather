import os
from supabase import create_client, Client


class SupabaseLogger:
    def __init__(self):
        self.client = self.get_supabase_client()

    def get_supabase_client(self) -> Client:
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        return create_client(url, key)

    def log_sample(self, values):
        # {
        #     sample_id: int
        #     sample_timestamp: timestamp
        #     temperature: float
        #     pressure: float
        #     humidity: float
        # }
        return self.client.table("samples").insert(values).execute()
