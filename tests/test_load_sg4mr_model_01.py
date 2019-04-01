# -*- coding: utf-8 -*-

"""Test the instantiation of TransE trained on SG4MR"""

import unittest

from tests.utils import load_model

"""Note: Test cun be run only if GPU is avilable since model was trained on GPU."""

class TestModelInstantiation(unittest.TestCase):

    def test_instantation(self):
        model_direc = '../scholarly_data_related_recommendations/SG4MR/sg4mr_model_01'
        transE_sg4mr_model = load_model(model_directory = model_direc)

        self.assertIsNotNone(transE_sg4mr_model)
