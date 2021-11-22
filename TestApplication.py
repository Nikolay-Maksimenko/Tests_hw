import app
import unittest
from unittest.mock import patch

class AppTester(unittest.TestCase):

    test_doc_number = '10006'
    doc_number_delete = '2207 876234'
    add_test_doc = ['777-55', 'invoice', 'Bruce Wayne', '3']

    def test_check_document_existence(self):
        self.assertTrue(app.check_document_existance('11-2'))
        self.assertFalse(app.check_document_existance('999'))
        self.assertFalse(app.check_document_existance(''))

    @patch('builtins.input', return_value=test_doc_number)
    def test_get_doc_owner_name(self, mock_input):
        doc_owner = [doc['name'] for doc in app.documents if doc['number'] == AppTester.test_doc_number][0]
        self.assertEqual(app.get_doc_owner_name(), doc_owner)

    def test_remove_doc_from_shelf(self):
        docs_list = []
        app.remove_doc_from_shelf('10006')
        for documents in app.directories.values():
            for document in documents:
                docs_list.append(document)
        print(docs_list)
        self.assertNotIn('10006', docs_list)

    def test_add_new_shelf(self):
        self.assertEqual(app.add_new_shelf('new_shelf'), ('new_shelf', True))
        self.assertEqual(app.add_new_shelf('1'), ('1', False))
        self.assertIn('new_shelf', app.directories.keys())

    def test_append_doc_to_shelf(self):
        app.append_doc_to_shelf('new_doc', '3')
        self.assertIn('new_doc', app.directories['3'])

    @patch('builtins.input', return_value=doc_number_delete)
    def test_delete_doc(self, mock_input):
        app.delete_doc()
        docs = [doc['number'] for doc in app.documents]
        self.assertNotIn(AppTester.doc_number_delete, docs)

    @patch('builtins.input', return_value=test_doc_number)
    def test_get_doc_shelf(self, mock_input):
        for shelf, doc_list in app.directories.items():
            if AppTester.test_doc_number in doc_list:
                self.assertEqual(app.get_doc_shelf(), shelf)
                break

    def test_show_document_info(self):
        first_doc = f'{app.documents[0]["type"]} "{app.documents[0]["number"]}" "{app.documents[0]["name"]}"'
        last_doc = f'{app.documents[-1]["type"]} "{app.documents[-1]["number"]}" "{app.documents[-1]["name"]}"'
        self.assertEqual(app.show_document_info(app.documents[0]), first_doc)
        self.assertEqual(app.show_document_info(app.documents[-1]), last_doc)

    def test_show_all_docs_info(self):
        docs_from_documents = [f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"' for doc in app.documents]
        print(docs_from_documents)
        self.assertEqual(app.show_all_docs_info(), docs_from_documents)

    @patch('builtins.input', side_effect=add_test_doc)
    def test_add_new_doc(self, mock_input):
        app.add_new_doc()
        doc_number, doc_type, doc_owner, shelf = AppTester.add_test_doc
        new_doc = {'type': doc_type, 'number': doc_number, 'name': doc_owner}
        self.assertIn(new_doc, app.documents)
        self.assertIn(shelf, app.directories)