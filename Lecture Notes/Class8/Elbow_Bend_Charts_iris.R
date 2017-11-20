iris # Chosen dataset
iris <- iris[,-5]
install.packages("GMD") # Needed package
require("GMD")

dist.obj <- dist(iris[,1:4],method="manhattan") # Defining distance object and method
hclust.obj <- hclust(dist.obj) # Creating clusters
css.obj <- css.hclust(dist.obj,hclust.obj) # Creating multi object
names(css.obj)
elbow.obj <- elbow.batch(css.obj) # Creating elbow object
print(elbow.obj)
plot(css.obj,elbow.obj=NULL)

#clustering with more relaxed thresholds (resulting a smaller "good" k)
elbow.obj2 <- elbow(css.obj,ev.thres=0.90,inc.thres=0.05) 
print(elbow.obj2)


##Bend graph
iris # Chosen dataset
iris <- iris[,-5] # Dropping last column
iris
wss <- nrow((iris)-1)*sum(apply(iris,2,var)) 
for (i in 2:15) 
{
  wss[i] <- sum(kmeans(iris,centers=i)$withinss) # Within Sum of Squared for 
                                                 # different number of clusters
}  

plot(1:15, wss, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares")

