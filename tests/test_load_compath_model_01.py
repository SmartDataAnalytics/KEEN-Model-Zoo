# -*- coding: utf-8 -*-

"""Test the instantiation of TransE trained on ComPath"""

import unittest

from tests.utils import load_model


class TestModelInstantiation(unittest.TestCase):

    def test_instantation(self):
        model_direc = '../bioinformatics/ComPath/compath_model_01'
        transE_compath_model = load_model(model_directory = model_direc)

        self.assertIsNotNone(transE_compath_model)
