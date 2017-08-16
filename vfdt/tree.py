
import numpy as np
import pandas as pd


class Histogram:
    """
    This class implements histogram adding, updating and compression for a single point value pair 
    """
    def find_two_closest(self, numbers):
        # https://stackoverflow.com/questions/36845202/two-closest-points-in-list
        delta = max(numbers), min(numbers)
        for i, element in enumerate(numbers):
            for j, sec_element in enumerate(numbers):
                if i == j:
                    continue
                if abs(sec_element - element) < abs(delta[0] - delta[1]):
                    delta = sec_element, element
        return delta

    def __init__(self, points=[], value=[], num_partitions=100):
        self.points = np.array(points)
        self.value = np.array(value)
        self.num_partitions=num_partitions
    
    def update(self, x):
        """
        Add one data point

        Parameters:
        *  x: a single value
        """
        self.points = np.hstack([self.points, x])
        self.value = np.hstack([self.value, 1])
        
        if self.points.shape[0] > num_partitions:
            # remove one bin
            self.compress()
        return self     

    def compress(self):
        p1, p2 = find_two_closest(self.points)
        p1_loc = np.argwhere(self.points == p1)
        p1_val = self.value[p1_loc]
        p2_loc = np.argwhere(self.points == p2)
        p2_val = self.value[p2_loc]

        compress_points = [x for x in list(self.points) if x not in [p1, p2]]
        compress_vals   = [self.value[idx] for idx, x in enumerate(self.points) if x not in [p1, p2]]

        new_point = (p1*p1_val + p2*p2_val)/(p1_val + p2_val)
        new_val = (p1_val + p2_val)

        compress_points.append(new_point)
        compress_vals.append(new_val)
        self.points = compress_points
        self.value = compress_vals


def combine_histograms(list_of_histograms=[]):
    """
    Combines a list of histograms together
    """
    return None




class SplitMetric:
    def __init__()



class VFDT(BaseEstimator, TransformerMixin):
    """
    Very Fast Decision Trees (VFDT) is an algorithm based on Hoeffding trees. 

    Mining High-Speed Data Streams:

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

    Parameters

    *  split_rule: the split evaluation function, one of `gini`, `entropy`
    *  delta: one minus the desired probability of
              choosing the correct attribute at any
              given node.
    """
    def __init__(self, split_rule='gini', delta=0.05):
        self.split_rule = split_rule # this should be a function!
        self.delta = delta
    



    

