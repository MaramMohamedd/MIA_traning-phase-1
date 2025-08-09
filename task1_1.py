#fucntion display : 
def display_gear(grid):
    for i in range(5):
       ele = ""
       for j in range(4):
          ele += grid[i][j]
       print(ele)
       
  # main body        
print("Welcom to our System !")
print('_'*20)
shape = -1 # intial value to enter the loop


#loop for validation
while True :
   try :
      shape = int(input("Enter the gear (0-8):\n"))
      if shape >= 0 and shape <= 8:
         break 
      else :
         print("Gear must be in range from 0 to 8 !")
   except ValueError:
      print("Invalid input : please enter a number (0-8) :")



#my idea is about making a grid like the freq array but instaed of storing the freq -> storing the shape(2d list)
#i know this is not the best solution but due to time i will submit it like this and will improve it later
grid = [] #0 1 2 3 4 5 6 7 8

grid.append([["#","#","#","#" ] , ["#" ," " ," " , "#"] , ["#"," "," ","#"] , ["#"," ", " " , "#"] , ["#", "#","#","#"]])#0
grid.append([[" "," "," ","#" ] , [" " ,"#" ," " , "#"] , ["#"," "," ","#"] , ["#"," ", " " , "#"] , ["#", "#","#","#"]])#1
grid.append([["#","#","#","#" ] , [" " ," " ," " , "#"] , ["#","#","#","#"] , ["#"," ", " " , " "] , ["#", "#","#","#"]])#2
grid.append([["#","#","#","#" ] , [" " ," " ," " , "#"] , ["#","#","#","#"] , [" "," ", " " , "#"] , ["#", "#","#","#"]])#3
grid.append([["#"," "," ","#" ] , ["#" ," " ," " , "#"] , ["#","#","#","#"] , [" "," ", " " , "#"] , [" ", " "," ","#"]])#4
grid.append([["#","#","#","#" ] , ["#" ," " ," " , " "] , ["#","#","#","#"] ,[" " ," " ," " , "#"] , ["#", "#","#","#"]])#5
grid.append([["#","#","#","#" ] , ["#" ," " ," " , " "] , ["#","#","#","#"] ,["#" ," " ," " , "#"] , ["#", "#","#","#"]])#6
grid.append([["#","#","#","#" ] , [" " ," " ," " , "#"] , ["#","#","#","#"] ,[" " ,"#" ," " , " "] , ["#", " "," "," "]])#7
grid.append([["#","#","#","#" ] , ["#" ," " ," " , "#"] , ["#","#","#","#"] ,["#" ," " ," " , "#"] , ["#", "#","#","#"]])#8

 

####
#another idea i can use print("#"*4) for example instead of loop better than O(npower2)
#lis = [[[1,4],[1 , 3 , 5]] , [[4],[5]]  , [[],[]], [[4],[1 , 3 , 5]]] #[cols, rows]->for each number
####
#calling the function to display gear
display_gear(grid[int(shape)])
