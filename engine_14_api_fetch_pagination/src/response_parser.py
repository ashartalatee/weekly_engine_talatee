# src/response_parser.py

from typing import List, Dict, Any, Optional


class ResponseParser:
    def __init__(self, fields: Optional[List[str]] = None):
        """
        fields: daftar field yang ingin diambil.
        Kalau None → ambil semua field.
        """
        self.fields = fields

    def parse(self, response_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        parsed = []

        for item in response_data:
            if self.fields:
                filtered = {k: item.get(k) for k in self.fields}
                parsed.append(filtered)
            else:
                parsed.append(item)

        return parsed
