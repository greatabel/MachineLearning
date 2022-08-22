#随机森林

library(randomForest)
train0<-train[,rfe]

train<-cbind(train[,c(1,2,5,8)],train0)
test0<-test[,rfe]
test<-cbind(test[,c(1,2,5,8)],test0)
rf<-randomForest(train$isviolation~.,train[,-c(1,2,3,4)],importance=TRUE,proximity=TRUE,ntree=1000)
plot(rf)#确定ntree