#### kmeans (Euclidean Distance)
iris # Chosen dataset
iris <- iris[,-5] # Dropping last column
iris # New dataset
?kmeans # What is kmean?
km.out <- kmeans(iris,3,nstart=10) #nstart tells how many times algorithm
# starts from beginning since the final answers is related to initial assignments.
names(km.out)
km.out$cluster # kmeans results
plot(iris, col=(km.out$cluster), main="K-mean result with k=3") #Scatterplot matrix


#### Hierarchical clustering
iris=scale(iris) #Scaling the data

hc.complete=hclust(dist(iris),method="complete") # Complete linkage type
hc.average=hclust(dist(iris),method="average")  # Average linkage type

par(mfrow=c(1,2)) #Plotting in a matrix form
plot(hc.complete,main='Complete')
plot(hc.average,main='Average')

cutree(hc.complete,3)
cutree(hc.average,3)


