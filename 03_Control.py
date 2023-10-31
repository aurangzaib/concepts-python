"""

 Description:
 Control
 
 Modifications:
 ---------------------------------------------------------------------------------------
 Date      Vers.  Comment                                                     Name
 ---------------------------------------------------------------------------------------
 01.10.17  01.00  Created												      Siddiqui
 31.10.23  02.00  Updated												      Siddiqui
 ---------------------------------------------------------------------------------------

"""

if __name__ == "__main__":
    # ==========================================================================================================
    # Notes
    # ==========================================================================================================
    # - continue:    Skip current iteration
    # - break:       Skip all iterations
    # - pass:        Goto next line (NO SKIP)

    max_count = 10
    list1 = [1, 2, 3]
    list2 = [97, 98, 99, 100]
    tuple1 = ((1, 2), (3, 4))
    dict1 = {"x": 1, "y": 2, "z": 3}

    # ==========================================================================================================
    # If Else
    # ==========================================================================================================
    if list1[0] == 0:
        pass
    elif list1[1] == 0:
        pass
    else:
        pass

    # ==========================================================================================================
    # Ternary Operators
    # ==========================================================================================================
    var = list1[0] if list1[0] > 99 else list[1]

    # ==========================================================================================================
    # Condition Chaining
    # ==========================================================================================================
    if list1[0] > list1[1] < list1[2]:  # list1[0] > list1[1] and list1[1] < list1[2]
        pass

    # ==========================================================================================================
    # For
    # ==========================================================================================================
    for element in list1:
        pass

    # ==========================================================================================================
    # For Range
    # ==========================================================================================================
    for element in range(10, 100, 10):
        pass

    # ==========================================================================================================
    # For Enumerate
    # ==========================================================================================================
    for index, value in enumerate(list1):
        pass

    # ==========================================================================================================
    # For Zip
    # ==========================================================================================================
    for element1, element2 in zip(list1, list2):
        pass

    # ==========================================================================================================
    # For Tuple
    # ==========================================================================================================
    for element1, element2 in tuple1:
        pass

    # ==========================================================================================================
    # For Dictionary
    # ==========================================================================================================
    for key, value in dict1.items():
        pass
