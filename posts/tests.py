from django.test import TestCase
from django.urls import reverse

from posts.models import Post


class PostsTestCase(TestCase):
    def setUp(self):
        self.post1 = Post.objects.create(text='text', title='title')
        self.post2 = Post.objects.create(text='text2', title='title2')

    def test_posts_list(self):
        url = reverse('posts.list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text=self.post1.title)
        self.assertContains(response, text=self.post1.text)
        self.assertContains(response, text=self.post2.title)
        self.assertContains(response, text=self.post2.text)

    def test_posts_detail(self):
        url = reverse('posts.detail', args=(self.post1.id,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text=self.post1.title)
        self.assertContains(response, text=self.post1.text)

    def test_posts_create(self):
        url = reverse('posts.create')
        data = {'text': 'text3', 'title': 'title3'}
        response = self.client.post(url, data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain, [('/posts/', 302)])

        self.assertContains(response, text=data['text'])
        self.assertContains(response, text=data['title'])

        self.assertEqual(Post.objects.all().count(), 3)
        self.assertEqual(Post.objects.get(id=3).title, data['title'])
        self.assertEqual(Post.objects.get(id=3).text, data['text'])

    def test_posts_update(self):
        url = reverse('posts.update', args=(self.post2.id,))
        data = {'text': 'text2_upd', 'title': 'title2_upd'}
        response = self.client.post(url, data, follow=True)

        self.post2.refresh_from_db()
        self.assertEqual(response.redirect_chain, [
                         (reverse('posts.detail', args=(self.post2.id,)), 302)])

        self.assertContains(response, text=data['text'])
        self.assertContains(response, text=data['title'])

        self.assertEqual(Post.objects.get(
            id=self.post2.id).title, data['title'])
        self.assertEqual(Post.objects.get(id=self.post2.id).text, data['text'])

    def test_posts_delete(self):
        url = reverse('posts.delete', args=(self.post2.id,))
        response = self.client.post(url, follow=True)

        self.assertEqual(response.redirect_chain, [
                         (reverse('posts.list'), 302)])

        self.assertEqual(Post.objects.all().count(), 1)
