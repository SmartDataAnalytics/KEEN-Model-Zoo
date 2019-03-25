KGE Models for ComPath
======================

This directory contains KGE models trained on ComPath [1]. The ComPath dataset contains inter- and intra-database pathway mappings
that represent equivalent and hierarchically related pathways. The resources included
in ComPath are Kyoto Encyclopedia of Genes and Genomes (KEGG),
Reactome, and WikiPathways. To map equivalences and hierarchies of
biological pathways, the *equivalentTo* and *isPartOf* relationship were introduced.

Following figure shows the hierarchies between pathways:

.. image:: bioinformatics/ComPath/figures/compath_example.png


## Links to Resources

* Paper: [2,3]
* **Note**: ComPath has been updated, for this reason we have uploaded the dataset version that we have used for
 our experiments: `dataset <https://github.com/SmartDataAnalytics/KEEN-Model-Zoo/blob/master/bioinformatics/ComPath/compath.keen.tsv>`_







## References
[1]: Domingo-Fernandez, Daniel, *et al.* "ComPath: An ecosystem for exploring, analyzing, and curating mappings across
 pathway databases." NPJ systems biology and applications 4.43 (2018).

[2]: Ali, Mehdi, *et al.* "BioKEEN: A library for learning and evaluating biological knowledge graph embeddings." bioRxiv (2018): 475202.

[3]: Mehdi Ali, Charles Tapley Hoyt, Daniel Domingo-Fernández, Jens Lehmann, Hajira Jabeen, BioKEEN: a library for 
learning and evaluating biological knowledge graph embeddings, Bioinformatics,
 btz117, https://doi.org/10.1093/bioinformatics/btz117
