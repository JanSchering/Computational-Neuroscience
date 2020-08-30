from math import log2


def exercise1():
    return -0.1*log2(0.1)-0.9*log2(0.9)

# The task is to calculate the Mutual Information between the flashing
# of the light and the firing of the neuron. The formula for mutual information
# is:
# H(X;Y) = H(Y) - H(Y|X)
def exercise2():

    # the First Step is to calculate H(Y) = Entropy of the flashing light
    # H(Y) = - sum( P(Xi) * log2(P(Xi) ) for all i possible states
    entropy_flash = -1 * (0.1 * log2(0.1) + 0.9 * log2(0.9))

    # The Next Step is to Calculate H(Y|X) = Conditional Entropy of the variable
    # H(Y|X) = sum( P(Xi) * H(Y | X = Xi) for all i possible x

    # For Convenience, we make use of the exchangeability between X and Y in the Mutual 
    # Information Calculation and see the Flashing now as X and the Firing as Y 
    # There are 2 possible cases:
    entropy_firing_with_flash = -1 * ( 0.1 * ( 0.5 * log2(0.5) + 0.5 * log2(0.5) ) )

    entropy_firing_without_flash = -1 * ( 0.9 * ( (1/18) * log2(1/18) + (17/18) * log2(17/18) ) )

    total_conditional_entropy = entropy_firing_with_flash + entropy_firing_without_flash

    mutual_information = entropy_flash - total_conditional_entropy

    return mutual_information

