# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    #Base case of the sequeneces of length 1
    if len(sequence) == 1:
        return [sequence]
    
    #Recursive call to get persumations with sequences less the first character
    permutations = get_permutations(sequence[1:])
    
    #First character of sequences
    char = sequence[0]
    #Result array
    result = []

    #To insert the first character of the permutations string to results
    for permutation in permutations:
        for i in range(len(permutations) + 1):
            #i starts at 0 and goes to range + 1
            #The first result permutation for each recurvsice result will always have the char as the 
            #Frist letter in the results array
            result.append(permutation[:i]+char+permutation[i:])
    
    #Return the result of the recursive calls
    #Egs: the results for a string length 3 will have 2 recursive calls
    #egs get_perm('abc')
    #1--> first call ['c] #base case
    #2--> second call, first recursive call results = ['bc', 'cb']
    #3--> third call, second recurisve call res = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
    return result

print(get_permutations('abc'))

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

