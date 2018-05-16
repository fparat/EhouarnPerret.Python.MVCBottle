from unittest import TestCase
from project.controllers.api.samples import SAMPLES, get_samples


class SamplesFixture(TestCase):

    def test_get_samples(self, samples, no, expected):
        SAMPLES = samples
        actual = get_samples(no)
        self.assertEqual(actual, expected)

    def should_return_return_when_empty_samples_backfield_and_empty_no(self):
        pass

    def should_return_return_when_empty_samples_backfield_and_empty_no(self):
        pass

    def should_return_return_when_empty_samples_backfield_and_empty_no(self):
        pass

    def should_return_return_when_empty_samples_backfield_and_empty_no(self):
        pass




