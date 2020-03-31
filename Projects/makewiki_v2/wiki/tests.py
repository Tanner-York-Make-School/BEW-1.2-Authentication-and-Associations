from django.test import TestCase
from django.contrib.auth.models import User
from wiki.models import Page

class WkikTestCase(TestCase):

    # Unit Tests
    def test_page_slugify_on_save(self):
        """ Tests the slug generated when saving a Page. """
        user = User()
        user.save()
        page = Page.objects.create(title="My Test Page", content="test", author=user)
        page.save()
        self.assertEqual(page.slug, "my-test-page")


    # Route Tests
    def test_multiple_pages(self):
        # Make some test data to be displayed on the page.
        user = User.objects.create()

        Page.objects.create(title="My Test Page", content="test", author=user)
        Page.objects.create(title="Another Test Page", content="test", author=user)

        # Issue a GET request to the MakeWiki homepage.
        # When we make a request, we get a response back.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the number of pages passed to the template
        # matches the number of pages we have in the database.
        responses = response.context['pages']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Page: My Test Page>', '<Page: Another Test Page>'],
            ordered=False
        )

    def test_create_page_url(self):
        response = self.client.get('/w/create/')
        self.assertEqual(response.status_code, 200)

    def test_create_post_url(self):
        response = self.client.get('/p/create/')
        self.assertEqual(response.status_code, 200)

    def test_page_list_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)