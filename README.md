# The Head-directionality Converter for Dependency Treebank

We created a simple method to swap the head-directionality of parse trees in a dependency treebank in the CoNLLU format, named **headSwap**. In Alfina et al (2020), we applied this method to swap the head-directionality for noun phrases in Indonesian dependency treebank.


## The CSUI Dependency Treebank

The CSUI treebank is a conversion from an Indonesian constituency treebank in the Penn Treebank format named [**Kethu**](https://github.com/ialfina/kethu) that was also a conversion from a constituency treebank built by [**Dinakaramani et al. (2015)**](https://github.com/famrashel/idn-treebank). 
We named this treebank **CSUI**, since all the three versions of the treebanks were built at Faculty of Computer Science, Universitas Indonesia.

Other characteristics of the treebank:
* This treebank consists of 1030 sentences and 28,263 words.
* The genre of the sentences are mainly news in formal Indonesian. 
* Average sentence length is around 27.4 words per-sentence, which is very high compare to the [Indonesian-PUD](https://github.com/UniversalDependencies/UD_Indonesian-PUD) treebank that has average sentence length of 19.4.


### The Split
We provide two splits of the CSUI Dependency Treebank:
* Split-105-925, that was used on the experiment on a paper that described how the treebank was constructed (Alfina et a., 2020). This split consists of two dataset:
  * csui-test-105, the gold standard that manually annotated
  * csui-train-925, the training dataset that automatically converted 
  
* Split-UD, thas was published in UD website with name [UD Indonesian CSUI](https://github.com/UniversalDependencies/UD_Indonesian-CSUI). We need to create this split since UD treebank has requirement that a dataset with 20-30 K words should be split into 2 set, with the testing dataset consist of around 10K words. This split consists of two dataset:
  * id_csui-ud-test.conllu, consists of around 10K words
  * id_csui-ud-train.conllu, consists of around 18K words



## Acknowledgments

* The original constituency treebank was built with manual annotation by [Arawinda Dinakaramani, Fam Rashel, Andry Luthfi, and Ruli Manurung](https://github.com/famrashel/idn-treebank) at Faculty of Computer Science, Universitas Indonesia in 2015.
* The previous treebank was converted to the Penn Treebank format by Ika Alfina and Jessica Naraiswari Arwidarasti at Faculty of Computer Science, Universitas Indonesia in 2019. This PTB version was named [**Kethu**](https://github.com/ialfina/kethu).

## References
* Ika Alfina, Indra Budi, and Heru Suhartanto. [Tree Rotations for Dependency Trees: Converting the Head-Directionality of Noun Phrases](http://thescipub.com/pdf/jcssp.2020.1585.1597.pdf). In Journal of Computer Science, Vol 16 No 11, 2020.


## Changelog

2020-10-15 v1.0
* Initial release 

## Licence
You can use this dataset for free. You don't need our permission to use it. Please cite our paper if your work uses our data in your publication.
Please note that you are not allowed to create a copy of this dataset and share it publicly in your own repository without our permission.

## Contact
ika.alfina [at] cs.ui.ac.id
