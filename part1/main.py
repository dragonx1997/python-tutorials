from source import route
from utils import printResults



if __name__ == "__main__":
    
    param = "quicksort [1,2,3,4,5]"
    givenAnswer = route(param)
    res = [1,2,3,4,5]
    printResults(givenAnswer,res)

    param = "mergesort [3,6,4,6,8,1]"
    givenAnswer = route(param)
    res = [1,3,4,6,6,8]
    printResults(givenAnswer,res)

    param = "pythonsort [5,4,3,2,1]"
    givenAnswer = route(param)
    res = [1,2,3,4,5]
    printResults(givenAnswer,res)

    param = "bucketsort [6,5,3,5,2]"
    givenAnswer = route(param)
    res = [2,3,5,5,6]
    printResults(givenAnswer,res)
