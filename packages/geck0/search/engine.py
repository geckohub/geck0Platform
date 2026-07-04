class Geck0Search:
    def search(self, query: str):
        return {
            "query": query,
            "providers": ["notes", "files", "photos", "voice", "wiki", "git", "scans", "knowledgeGraph"],
            "status": "placeholder"
        }
