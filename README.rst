KEEN Model Zoo
==============
This repository represents the model zoo for the KEEN-Universe. All models that are trained with `PyKEEN <https://github.com/SmartDataAnalytics/PyKEEN>`_
and `BioKEEN <https://github.com/SmartDataAnalytics/BioKEEN>`_ can be shared along the additional experimental artefacts
via this model zoo (please check requirements listed below). The models are sorted according the research
fields.


How to Share Your KGE Model
===========================
To share your KGE model (and further experimental artefacts) please make a pull request. The pull request should contain
a directory with following files (that will be created automatically by Py/BioKEEN except the readme.rst and the test.py):

* **configuration.json**: Configuration file describing the experimental setup
* **entities_to_embeddings.json**: The learned embedding for the entities
* **relations_to_embeddings.json**: (optional since not every KGE model makes use of relations): The learned embedding for the relations

* **entity_to_id.json**: Mapping of each entity to its id 
* **relation_to_id.json**: Mapping of each relation to its id
* **evaluation_summary.json**: Achieved results 
* **losses.json**: Loss values for each epoch 
* **trained_model.pkl**: Trained model
* **readme.rst**: A description of the experiment including the links to the paper and datasets; an example can be found `here <bioinformatics/ComPath/compath_model_01/readme.rst>`_

* **test.py**: A unit test that checks whether your model can be instantiated correctly using your provided files

**Note**: To ensure the quality of the shared models, we require that the corresponding experiment
was reviewed and published in a paper. Furthermore, the dataset used to train the model needs to be public accessible.

We will review your pull request and assist you if any fixes are required.

The KEEN Model Zoo is licensed under the MIT License. By contributing to the project, you agree to the license
and copyright terms therein and release your contribution under these terms.


Structure of the KEEN Model Zoo
===============================

Experiments are categorised based on the research field. Currently, KGE models are available for experiments conducted
in the fields of:

* `Bioinformatics <bioinformatics>`_
* `Scholarly data research <scholarly_data_related_recommendations>`_

Each of the directories contain subdirectories corresponding to datasets on which the experiments have been performed.
And each of the dataset-directories contain subdirectories comprising the artifacts of a specifc experiment that has been
conducted on the dataset.

