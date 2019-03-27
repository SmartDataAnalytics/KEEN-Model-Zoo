KGE Model for ComPath
=====================
In this experiment the TransE model was trained on ComPath[1], and the experiment was reported in [2,3].
The corresponding results are saved in `evaluation_summary.json <evaluation_summary.json>`_, and the hyper-parameter values can be found in `configuration.json <configuration.json>`_


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

Links to Resources
==================

* Paper: [2,3]
* **Note**: ComPath has been updated, for this reason we have uploaded the dataset version that we have used for our experiments: `dataset <https://github.com/SmartDataAnalytics/KEEN-Model-Zoo/blob/master/bioinformatics/ComPath/compath.keen.tsv>`_


References
==========
.. [1] Domingo-Fernández, Daniel, *et al.* (2018) `ComPath: An ecosystem for exploring, analyzing, and curating mappings ´
       across pathway databases <https://doi.org/10.1038/s41540-018-0078-8>`_. NPJ systems biology and applications 4.43 .
.. [2] Mehdi Ali, Charles Tapley Hoyt, Daniel Domingo-Fernández, Jens Lehmann, & Hajira Jabeen(2019) `BioKEEN: a library for 
       learning and evaluating biological knowledge graph embeddings <https://doi.org/10.1093/bioinformatics/btz117>`_,    
       *Bioinformatics*, btz117.
