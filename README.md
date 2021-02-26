# Brief Summary :

## Question :

1. Uploaded in problems folder

## How I implemented it in short :

1) I wrote classes for car,streets and schedule_per_intersection . 
2) Then read data from all input data files in problems folder
3) Now to finally write schedules for each traffic signals , I found out all the incoming streets for each intersection.
4) Now corresponding to each incoming street at a particular intersection I kept the signal scheduled to green for 1s (in a round robin fashion)   
5) This solution could be improved by also checking if at a particular instant if there is no incoming car at a particular signal then no point of keeping the signal green there
6) The corresponding solution is submitted for the competion , I'll update it for better optimizations later : ) 


## Output :

Uploaded in results folder
