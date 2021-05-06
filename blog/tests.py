from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='checker', email='checker@email.com', password='secret')
        self.post = Post.objects.create(title='checking title', body='checking body', author=self.user)
    
    def test_get_absolute_url(self): 
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')
    
    def test_string_representation(self):
        post = Post(title='checking title')
        self.assertEqual(str(post), post.title)
    
  def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'checking title')
        self.assertEqual(f'{self.post.author}', 'checker')
        self.assertEqual(f'{self.post.body}', 'checking body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'checking body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detailView(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'checking title')
        self.assertTemplateUsed(response, 'postDetail.html')
    
    def test_post_createView(self):
        response = self.client.post(reverse('postNew'), {'title': 'New title', 'body': 'New file', 'author': self.user.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'New title')
        self.assertEqual(Post.objects.last().body, 'New file')
    
    def test_post_updateView(self):
        response = self.client.post(reverse('postEdit', args='1'), {'title': 'Updated title','body': 'Updated text'})
        self.assertEqual(response.status_code, 302)
    
    def test_post_deleteView(self):
        response = self.client.post(reverse('postDelete', args='1'))   
        self.assertEqual(response.status_code, 302)


