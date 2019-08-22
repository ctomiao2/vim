# -*- coding: utf-8 -*-

# Some random text with multi-byte characters (utf-8 encoded)
#
# Εδώ μάτσο κειμένων τη, τρόπο πιθανό διευθυντές ώρα μη. Νέων απλό παράγει ροή
# κι, το επί δεδομένη καθορίζουν. Πάντως ζητήσεις περιβάλλοντος ένα με, τη
# ξέχασε αρπάζεις φαινόμενο όλη. Τρέξει εσφαλμένη χρησιμοποίησέ νέα τι. Θα όρο
# πετάνε φακέλους, άρα με διακοπής λαμβάνουν εφαμοργής. Λες κι μειώσει
# καθυστερεί.

# 79 narrow chars
# 01 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 [79]

# 78 narrow chars (Na) + 1 wide char (W)
# 01 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8情

# 3 narrow chars (Na) + 40 wide chars (W)
# 情 情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情

# 3 narrow chars (Na) + 76 wide chars (W)
# 情 情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情

#
# 80 narrow chars (Na)
#: E501
# 01 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6  [80]
#
# 78 narrow chars (Na) + 2 wide char (W)
#: E501
# 01 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8情情
#
# 3 narrow chars (Na) + 77 wide chars (W)
#: E501
# 情 情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情情
#
