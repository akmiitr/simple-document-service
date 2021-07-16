import uuid

from simple_doc_service.User import User
from simple_doc_service.constants import Tier
from simple_doc_service.document import Document
from simple_doc_service.user_document_mapping import UserDocumentMapping


class DocumentService():
    base_directory_path = "simple_doc_service/document_date.csv"

    def __init__(self):
        self.document_name_data_map = dict()
        self.document_user_access_map = dict()
        self.user_map = dict()
        self.document_name_document_map = dict()

    def access_document(self, document_name, user_name):
        if not self.document_name_document_map.get(document_name):
            raise Exception("Document does not exist")
        if self.document_name_document_map[document_name]:
            document = self.document_name_document_map[document_name]
            if not document.is_global_access:
                if not self.document_name_data_map.get(user_name):
                    raise Exception("User does not have right to access this document")

                document_names = self.document_name_data_map[user_name]
                for doc_name in document_names:
                    if doc_name == document_name:
                        return document
                raise Exception("User does not have right to access this document")
            return document

    def create_user(self, user_name, email, phone_number):
        user_id = uuid.uuid4()
        user = User(user_id, user_name, email, phone_number)
        self.user_map[user.user_name] = user
        return user

    def get_document(self, document_name, user_name):
        document = self.access_document(document_name, user_name)
        if document.tier == Tier.COLD:
            document_data = self.get_data_from_directory(document.document_name)
        if document.tier == Tier.HOT:
            document_data = self.document_name_data_map.get(document.document_name)
        document.document_data = document_data
        return document

    def create_document(self, document_name, owner_id, document_data, tier, is_global_access=False):
        document_id = uuid.uuid4()
        document = Document(document_id, document_name, owner_id, document_data, tier, is_global_access)
        if document.tier == Tier.COLD:
            self.put_data_into_directory(document)
        if document.tier == Tier.HOT:
            self.document_name_data_map[document.document_name] = document.document_data
        self.document_name_document_map[document_name] = document
        return document

    def edit_document(self, document_name, updated_document_data, user_name):
        document = self.access_document(document_name, user_name)
        document = Document(document_id=document.document_id, document_name=document.document_name,
                            owner_id=document.owner_id, document_data=updated_document_data, tier=document.tier)
        if document.tier == Tier.COLD:
            self.put_data_into_directory(document)
        if document.tier == Tier.HOT:
            self.document_name_data_map[document.document_name] = document.document_data
        self.document_name_document_map[document_name] = document
        return document

    def delete_document(self, document_name, user_name):
        # will check first if user has permission on particular document or not
        pass

    def give_permission(self, document_name, user_name, can_access=False):
        user_mapping = UserDocumentMapping(user_name, document_name, can_access)
        if self.document_name_data_map.get(user_mapping.user_name):
            self.document_name_data_map[user_mapping.user_name] = self.document_name_data_map[
                user_mapping.user_name].append(user_mapping.document_name)
        else:
            self.document_name_data_map[user_mapping.user_name] = [user_mapping.document_name]

    def put_data_into_directory(self, document):
        # use base path directory to put data into file
        pass

    def get_data_from_directory(self, docoment_name):
        # use base path directory to get data from file
        pass
