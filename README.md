# InverseSimpson
# Language: Python
# Input: CSV (abundances)
# Output: none (screen only)
# Tested with: PluMA 1.0, Python 3.6

PluMA plugin to compute the Inverse Simpson Diversity Index for each of a set of samples.
The plugin accepts sample data in the form of a CSV file where rows represent samples and columns
community members, with entry (i, j) holding the abundances of element j in sample i.
Output is only to the screen, and therefore this plugin expects no outputfile (pass 'none')
