#function for printing palindromic Pyramid
def palindromicPyramid(rows):
    #outer loop for each row
    for i in range(0,rows+1):

        #1st inner loop for printing blank spaces in each row
        for j in range(i,rows):
            print(" ",end=" ")

        #2nd inner loop for printing increasing half in each row
        for j in range(1,i+1):
            print(j,end=" ")

        #3rd inner loop for printing decreasing half in each row
        for j in range(i-1,0,-1):
            print(j,end=" ")

        #print new line character for next row
        print()
                
#input
n=int(input("Enter the number of rows :"))

#function call
palindromicPyramid(n)
