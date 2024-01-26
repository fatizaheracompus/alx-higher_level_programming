#!/usr/bin/python3
"""Function that finds a peak in a list of integers"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers.
    """

    liste_ = list_of_integers
    # if there is no list of integer return None
    if liste_ == []:
        return None
    length = len(liste_)

    starte, ende = 0, length - 1
    while starte < ende:
        mide = starte + (ende - starte) // 2
        if liste_[mide] > liste_[mide - 1] and liste_[mide] > liste_[mide + 1]:
            return liste_[mide]
        if liste_[mide - 1] > liste_[mide + 1]:
            ende = mide
        else:
            starte = mide + 1
    return liste_[starte]
