import random

def LRU(pages, capacity, MaxPages):
    s = set()
    indexes = {}#To store the LRU to check
    page_faults = 0 #Imports a random module for randomly generated pages

    #Initialize a For loop to determine each page
    for page in range(MaxPages):
        #If the set is less than the capacity(3), it will add the current page into the set
        if len(s) < capacity:
            #If the number is currently on the page then the statement will return as True
            if pages[page] not in s:
                s.add(pages[page])
                page_faults += 1
            indexes[pages[page]]= page
        #If the set is full, then it will calculate on what is the least recently used page
        #replace the least recently use one for the new one
        else:
            #If the number is currently on the page then the statement will return as True
            if pages[page] not in s:
                lru = float('inf')
                for frame in s:
                    if indexes[frame] < lru:
                        lru= indexes[frame]
                        val = frame
                s.remove(val)
                s.add(pages[page])
                page_faults += 1
            indexes[pages[page]]= page
        print(f"Page: {pages[page]} -> Frames: {list(s)}")

    print(f"\nTotal Page Faults: {page_faults}")


# main code
MaxPages=10
pages = [random.randint(1, 9) for frames in range(MaxPages)]
capacity = 3
LRU(pages, capacity, MaxPages)