from django.test import TestCase
from django.utils import timezone
from .models import Samples, Result

class SamplesTest(TestCase):

    def test_without_image(self):
        sample = Samples.objects.create(
            sample_name="SAMPLE 1",
            sample_pacient_name="JOHN DOE",
            sample_date=timezone.now(),
        )
        self.assertTrue(sample.sample_image)

    def test_with_pacient_name(self):
        sample = Samples.objects.create(
            sample_name="SAMPLE 2",
            sample_pacient_name="JANE DOE",
            sample_date=timezone.now(),
        )
        self.assertTrue(sample.sample_pacient_name)

    def test_without_pacient_name(self):
        sample = Samples.objects.create(
            sample_name="SAMPLE 3",
            sample_pacient_name="",
            sample_date=timezone.now(),
        )
        self.assertFalse(sample.sample_pacient_name)


class ResultTest(TestCase):

    def setUp(self):
        self.sample = Samples.objects.create(
            sample_name="SAMPLE 4",
            sample_pacient_name="Juan Perez",
            sample_date=timezone.now(),
        )

    def test_result_default_negative(self):
        result = Result.objects.create(
            samples=self.sample,
            result_sample="SAMPLE 5",
            result_date=timezone.now(),
        )
        self.assertEqual(result.result_result, "NEGATIVE")

    def test_result_nositive(self):
        result = Result.objects.create(
            samples=self.sample,
            result_sample="SAMPLE 6",
            result_result="POSITIVE",
            result_date=timezone.now(),
        )
        self.assertEqual(result.result_result, "POSITIVE")

    def test_result_must_repeat(self):
        result = Result.objects.create(
            samples=self.sample,
            result_sample="SAMPLE 7",
            result_result="MUST REPEAT",
            result_date=timezone.now(),
        )
        self.assertEqual(result.result_result, "MUST REPEAT")