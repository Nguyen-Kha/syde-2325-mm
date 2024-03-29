# Python3 program for stable marriage problem 
  
# Number of Men or Women 
# N = 36
  
# This function returns true if  
# woman 'w' prefers man 'm1' over man 'm' 
def wPrefersM1OverM(prefer, w, m, m1): 
      
    # Check if w prefers m over her  
    # current engagment m1 
    for i in range(N): 
          
        # If m1 comes before m in lisr of w,  
        # then w prefers her current engagement, 
        # don't do anything 
        if (prefer[w][i] == m1): 
            return True
  
        # If m cmes before m1 in w's list,  
        # then free her current engagement  
        # and engage her with m 
        if (prefer[w][i] == m): 
            return False
  
# Prints stable matching for N boys and N girls.  
# Boys are numbered as 0 to N-1.  
# Girls are numbereed as N to 2N-1. 
def stableMarriage(prefer): 
      
    # Stores partner of women. This is our output  
    # array that stores paing information.  
    # The value of wPartner[i] indicates the partner  
    # assigned to woman N+i. Note that the woman numbers  
    # between N and 2*N-1. The value -1 indicates  
    # that (N+i)'th woman is free 
    wPartner = [-1 for i in range(N)] 
  
    # An array to store availability of men.  
    # If mFree[i] is false, then man 'i' is free, 
    # otherwise engaged. 
    mFree = [False for i in range(N)] 
  
    freeCount = N 
  
    # While there are free men 
    while (freeCount > 0): 
          
        # Pick the first free man (we could pick any) 
        m = 0
        while (m < N): 
            if (mFree[m] == False): 
                break
            m += 1
  
        # One by one go to all women according to  
        # m's preferences. Here m is the picked free man 
        i = 0
        while i < N and mFree[m] == False: 
            w = prefer[m][i] 
  
            # The woman of preference is free,  
            # w and m become partners (Note that  
            # the partnership maybe changed later).  
            # So we can say they are engaged not married 
            if (wPartner[w - N] == -1): 
                wPartner[w - N] = m 
                mFree[m] = True
                freeCount -= 1
  
            else:  
                  
                # If w is not free 
                # Find current engagement of w 
                m1 = wPartner[w - N] 
  
                # If w prefers m over her current engagement m1, 
                # then break the engagement between w and m1 and 
                # engage m with w. 
                if (wPrefersM1OverM(prefer, w, m, m1) == False): 
                    wPartner[w - N] = m 
                    mFree[m] = True
                    mFree[m1] = False
            i += 1
  
            # End of Else 
        # End of the for loop that goes  
        # to all women in m's list 
    # End of main while loop 
  
    # Prthe solution 
    with open('leftover.txt', 'w') as f:
        f.write("2023 " + ',' + " 2025\n") 
        for i in range(N): 
            f.write(str(i + N) + "\t" + str(wPartner[i]) + '\n') 

########################################################################################################################################################

# Amount of rows/columns (this should be an N x N grid)
N = 36
  
# Driver Code 
# prefer = [[7, 5, 6, 4], [5, 4, 6, 7], # SYDE 2025's preference
#           [4, 5, 6, 7], [4, 5, 6, 7], 
#           [0, 1, 2, 3], [0, 1, 2, 3], # SYDE 2023's preference
#           [0, 1, 2, 3], [0, 1, 2, 3]] 

# Retreive the following data after creating the MAX spreadsheet, and then the G.S. Algo spreadsheet
prefer = [
    # 2025 and who they want. SYDE 25 will get their best one after they look for. on_campus.txt
[55, 45, 47, 60, 63, 41, 62, 50, 58, 61, 66, 68, 69, 71, 43, 70, 38, 42, 44, 46, 54, 57, 65, 67, 37, 48, 49, 39, 52, 56, 64, 36, 40, 51, 53, 59],
[50, 55, 63, 41, 45, 47, 68, 43, 44, 60, 62, 66, 71, 38, 42, 46, 48, 49, 52, 57, 65, 69, 36, 40, 61, 64, 70, 39, 51, 53, 54, 56, 58, 59, 37, 67],
[45, 63, 55, 47, 60, 41, 50, 62, 65, 69, 70, 38, 43, 46, 58, 61, 66, 68, 71, 44, 54, 42, 48, 57, 59, 64, 36, 49, 52, 67, 37, 40, 51, 53, 56, 39],
[55, 63, 41, 50, 45, 47, 60, 71, 43, 62, 66, 68, 70, 44, 57, 65, 61, 38, 40, 42, 46, 48, 49, 52, 53, 58, 64, 69, 36, 51, 54, 56, 39, 59, 67, 37],
[45, 47, 55, 63, 70, 60, 38, 41, 46, 50, 65, 66, 71, 54, 58, 61, 62, 68, 69, 42, 43, 44, 49, 53, 57, 59, 67, 36, 37, 48, 51, 52, 64, 39, 40, 56],
[50, 55, 41, 45, 47, 60, 62, 63, 66, 68, 71, 44, 69, 43, 48, 38, 42, 46, 49, 52, 57, 64, 65, 70, 36, 40, 51, 53, 56, 61, 39, 54, 58, 59, 67, 37],
[63, 45, 55, 50, 60, 61, 62, 65, 69, 70, 41, 47, 71, 38, 46, 66, 68, 43, 44, 54, 58, 42, 48, 57, 59, 64, 36, 40, 49, 52, 67, 37, 51, 53, 56, 39],
[55, 45, 63, 62, 41, 47, 50, 60, 68, 69, 71, 66, 38, 44, 46, 61, 70, 42, 43, 48, 57, 58, 65, 67, 37, 49, 52, 54, 56, 36, 39, 40, 59, 64, 51, 53],
[45, 63, 50, 55, 70, 47, 60, 62, 66, 71, 38, 41, 46, 61, 65, 68, 69, 44, 36, 42, 43, 48, 52, 54, 58, 59, 64, 67, 37, 40, 49, 51, 53, 56, 57, 39],
[55, 63, 41, 45, 60, 62, 47, 50, 61, 68, 69, 71, 43, 57, 58, 65, 66, 70, 38, 44, 46, 42, 48, 54, 67, 37, 40, 49, 52, 56, 64, 36, 39, 53, 59, 51],
[45, 55, 63, 47, 41, 50, 38, 46, 60, 62, 65, 68, 69, 70, 71, 43, 44, 58, 61, 66, 42, 54, 57, 48, 49, 52, 59, 67, 36, 37, 40, 56, 64, 39, 51, 53],
[55, 63, 41, 45, 47, 50, 60, 71, 43, 66, 68, 44, 62, 70, 57, 65, 38, 42, 46, 48, 49, 52, 58, 61, 64, 69, 36, 40, 51, 53, 54, 56, 39, 59, 67, 37],
[55, 41, 62, 47, 50, 60, 63, 45, 68, 71, 43, 57, 66, 69, 44, 58, 61, 65, 38, 42, 46, 48, 40, 49, 52, 54, 56, 67, 70, 36, 37, 39, 64, 51, 53, 59],
[55, 45, 60, 63, 47, 41, 50, 62, 71, 43, 66, 68, 69, 38, 44, 46, 58, 61, 65, 70, 42, 48, 54, 57, 49, 52, 64, 67, 36, 37, 40, 53, 56, 59, 39, 51],
[55, 60, 41, 47, 50, 71, 43, 45, 63, 66, 68, 44, 62, 53, 57, 65, 70, 38, 42, 46, 48, 49, 52, 58, 69, 36, 40, 51, 54, 56, 64, 39, 59, 61, 67, 37],
[55, 63, 45, 41, 47, 50, 62, 38, 46, 60, 65, 69, 70, 71, 61, 66, 68, 43, 44, 54, 57, 58, 42, 48, 40, 49, 52, 59, 67, 36, 37, 56, 64, 39, 51, 53],
[45, 55, 63, 47, 60, 69, 38, 41, 46, 50, 62, 65, 70, 71, 43, 54, 58, 66, 68, 44, 61, 42, 48, 57, 59, 36, 49, 52, 64, 67, 37, 40, 51, 53, 56, 39],
[55, 50, 63, 41, 45, 71, 47, 60, 62, 66, 68, 44, 65, 43, 57, 70, 38, 40, 42, 46, 48, 49, 52, 61, 69, 36, 51, 53, 56, 64, 39, 54, 58, 59, 67, 37],
[55, 41, 50, 60, 63, 45, 47, 62, 43, 66, 68, 71, 44, 57, 69, 48, 61, 65, 38, 40, 42, 46, 49, 52, 58, 64, 70, 53, 54, 56, 36, 39, 51, 67, 37, 59],
[55, 41, 50, 47, 60, 62, 63, 43, 45, 66, 68, 71, 44, 57, 61, 48, 65, 69, 38, 40, 42, 46, 49, 52, 58, 64, 54, 56, 70, 36, 39, 51, 53, 67, 37, 59],
[55, 50, 63, 41, 45, 60, 71, 47, 62, 66, 68, 44, 43, 57, 38, 40, 42, 46, 48, 49, 52, 65, 69, 70, 53, 56, 61, 36, 39, 51, 54, 58, 64, 67, 37, 59],
[55, 60, 47, 41, 45, 50, 62, 63, 71, 43, 66, 68, 69, 44, 65, 38, 42, 46, 48, 57, 58, 61, 64, 70, 36, 49, 52, 53, 54, 40, 51, 56, 59, 67, 37, 39],
[50, 55, 41, 45, 47, 62, 63, 68, 44, 60, 66, 71, 43, 48, 69, 38, 42, 46, 49, 52, 57, 64, 65, 70, 36, 40, 56, 61, 39, 51, 53, 54, 58, 59, 67, 37],
[55, 47, 60, 41, 45, 50, 63, 66, 71, 43, 68, 44, 62, 42, 49, 57, 58, 70, 38, 46, 48, 52, 54, 65, 69, 39, 40, 51, 53, 56, 61, 64, 67, 36, 37, 59],
[55, 50, 62, 63, 41, 45, 47, 60, 71, 66, 68, 44, 61, 65, 69, 38, 42, 43, 46, 48, 57, 64, 70, 36, 40, 49, 52, 51, 53, 54, 56, 58, 59, 67, 37, 39],
[66, 47, 50, 60, 71, 55, 63, 68, 41, 42, 43, 44, 45, 48, 49, 52, 62, 38, 39, 40, 46, 51, 53, 57, 69, 36, 37, 54, 56, 58, 65, 67, 70, 61, 64, 59],
[55, 63, 41, 45, 47, 50, 60, 62, 43, 66, 68, 71, 44, 57, 65, 69, 38, 42, 46, 48, 58, 61, 70, 40, 49, 52, 54, 36, 56, 64, 67, 37, 39, 51, 53, 59],
[55, 63, 45, 60, 41, 47, 62, 50, 68, 69, 71, 43, 58, 66, 70, 38, 44, 46, 57, 61, 65, 42, 48, 54, 67, 37, 49, 52, 56, 36, 39, 40, 53, 59, 64, 51],
[55, 41, 50, 60, 62, 63, 45, 47, 68, 71, 43, 57, 66, 44, 69, 48, 58, 61, 65, 38, 40, 42, 46, 49, 52, 56, 70, 39, 53, 54, 64, 67, 36, 37, 51, 59],
[55, 63, 45, 41, 47, 50, 62, 60, 71, 65, 66, 68, 69, 38, 43, 44, 46, 57, 61, 70, 42, 48, 58, 40, 49, 52, 54, 67, 36, 37, 56, 59, 64, 39, 51, 53],
[55, 41, 60, 63, 45, 47, 50, 62, 68, 71, 43, 66, 44, 57, 61, 56, 58, 70, 38, 42, 46, 48, 49, 52, 65, 69, 39, 40, 53, 54, 64, 67, 36, 37, 51, 59],
[50, 55, 71, 41, 47, 60, 63, 66, 68, 44, 45, 62, 65, 43, 57, 61, 38, 40, 42, 46, 48, 49, 52, 53, 64, 69, 70, 36, 51, 56, 39, 54, 58, 59, 67, 37],
[50, 47, 55, 62, 63, 66, 71, 41, 45, 48, 60, 68, 70, 36, 39, 42, 43, 44, 49, 51, 52, 53, 64, 69, 37, 38, 40, 46, 56, 57, 65, 54, 58, 59, 61, 67],
[55, 45, 47, 50, 60, 62, 63, 71, 41, 66, 68, 44, 69, 38, 42, 43, 46, 48, 61, 64, 65, 70, 36, 49, 52, 57, 40, 51, 53, 54, 56, 58, 59, 67, 37, 39],
[55, 50, 62, 63, 45, 47, 71, 41, 60, 66, 69, 44, 68, 38, 42, 43, 46, 48, 57, 65, 40, 49, 52, 61, 70, 54, 56, 58, 67, 36, 37, 39, 51, 53, 59, 64],
[55, 60, 41, 47, 62, 45, 50, 63, 68, 71, 43, 66, 44, 57, 58, 69, 38, 42, 46, 48, 61, 65, 49, 52, 54, 56, 67, 70, 36, 37, 39, 40, 53, 64, 51, 59],

    # SYDE 2023 and who they want
[32, 1, 25, 22, 8, 31, 33, 5, 24, 14, 17, 4, 10, 19, 23, 2, 3, 11, 20, 21, 26, 7, 29, 34, 12, 18, 35, 13, 15, 16, 0, 30, 6, 28, 9, 27],
[25, 32, 1, 22, 8, 31, 33, 4, 5, 10, 23, 24, 7, 14, 17, 19, 2, 20, 26, 29, 34, 0, 3, 11, 12, 21, 35, 13, 15, 18, 16, 30, 9, 27, 28, 6],
[1, 25, 32, 22, 8, 4, 10, 31, 33, 5, 24, 2, 14, 17, 19, 23, 7, 15, 20, 26, 29, 34, 3, 11, 16, 21, 12, 13, 18, 35, 0, 6, 30, 9, 27, 28],
[25, 32, 1, 22, 31, 5, 8, 23, 33, 14, 17, 19, 24, 4, 10, 20, 3, 7, 11, 26, 34, 2, 12, 18, 21, 29, 35, 0, 30, 13, 15, 28, 16, 9, 27, 6],
[25, 1, 32, 22, 31, 5, 8, 17, 19, 24, 33, 14, 20, 23, 3, 10, 26, 34, 4, 11, 18, 29, 2, 7, 12, 21, 15, 35, 13, 28, 30, 0, 16, 6, 9, 27],
[1, 22, 25, 32, 19, 31, 5, 14, 17, 23, 24, 33, 3, 8, 10, 20, 26, 4, 11, 12, 18, 29, 2, 7, 21, 30, 34, 35, 15, 28, 0, 13, 9, 16, 27, 6],
[25, 1, 32, 22, 31, 33, 5, 8, 23, 24, 4, 10, 14, 17, 19, 20, 26, 34, 2, 3, 7, 11, 21, 29, 12, 18, 35, 0, 13, 15, 16, 30, 28, 6, 9, 27],
[1, 25, 32, 22, 14, 19, 23, 31, 5, 33, 3, 8, 10, 11, 17, 24, 26, 2, 4, 18, 20, 21, 12, 29, 34, 35, 7, 13, 30, 0, 15, 16, 28, 9, 27, 6],
[1, 25, 22, 32, 31, 5, 33, 8, 14, 17, 19, 23, 24, 10, 20, 3, 4, 11, 26, 34, 2, 7, 18, 21, 29, 12, 35, 13, 15, 30, 0, 16, 28, 6, 9, 27],
[1, 8, 22, 25, 32, 10, 33, 2, 4, 5, 17, 23, 24, 31, 7, 14, 19, 20, 26, 29, 3, 11, 15, 34, 13, 18, 21, 0, 12, 16, 35, 6, 30, 9, 27, 28],
[1, 25, 32, 22, 8, 4, 10, 31, 33, 5, 24, 2, 14, 17, 19, 23, 7, 15, 20, 26, 29, 34, 3, 11, 16, 21, 12, 13, 18, 35, 0, 6, 30, 9, 27, 28],
[25, 1, 32, 22, 23, 31, 33, 4, 5, 8, 10, 14, 19, 24, 17, 26, 2, 3, 11, 20, 21, 29, 34, 7, 12, 18, 35, 0, 13, 15, 16, 30, 28, 9, 27, 6],
[25, 32, 1, 22, 5, 31, 33, 8, 19, 24, 14, 17, 23, 10, 20, 26, 34, 2, 3, 4, 7, 11, 18, 21, 29, 12, 35, 13, 15, 0, 16, 28, 30, 6, 9, 27],
[25, 1, 32, 22, 31, 5, 23, 33, 8, 14, 17, 19, 24, 4, 10, 20, 3, 11, 26, 34, 2, 7, 18, 21, 29, 12, 35, 0, 13, 15, 30, 16, 28, 6, 9, 27],
[1, 25, 32, 22, 31, 17, 5, 8, 19, 24, 33, 14, 20, 23, 3, 10, 26, 34, 4, 11, 18, 29, 2, 7, 12, 21, 15, 35, 13, 28, 30, 0, 6, 16, 9, 27],
[25, 32, 1, 22, 31, 5, 8, 33, 14, 17, 23, 24, 4, 19, 3, 11, 20, 2, 10, 21, 26, 34, 7, 18, 29, 12, 35, 0, 13, 15, 16, 30, 28, 6, 9, 27],
[25, 1, 32, 22, 31, 5, 8, 33, 14, 17, 19, 23, 24, 10, 20, 3, 4, 11, 26, 34, 2, 7, 18, 21, 29, 12, 35, 13, 15, 30, 0, 16, 28, 6, 9, 27],
[25, 32, 1, 22, 31, 14, 5, 8, 33, 4, 17, 23, 24, 3, 19, 20, 11, 21, 2, 10, 18, 26, 34, 7, 29, 35, 12, 13, 30, 0, 15, 16, 28, 6, 9, 27],
[25, 1, 32, 22, 4, 8, 10, 23, 31, 33, 2, 5, 14, 19, 24, 17, 26, 3, 7, 11, 15, 16, 20, 21, 29, 34, 0, 12, 13, 18, 35, 6, 30, 9, 27, 28],
[1, 22, 25, 32, 17, 23, 31, 3, 10, 14, 19, 20, 24, 33, 5, 8, 11, 26, 29, 4, 7, 12, 18, 30, 34, 2, 15, 21, 28, 35, 0, 13, 9, 16, 27, 6],
[25, 32, 1, 22, 31, 5, 8, 33, 14, 17, 19, 23, 24, 10, 20, 3, 4, 7, 11, 26, 34, 2, 12, 18, 21, 29, 30, 35, 0, 13, 15, 28, 16, 9, 27, 6],
[1, 25, 32, 22, 31, 19, 5, 14, 17, 23, 24, 33, 3, 8, 10, 20, 26, 4, 11, 12, 18, 29, 34, 2, 7, 21, 35, 15, 28, 30, 0, 13, 9, 16, 27, 6],
[25, 1, 32, 22, 4, 8, 10, 23, 2, 14, 19, 31, 33, 5, 24, 26, 0, 3, 7, 11, 12, 17, 21, 29, 35, 13, 15, 16, 18, 20, 34, 30, 9, 27, 28, 6],
[1, 32, 25, 22, 8, 31, 33, 4, 5, 10, 24, 2, 14, 17, 19, 23, 3, 7, 11, 20, 21, 26, 29, 34, 15, 16, 12, 13, 18, 35, 0, 6, 30, 9, 27, 28],
[25, 1, 32, 22, 14, 23, 31, 33, 5, 8, 19, 24, 4, 17, 20, 21, 26, 2, 3, 10, 11, 18, 35, 7, 12, 13, 29, 34, 0, 30, 15, 16, 28, 9, 27, 6],
[1, 25, 32, 8, 22, 31, 19, 24, 33, 4, 10, 2, 5, 17, 3, 7, 23, 26, 29, 0, 11, 12, 14, 15, 18, 20, 21, 34, 6, 9, 13, 30, 35, 16, 28, 27],
[32, 1, 22, 25, 24, 33, 5, 8, 19, 31, 17, 26, 34, 7, 10, 12, 14, 20, 23, 29, 2, 3, 4, 18, 21, 35, 11, 15, 0, 13, 28, 30, 9, 16, 6, 27],
[1, 25, 32, 8, 22, 10, 17, 24, 31, 33, 2, 3, 4, 5, 19, 20, 23, 26, 29, 7, 11, 14, 15, 34, 18, 6, 12, 13, 21, 0, 9, 16, 30, 35, 27, 28],
[32, 1, 22, 25, 31, 33, 5, 8, 24, 19, 14, 17, 23, 2, 3, 4, 10, 11, 21, 18, 20, 26, 7, 29, 34, 12, 13, 35, 0, 15, 16, 30, 6, 28, 9, 27],
[1, 25, 32, 22, 31, 8, 4, 10, 17, 24, 33, 2, 5, 14, 19, 3, 23, 26, 29, 11, 15, 20, 21, 34, 7, 12, 16, 18, 6, 13, 35, 0, 9, 28, 30, 27],
[25, 32, 1, 22, 31, 5, 8, 23, 33, 14, 17, 19, 24, 4, 20, 3, 10, 11, 26, 34, 2, 7, 18, 21, 29, 12, 35, 0, 13, 15, 30, 16, 28, 6, 9, 27],
[25, 32, 1, 22, 8, 31, 33, 4, 5, 10, 23, 24, 7, 14, 17, 19, 2, 20, 26, 29, 34, 0, 3, 11, 12, 21, 35, 13, 15, 18, 16, 30, 9, 27, 28, 6],
[1, 25, 22, 32, 31, 5, 33, 8, 14, 17, 19, 23, 24, 10, 20, 3, 4, 7, 11, 26, 2, 12, 18, 21, 29, 34, 35, 30, 0, 13, 15, 28, 16, 9, 27, 6],
[1, 25, 32, 22, 5, 8, 33, 10, 24, 31, 2, 4, 7, 19, 34, 14, 17, 21, 23, 26, 29, 12, 15, 16, 18, 20, 0, 3, 11, 13, 35, 6, 9, 27, 28, 30],
[32, 1, 8, 25, 4, 22, 10, 31, 33, 2, 3, 5, 14, 17, 23, 24, 11, 7, 15, 19, 20, 26, 29, 16, 21, 34, 0, 6, 13, 18, 12, 30, 35, 9, 27, 28],
[25, 32, 1, 22, 31, 33, 5, 8, 14, 17, 23, 24, 19, 20, 3, 4, 10, 11, 34, 7, 21, 26, 29, 2, 12, 18, 35, 13, 15, 30, 0, 16, 28, 6, 9, 27],

]
  
stableMarriage(prefer) 
  
# This code is contributed by Mohit Kumar 
