CALCULATING DISTANCES AND SHORTEST PATH BETWEEN VERTICES USING DIJKSTRA'S ALGORITHM

A complete function in Python with file handling, integer parsing and text output that reads a text file representing a weighted, directed graph that contains lines of integers to return shortest path and its distance between each pair of vertices.

Python, heapq

FEATURES ---  

Integer Splitting/Parsing --> File handling that involves splitting integers in the file by line and parsing each one as an integer representing number of vertices, edges or information about the edge

Function Definition --> Implementation of Dijkstra's algorithm which initializes distance from source vertex, forms heap from queue of distances and recursively pops heap to find shortest distance

Path Function --> Function with initialized path representing shortest path between pair of vertices which iteratively appends each vertex to the path

Edge Parsing --> Function which parses lines containing information about the edge with line's first two numbers representing index of endpoints of the edge

File Handling/Text Output --> Implementation of file handling that involves opening text file, splitting its integers to parse them and returning text output of shortest path and distance between pairs of vertices

