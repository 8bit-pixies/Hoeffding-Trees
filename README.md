
Very Fast Decision Tree
=======================

This repository is an attempt to implement VFDT algorithm (Hoeffding Trees) within the scikit learn framework. The idea is not to produce a faithful representation, but rather a simple one which should be "good enough". 

This will be done in pure Python so it may not be as performant as "batch" models. However the purpose of this is to attempt to understand the implications of streaming or fitting infinitely large decision trees

**[Mining High-Speed Data Streams](https://homes.cs.washington.edu/~pedrod/papers/kdd00.pdf)**

>  Hoeffding trees can be learned in constant time per example (more precisely,
>  in time that is worst-case proportional to the number of
>  attributes), while being nearly identical to the trees a conventional
>  batch learner would produce, given enough examples.
>  The probability that the Hoeffding and conventional
>  tree learners will choose different tests at any given node decreases
>  exponentially with the number of examples. 
>  
>  VFDT is I/O bound in the sense
>  that it mines examples in less time than it takes to input
>  them from disk. It does not store any examples (or parts
>  thereof) in main memory, requiring only space proportional
>  to the size of the tree and associated sufficient statistics.
>  
>  Thus, given a stream of examples, the
>  first ones will be used to choose the root test; once the root
>  attribute is chosen, the succeeding examples will be passed
>  down to the corresponding leaves and used to choose the appropriate
>  attributes there, and so on recursively

One difference in this setting is that examples will be "compressed" via histogram approaches as discussed in [A Streaming Parallel Decision Tree Algorithm](http://www.jmlr.org/papers/volume11/ben-haim10a/ben-haim10a.pdf).


