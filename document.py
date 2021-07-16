from simple_doc_service.constants import Tier


class Document:
    def __init__(self, document_id, document_name, owner_id, document_data, tier:Tier, is_global_access=False):
        self.document_id = document_id
        self.document_name = document_name
        self.owner_id = owner_id
        self.is_global_access = is_global_access
        self.document_data = document_data
        self.tier = tier
