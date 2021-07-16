from simple_doc_service.constants import Tier
from simple_doc_service.document_service import DocumentService

if __name__ == '__main__':
    """
    Simple document Service

    Design and implement a Simple document Service where users can create documents and read the same. A document has a name and associated string content <name{string}, content{string}>
    
    All documents are private when created.
    Owners of documents can grant access to other users
    Grants  can be made at global level as well. For example, if access is granted globally, then every user should have access to that document.
    Username will be just a string. Every action like create/read/edit must be made on behalf of a user
    Have different tiers. Hot tier should be served from memory. Cold tier should be served from the disk. Owner can specify which tier
    
    
    Document → document_id, owner_id, is_global_access, document_data, tier
    
    User → user_name, email, phone
    
    Document <--> User
    
    Many-to-many
    
    document_id, user_name, can_access


    """
    document_service = DocumentService()
    owner = document_service.create_user("ashok.kumar", "ashok.kumar@gmail.com", "7417386596")
    user = document_service.create_user("ashok", "ashok@gmail.com", "7417386597")
    document = document_service.create_document("personal_information", owner.user_id,
                                                {"name": "ashok", "content": {"place": "bangalore"}}, Tier("hot"))
    document_service.give_permission(document.document_name, user.user_name)
    document_service.access_document(document.document_name, user.user_name)
    result_doc = document_service.get_document(document.document_name, user.user_name)
    
    print(result_doc.__dict__)
