import unittest

class TestLoggedOut(unittest.TestCase):
    """Tests for audio articles site."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        connect_to_db(app, "postgresql:///testdb")
        db.create_all()

    def tearDown(self):
        """Should close the session and drop all tables"""
        db.session.close()
        db.drop_all()

    def testHomepage(self):
        result = self.client.get('/', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn("Welcome to Audio Articles", result.data)

    
    def testRead(self):
        result = self.client.get('/read', data={'text': "Hi this is a test",
                                                'voice_id': "Amy",
                                                'article_id': "1"}, follow_redirects=True)
        self.assertEqual(result.status_code, 200)


class TestLoggedIn(unittest.TestCase):
    """Testing logged in version of homepage"""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        connect_to_db(app, "postgresql:///testdb")
        db.create_all()
        example_data_users()
        example_data_articles()
        example_data_tags()
        example_data_taggings()

        with self.client as c:
            with c.session_transaction() as sess:
                sess["user_id"] = 1

    def tearDown(self):
        """Should close the session and drop all tables"""
        db.session.close()
        db.drop_all()

    def testHomepage(self):
        result = self.client.get('/', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn("Welcome,", result.data)

    def testRegister(self):
        result = self.client.get('/register', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn("Welcome,", result.data)

    def testLogin(self):
        result = self.client.get('/login', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn("Welcome,", result.data)

    def testCreateArticle(self):
        result = self.client.get('/create-article',
                                 query_string={'user_id_from_form': "1"}, 
                                 follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn("Title:", result.data)

    def testUserArticles(self):
        result = self.client.get('/user-articles/1', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn("Welcome", result.data)

    def testArticleCloseup(self):
        result = self.client.get('/article-closeup/1', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn("Select a voice:", result.data)

    def testArticleEdit(self):
        result = self.client.get('/article-edit/1')
        self.assertEqual(result.status_code, 200)
        self.assertIn("Title:", result.data)

    def testRead(self):
        result = self.client.get('/read', query_string={'text': "Hi this is a test",
                                                        'voice': "Amy",
                                                        'article_id': "1"}, 
                                                        follow_redirects=True)
        self.assertEqual(result.status_code, 200)