I found the location of each tile in a 12-by-12 grid by computing the graph-theoretic distance of the tile from each corner. If the distance from corner 0,0 is n and the distance from corner 0,1 is m, then the distance from the top row is (m+n-c)/2 for some constant c. Knowing that tiles x and y share an edge e and knowing the locations of x and y, then the location of edge e can be written as the average, (loc(x) + loc(y))/2 . Multiplying all the locations by 8 should leave 8 empty spaces between each pair of edges..
 
We can locate each # in the final 8*12 grid as follows:
from the location of each # in the tile, we compute the distance to each edge. 
Given the distances from the edges in the final 8*12 grid, we assign to this # a location in the final grid.
 
I.e., I think one can avoid all the group theory (flipping, rotating) completely, and just compute location from "distance to fixed points". 
