rf<-randomForest(train$isviolation~.,train[,-c(1,2,3,4)],importance=TRUE,proximity=TRUE,ntree=600,mtry=mtry)
rfpred<-predict(rf,test[-c(1,2,3,4)])
table(test$isviolation,rfpred)
library(pROC)#查看roc曲线
ran_roc <- roc(test$isviolation,as.numeric(rfpred))
plot(ran_roc, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='RF模型测试集ROC曲线,mtry=34,ntree=600')