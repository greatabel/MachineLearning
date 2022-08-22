#异常值处理
out0<-list()
out1<-list()

a0<-data[which(data$isviolation==0),]
a1<-data[which(data$isviolation==1),]
for (i in c(9:length(data))) {#根据实际情况调整
  out0add <- which((a0[,i]>mean(a0[,i])+2*var(a0[,i])) | (a0[,i]<mean(a0[,i])-2*var(a0[,i])))
  out1add <- which((a1[,i]>mean(a1[,i])+2*var(a1[,i])) | (a1[,i]<mean(a1[,i])-2*var(a1[,i])))
  out0<-c(out0,list(out0add))
  out1<-c(out1,list(out1add))
}

out1_u<-out1[[1]]
for (i in c(1:(length(data)-9+1))) {
  if(length(out1[[i]])<200){
    out1_u<-union(out1_u, out1[[i]])
  }
  
}

out0_u<-out0[[1]]
for (i in c(1:(length(data)-9+1))) {
  if(length(out0[[i]])<2000){
    out0_u<-union(out0_u, out0[[i]])
  }
}

a0<-a0[-out0_u,]
a1<-a1[-out1_u,]
set.seed(1234)
sample1<-sample(nrow(a1),1442,replace = FALSE)
sample0<-sample(nrow(a0),1442,replace = FALSE)
train<-rbind(a0[sample0,],a1[sample1,])
test<-rbind(a0[-sample0,],a1[-sample1,])

write.csv(train,file = "train.csv")
write.csv(test,file = "test.csv")