1. make a function of factorization. 
2. The factorization function should factorize each number
3. looping start from 1 to desired number (20 in the problem)
    * i = 1; result = 1
    * factorize i
    * if result / factorized\_i[i-th member] is integer -> skip multiplication, continue to another member
    * result = result * factorized\_i[i-th member]
    * continue looping, i = i + 1, stop if i == desired number (20)
