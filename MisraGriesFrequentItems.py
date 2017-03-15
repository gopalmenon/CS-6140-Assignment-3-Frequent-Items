########################################################################################################################
#                                                                                                                      #
# Find frequent items in a stream using the Misra-Gries algorithm                                                      #
#                                                                                                                      #
########################################################################################################################


class MisraGriesFrequentItems(object):

    S1_FILE_NAME = "data/S1.txt"
    S2_FILE_NAME = "data/S2.txt"
    NUMBER_OF_ITEMS_TO_ESTIMATE_FREQUENCY_FOR = 10

    def __init__(self, stream_file_name, number_of_items_to_estimate_frequency_for):

        # Save stream file name
        self.stream_file_name = stream_file_name

        # Save number of counters required (plus one)
        self.number_of_items_to_estimate_frequency_for = number_of_items_to_estimate_frequency_for

        # Dictionary to save labels and their counts
        self.labels_and_counters = dict()

    # Return one character at a time from the file
    def __get_next_character_from_stream_file(self):

        with open(self.stream_file_name) as file_handle:
            for text_line in file_handle:
                for character in text_line:
                    yield character

    # Estimate the count for the k most occurring characters
    def estimate_character_counts(self):

        for stream_character in self.__get_next_character_from_stream_file():
            print(stream_character)

if __name__ == "__main__":

    misra_gries_frequent_items = \
        MisraGriesFrequentItems(MisraGriesFrequentItems.S1_FILE_NAME,
                                MisraGriesFrequentItems.NUMBER_OF_ITEMS_TO_ESTIMATE_FREQUENCY_FOR)
    misra_gries_frequent_items.estimate_character_counts()