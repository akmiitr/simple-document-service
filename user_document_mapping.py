class UserDocumentMapping:

    def __init__(self, user_name, document_name, can_access=False):
        self.user_name = user_name
        self.document_name = document_name
        self.can_access = can_access
