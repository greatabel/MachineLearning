#ЬиеїЯћГ§
train$isviolation<-as.factor(train$isviolation)
test$isviolation<-as.factor(test$isviolation)
for (i in c(3,4,6,7)) {
  train[,i]<-as.factor(train[,i])
  test[,i]<-as.factor(test[,i])
}


library(caret)
control <- rfeControl(functions=rfFuncs, method="cv", number=10)
rfe.train <- rfe(train[,c(3,4,6,7,9:length(data))], train[,8], sizes=1:(length(data)-4), rfeControl=control)
plot(rfe.train, type=c("g", "o"), cex = 1.0, col = 1:(length(data)-4))
rfe<-predictors(rfe.train)


