# -*- coding: utf-8 -*-

"""Utilities for test cases."""

import json
import os

import torch
from pykeen.kge_models import get_kge_model
from torch.nn import Module


def load_model(model_directory: str) -> Module:
    """Load trained KGE model."""

    # Load configuration file
    with open(os.path.join(model_directory, 'configuration.json')) as f:
        config = json.load(f)

    trained_kge_model: Module = get_kge_model(config=config)
    path_to_model = os.path.join(model_directory, 'trained_model.pkl')
    trained_kge_model.load_state_dict(torch.load(path_to_model))

    return trained_kge_model
