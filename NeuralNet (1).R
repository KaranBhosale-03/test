library(neuralnet)
library(caret)
library(forecast)

### The cheese example

df <- read.csv("/Users/karanbhosale/Documents/Machine learning/CheeseData.csv")

df$Like <- ifelse(df$Acceptance=="like",1,0)

set.seed(1)
nn <- neuralnet(Like ~ Fat + Salt, data = df, linear.output=FALSE, hidden = 3)

# display weights
nn$weights

# plot network
plot(nn)


## use compute() function to predict for neural nets
predict <- compute(nn, df[,2:3])
confusionMatrix(relevel(as.factor(ifelse(predict$net.result>0.5, "like", "dislike")),ref="like"), 
                relevel(as.factor(df$Acceptance),ref="like"))




### Toyota Practice (Practice 1 in lecture notes)

toyota.df <- read.csv("/Users/karanbhosale/Documents/Machine learning/ToyotaCorolla (1).csv")


varlist<-c(3,4,9,12,14,17,19,21,25,26,28,30,34,39)

# partition
train.index <- sample(rownames(toyota.df), 0.6*dim(toyota.df)[1])  
valid.index <- setdiff(rownames(toyota.df), train.index)  
train.df <- toyota.df[train.index, varlist]
valid.df <- toyota.df[valid.index, varlist]

# normalize
norm.values <- preProcess(toyota.df[,varlist], method="range")
train.norm.df <- predict(norm.values, train.df)
valid.norm.df <- predict(norm.values, valid.df)

# 1 hidden layer with 2 nodes
nn1 <- neuralnet(Price ~ ., data = train.norm.df, linear.output = TRUE, hidden = 2)

plot(nn1)

prediction1<-compute(nn1, valid.norm.df)

# RMSE and other measures
accuracy(prediction1$net.result[,1], valid.norm.df$Price)

# 1 hidden layer with 5 nodes
nn2 <- neuralnet(Price ~ ., data = train.norm.df, linear.output = TRUE, hidden =5)

plot(nn2)

prediction2<-compute(nn2, valid.norm.df)

# RMSE and other measures
accuracy(prediction2$net.result[,1], valid.norm.df$Price)

# 2 hidden layers with 5 nodes in each
nn3 <- neuralnet(Price ~ ., data = train.norm.df, linear.output = TRUE, hidden = c(5,5))

plot(nn3)

prediction3<-compute(nn3, valid.norm.df)

# RMSE and other measures
accuracy(prediction3$net.result[,1], valid.norm.df$Price)

## feel free to try other structures :)

