#mtry 确定

n<-length(names(train[,-c(1,2,3,4)]))     #计算数据集中自变量个数，等同n=ncol(train_data)
rate=1     #设置模型误判率向量初始值

for(i in 1:(n-1)){
  set.seed(3823)
  rf_train<-randomForest(train$isviolation~.,data=train[,-c(1,2,3,4)],mtry=i,ntree=600)
  rate[i]<-mean(rf_train$err.rate)   #计算基于OOB数据的模型误判率均值
  #print(rf_train)    
}

plot(rate)
mtry<-which(rate==min(rate),arr.ind=TRUE)#最小误差的点%      