def top_n(items,n):

    """ Return the top n items in a array desc order
    
    Args:
        items(array): list or array like object
        n(int): num of items to return
    
    Return:
        array: top n items, in desc order
         
    Egs:
      >>>top_n([8,3,2,7,4],3)
      [8,7,3]
    """
    for i in range(n): #keep sorting until we have the top n item
        for j in range(len(items)-1-i):
            if items[i] > items[j+1]: #if this item is bigger than next item..
               items[j], items[j+1]=items[j+1],items[j]

    top_n = items[-n:] #set last two items

    return top_n[::-1]

