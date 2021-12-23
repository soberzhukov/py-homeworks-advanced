import unittest
import app
import unittest.mock


class TestSomething(unittest.TestCase):
    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    @unittest.mock.patch('builtins.input', lambda _: '11-2')
    def test_get_doc_owner_name_1(self): # p
        self.assertEqual(app.get_doc_owner_name(), 'Геннадий Покемонов')

    @unittest.mock.patch('builtins.input', lambda _: None)
    def test_get_doc_owner_name_2(self): # p
        self.assertEqual(app.get_doc_owner_name(), None)

    @unittest.mock.patch('builtins.input', lambda _: 'dsg')
    def test_get_doc_owner_name_3(self): # p
        self.assertEqual(app.get_doc_owner_name(), None)

    def test_get_all_doc_owners_names(self): # ap
        self.assertIs(type(app.get_all_doc_owners_names()), set)
        self.assertEqual(len(app.documents), len(app.get_all_doc_owners_names()))

    def test_show_all_docs_info(self): # l
        len_docs = len(app.documents)
        list_docs_info = list()
        for i in app.show_all_docs_info():
            list_docs_info.append(i)
        self.assertEqual(len(list_docs_info), len_docs)

    @unittest.mock.patch('builtins.input', lambda _: 'dsg')
    def test_get_doc_shelf_1(self): # s
        self.assertEqual(app.get_doc_shelf(), None)

    @unittest.mock.patch('builtins.input', lambda _: '11-2')
    def test_get_doc_shelf_2(self): # s
        self.assertEqual(app.get_doc_shelf(), '1')

    @unittest.mock.patch('builtins.input', side_effect=['1', '2', '3', '4'])
    def test_add_new_doc(self, mock_input): # a
        len_docs = len(app.documents)
        app.add_new_doc()
        self.assertGreater(len(app.documents), len_docs)
        self.assertIn('1', app.directories['4'])

    @unittest.mock.patch('builtins.input', lambda _: '10006')
    def test_delete_doc(self): # d
        before_len_docs = len(app.documents)
        before_len_directories_2 = len(app.directories['2'])
        app.delete_doc()
        self.assertGreater(before_len_docs, len(app.documents))
        self.assertGreater(before_len_directories_2, len(app.directories['2']))

    @unittest.mock.patch('builtins.input', side_effect=['2207 876234', '3'])
    def test_move_doc_to_shelf(self, mock_input): # m
        before_len_directories_1 = len(app.directories['1'])
        before_len_directories_3 = len(app.directories['3'])
        app.move_doc_to_shelf()
        self.assertGreater(before_len_directories_1, len(app.directories['1']))
        self.assertGreater(len(app.directories['3']), before_len_directories_3)

    @unittest.mock.patch('builtins.input', lambda _: '5')
    def test_add_new_shelf(self): # as
        before_len_directories = len(app.directories)
        app.add_new_shelf()
        self.assertGreater(len(app.directories), before_len_directories)
        self.assertIn('5', app.directories.keys())
