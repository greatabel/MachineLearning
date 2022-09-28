#mtry È·¶¨

n<-length(names(train[,-c(1,2,3,4)]))     #¼ÆËãÊý¾Ý¼¯ÖÐ×Ô±äÁ¿¸öÊý£¬µÈÍ¬n=ncol(train_data)
rate=1     #ÉèÖÃÄ£ÐÍÎóÅÐÂÊÏòÁ¿³õÊ¼Öµ

for(i in 1:(n-1)){
  set.seed(3823)
  rf_train<-randomForest(train$isviolation~.,data=train[,-c(1,2,3,4)],mtry=i,ntree=600)
  rate[i]<-mean(rf_train$err.rate)   #¼ÆËã»ùÓÚOOBÊý¾ÝµÄÄ£ÐÍÎóÅÐÂÊ¾ùÖµ
  #print(rf_train)    
}

plot(rate)
mtry<-which(rate==min(rate),arr.ind=TRUE)#×îÐ¡Îó²îµÄµã