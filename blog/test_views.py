
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post


class TestPostViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )

        self.post = Post(
            title="Blog title",
            author=self.user,
            slug="blog-title",
            excerpt="Blog excerpt",
            content="Blog content",
            status=1
        )
        self.post.save()

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""

        self.client.login(
            username="myUsername",
            password="myPassword"
        )

        post_data = {
            'body': 'This is a test comment.'
        }

        response = self.client.post(
            reverse('post_detail', args=['blog-title']),
            post_data
        )

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )
