# An artist has the possibility to visit a number of different exhibitions in different cities over
# the next four days. Based on her experience, she has estimated the probabilities of sales at
# each exhibition, given that she attends the exhibition for a day. Each of her paintings sells for
# $500. She also knows how much it costs to travel between exhibitions and from her home to
# each of the exhibitions. She can only attend each exhibition once.

# Exhibition Probability of Paintings Sold
#    0   1   2
# A 0.3 0.4 0.3
# B 0.2 0.5 0.3
# C 0.2 0.7 0.1
# D 0.3 0.5 0.2
# E 0.3 0.6 0.1
# F 0.4 0.3 0.3
# G 0.0 0.3 0.7
# H 0.1 0.1 0.8

#        A  B   C   D   E   F   G   H
# Home 143 108 118 121  88 121  57  92
# A         35  63 108 228 182  73 162
# B             45  86 193 165  42 129
# C                 46 190 203  73 105
# D                    172 224  98  71
# E                        174 160 108
# F                            129 212
# G                                117

# The artist wants to maximize her expected profit from a tour of four exhibitions. What
# path should she take?

# Suppose now that the artist only has 5 paintings to sell. What is her optimal strategy
# for a tour of at most four exhibitions assuming that she will return home once all
# paintings are sold?
