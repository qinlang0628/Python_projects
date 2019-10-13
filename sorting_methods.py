# Please add necessary comments 
import time
    
class counter(object):
    '''
    an counter object to record the number of compare, number of swap and running time by a sorting method
    '''
    def __init__(self):
        '''initialize a conter object'''
        self.num_compare = 0
        self.num_swap = 0
        self.start = time.time()
        self.running_time = 0
    
    def compare(self):
        '''compare once'''
        self.num_compare += 1
    
    def swap(self):
        '''swap once'''
        self.num_swap += 1
    
    def record_timing(self):
        '''record running time by deducting starting time from current time'''
        self.running_time = time.time() - self.start
        
    def get_running_time(self):
        '''get running time'''
        return self.running_time
    
    def __repr__(self):
        '''print instances'''
        s1 = 'number of comparison: {}'.format(self.num_compare)
        s2 = 'number of swap: {}'.format(self.num_swap)
        s3 = 'running time: {} seconds'.format(self.running_time)
        return '\n'.join([s1, s2, s3])


     
class MySorted(object):
    '''
    an object which has two methods (bubble sort and merge sort) to sort an iterable
    implemented sorting methods:
    - bubble_sort
    - merge_sort
    - quick_sort
    '''
    def __init__(self):
        '''
        initialize a MySort object
        '''
        return
        
    def _compare_swap_adjacent_elements(self, iterable, key, reverse, i, Counter):
        '''
        compare and swap (i)th and (i+1)th element in the iterable
        input:
            iterable, key, reverse, Counter: inherit value
            i: the index of the element
        output:
            None
        '''
        # extract comparable value from iterable[i] and iterable[i+1]
        xi, xj = iterable[i], iterable[i + 1]
        xi_val, xj_val = key(xi), key(xj)
        
        # compare and swap
        if (reverse and xi_val < xj_val) or (not reverse and xj_val < xi_val):
            iterable[i], iterable[i + 1] = xj, xi
            Counter.swap()
        Counter.compare()
        
         
            
    def bubble_sorted(self, iterable, key=lambda x: x, reverse=False, Counter=None, i=1):
        '''
        recursively bubble sort the iterable until no two adjacent elements could be swapped
        input:
            iterable: a sequence (list, tuple, string) or collection (dictionary, set, frozenset) or any other iterator that needs to be sorted.
            key: a function that would server as a key or a basis of sort comparison; use the raw element if no key is provided
            reverse: if True, sorted the iterable by descending order, if False, sorted in acsending order
            Counter: an counter object to record the number of compare, number of swap and running time
            i: an index denotes number of loops
        output:
            (the sorted list, number of comparison, number of swap, running time)
        '''
        # initialize a new counter at the beginning of bubble sort
        # to record number of comparison, number of swap and running time
        if not Counter:
            Counter = counter()
        n = len(iterable)
        
        # for every two adjacent elements in the iterable, compare and swap them
        # (deduct one after each iteration, because one element in the right end 
        # would be fixed after every iteration)
        for i in range(n):
            num_swap = Counter.num_swap
            for j in range(0, len(iterable) - i - 1):
                
                # compare and swap
                if (reverse and key(iterable[j]) < key(iterable[j+1])) or \
                (not reverse and key(iterable[j+1]) < key(iterable[j])):
                    iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j] 
                    Counter.swap()
                Counter.compare()
                    

            # if no swap happens, the literable is fully sorted, end the for loop, else continue
            if num_swap == Counter.num_swap:
                break
        
        Counter.record_timing()
        return (iterable, Counter)    
        
        
    
    # merge lsort and rsort
    def _merge(self, iterable, left, right, key, reverse, Counter):
        '''
        merge two sorted list in order
        input:
            left: a sorted list
            right: a sorted list
            key, reverse, Counter: inherit value
        output:
            merged: a sorted merged list
        '''
        # initiate a new list to store the value
        i, j, k = 0, 0, 0
        
        # compare the left side of both lists, add element in two lists to a new list in order
        while (i < len(left)) and (j < len(right)):
            xi, xj = left[i], right[j]
            xi_val, xj_val = key(xi), key(xj)
            if (xi_val < xj_val and not reverse) or (xi_val > xj_val and reverse):
                iterable[k] = xi
                i += 1
            else:
                iterable[k] = xj
                j += 1
            k += 1
            Counter.compare()
            Counter.swap()
        
        # when one list is exhausted, append the rest of other list
        if i < len(left):
            iterable[k:] = left[i:]
        elif j < len(right):
            iterable[k:] = right[j:]
                    
    
    def merge_sorted(self, iterable, key=lambda x: x, reverse=False, Counter=None):
        '''
        recursively split the iterable into half and merge the sorted components
        input:
            iterable: a sequence (list, tuple, string) or collection (dictionary, set, frozenset) or any other iterator that needs to be sorted
            key: a function that would server as a key or a basis of sort comparison; use the raw element if no key is provided
            reverse: if True, sorted the iterable by descending order, if False, sorted in acsending order
            Counter: a counter object to record the number of compare, number of swap and running time
        output:
            merged: a sorted list
            Counter: a counter object to record the number of compare, number of swap and running time
        '''
        # initialize a new counter at the beginning of bubble sort
        # to record number of comparison, number of swap and running time
        if not Counter:
            Counter = counter()
        
        # if there is only one element in the iterable, output itself
        if len(iterable) <= 1:
            merged = iterable
        else:
            # if there are are than one element in the iterable
            # split in half and merge sort (recursively) each of them
            m = int(len(iterable) / 2)
            left = iterable[:m]
            right = iterable[m:]
            self.merge_sorted(left, key, reverse, Counter)
            self.merge_sorted(right, key, reverse, Counter)

            # merge the left list and right list in order
#             iterable = self._merge(iterable, left, right, key, reverse, Counter)
            self._merge(iterable, left, right, key, reverse, Counter)
        
        Counter.record_timing()
        return (iterable, Counter)   

    
    def quick_sorted(self, iterable, key=lambda x: x, reverse=False, Counter=None):
        '''
        recursively partition the iterable and sort
        '''
        if not Counter:
            Counter = counter()
            
        # when length of the iterable = 1, terminate the iteration
        if len(iterable) <= 1:
            return (iterable, Counter)
        else:
            # set the last element in the list as a pivot, put it in the right side
            pivot = iterable[-1]
            left = []
            right = [pivot]
            
            for _, x in enumerate(iterable[:-1]):
                # be careful with key(x) == key(pivot) case, always put x in the left list
                # otherwise it will cause an endless recursion loop
                if (key(x) <= key(pivot) and not reverse) or (key(x) >= key(pivot) and reverse):
                    left.append(x)
                else:
                    right.append(x)
                Counter.compare()
                Counter.swap()

            left, _ = self.quick_sorted(left, key, reverse, Counter)
            right, _ = self.quick_sorted(right, key, reverse, Counter)
            iterable = left + right
            
            Counter.record_timing()
            return (iterable, Counter)