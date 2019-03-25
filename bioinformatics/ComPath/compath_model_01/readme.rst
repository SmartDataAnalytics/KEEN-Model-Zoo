KGE Model for ComPath
=====================
In this experiment the TransE model was trained on ComPath[1], and the experiment was reported in [2,3].
The corresponding results are saved in **evaluation_summary.json**. All the hyper-parameter values can be found in `configuration.json <https://github.com/SmartDataAnalytics/KEEN-Model-Zoo/blob/master/bioinformatics/ComPath/compath_model_01/configuration.json>`_


Contained Files:
================
* configuration.json
* entities_to_embeddings.json
* relations_to_embeddings.json
* entity_to_id.json
* relation_to_id.json
* evaluation_summary.json
* losses.json
* trained_model.pkl

References
==========
[1]: Domingo-Fernandez, Daniel, et al. "ComPath: An ecosystem for exploring, analyzing, and curating mappings across
pathway databases." NPJ systems biology and applications 5.1 (2018): 3.

[2]: Ali, Mehdi, et al. "BioKEEN: A library for learning and evaluating biological knowledge graph embeddings." bioRxiv (2018): 475202.

[3]: Mehdi Ali, Charles Tapley Hoyt, Daniel Domingo-Fernández, Jens Lehmann, Hajira Jabeen, BioKEEN: a library for
learning and evaluating biological knowledge graph embeddings, Bioinformatics,
btz117, https://doi.org/10.1093/bioinformatics/btz117
