from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

from .models import Post

class BlogTests(TestCase):
    def setUpTestData():
        testuser1 = User.objects.create_user(
            username='test1', password='asdqwe')
        testuser1.save()
        
        test_post = Post.objects.create(
            author=testuser1, title='title', body='body')
        test_post.save()
    
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'test1')
        self.assertEqual(title, 'title')
        self.assertEqual(body, 'body')
