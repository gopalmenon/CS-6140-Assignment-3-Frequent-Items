import HashFunctions
import unittest

########################################################################################################################
#                                                                                                                      #
# Find frequent items in a stream using Count-Min Sketch algorithm                                                     #
#                                                                                                                      #
########################################################################################################################


class CountMinSketchFrequentItems(object):

    S1_FILE_NAME = "data/S1.txt"
    S2_FILE_NAME = "data/S2.txt"
    NUMBER_OF_ITEMS_TO_ESTIMATE_FREQUENCY_FOR = 10
    NUMBER_OF_HASH_FUNCTIONS = 5

    def __init__(self, stream_file_name, number_of_items_to_estimate_frequency_for, number_of_hash_functions):

        self.stream_file_name = stream_file_name
        self.number_of_items_to_estimate_frequency_for = number_of_items_to_estimate_frequency_for
        self.number_of_hash_functions = number_of_hash_functions
        # Create the item counters as a dictionary with the hash function as the key
        self.item_counters = dict()
        for hash_function_counter in range(self.number_of_hash_functions):
            self.item_counters[HashFunctions.NGramHash(hash_function_counter,
                                                       self.number_of_items_to_estimate_frequency_for)] = \
            [0] * self.number_of_items_to_estimate_frequency_for

########################################################################################################################
#                                                                                                                      #
# Unit testing class.                                                                                                  #
#                                                                                                                      #
########################################################################################################################

class TestCountMinSketch(unittest.TestCase):

    def test_for_s1_and_s2(self):

        for file_name in [CountMinSketchFrequentItems.S1_FILE_NAME, CountMinSketchFrequentItems.S2_FILE_NAME]:
            count_min_sketch_frequent_items \
                = CountMinSketchFrequentItems(file_name,
                                              CountMinSketchFrequentItems.NUMBER_OF_ITEMS_TO_ESTIMATE_FREQUENCY_FOR,
                                              CountMinSketchFrequentItems.NUMBER_OF_HASH_FUNCTIONS)

"""
Self test
"""
if __name__ == "__main__":
    unittest.main()