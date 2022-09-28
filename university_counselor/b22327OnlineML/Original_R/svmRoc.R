library(e1071)
tuned<-tune.svm(isviolation~.,data = train[,-c(1,2,3)],gamma = 10^(-6:1),cost = 10^(-2:2))#调参
svm.tuned<-svm(isviolation~.,data = train[,-c(1,2,3)],gamma=tuned$best.parameters$gamma,cost=tuned$best.parameters$cost)#0.01,10
summary(svm.tuned)
predsvm.tuned<-predict(svm.tuned,test[,-c(1,2,3)])
plot(tuned$performances[,2:3])
library(scatterplot3d)
scatterplot3d(tuned$performances[,1], tuned$performances[,2], tuned$performances[,3],xlab="gamma", ylab="cost", zlab="error")

ran_roc <- roc(train$isviolation,as.numeric(svm.tuned$fitted))
plot(ran_roc, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='SVM模型训练集ROC曲线,gamma=0.1,cost=1')
