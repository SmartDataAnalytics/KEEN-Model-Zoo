KEEN-Model-Zoo
==============
This repository represents the model zoo for the KEEN-Universe. All models that are trained with `PyKEEN <https://github.com/SmartDataAnalytics/PyKEEN>`_
and `BioKEEN <https://github.com/SmartDataAnalytics/BioKEEN>`_ can be shared along the additional experimental artefacts
by means of this model zoo (please check below for the requirements).


How to Share Your KGE Model
===========================
To share your KGE model (and further experimental artefacts) please make a pull request. The pull request should contain
a directory with following files:

* configuration.json: Configuration file (automatically generated)  describing the experienntal setup
* **entities_to_embeddings.json**: The learned embedding for the entities
* **relations_to_embeddings.json**: (optional since not every KGE model makes use of relations): The learned embedding for
the relations
* **entity_to_id.json**: Mapping of each entity to its id (automatically generated)
* **relation_to_id.json**: Mapping of each relation to its id (automatically generated)
* **evaluation_summary.json**: Achieved results (automatically generated)
* **losses.json**: Loss values for each epoch (automatically generated)
* **trained_model.pkl**: Trained model (serialized and automatically generated)
* **readme.rst**: A description of the experiment including the links to the paper and datasets;
example can be seen `here <ComPath/compath_model_01/readme.rst>`_
* **test.py**: A unit test that checks whether your model can be instantiated correctly using your
provided files

**Note**:: To ensure the quality of the shared model, we require that the corresponding experiment
was reviewed and published in a paper. Furthermore, the dataset used to train the model needs to be public accessible.

We will review your pull request and assist you if any fixes are required.
