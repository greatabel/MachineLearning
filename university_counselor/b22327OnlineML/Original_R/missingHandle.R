#缺失值处理

library(DMwR)#查看缺失值情况，插补
data<-cbind(data[,c(1:3,44,49,50,37,9)],as.data.frame(lapply(data[,-c(1:3,44,49,50,37,9)],as.numeric)))
dataviolation<-data[which(data$isviolation==1),]
dataNoviolation<-data[-which(data$isviolation==1),]
a<-manyNAs(dataviolation,0.2)#找出缺失值大于20%列数的行
b<-manyNAs(dataNoviolation,0.2)
dataviolation<-dataviolation[-a,]
dataNoviolation<-dataNoviolation[-b,]

numviolation <- knnImputation(dataviolation[,-c(1:8)],k=50)#knn插补，基于欧氏距离找到K个与其最近的观测数值，然后对这K个近邻的数据利用距离逆加权得到插补的值
numNoviolation <- knnImputation(dataNoviolation[,-c(1:8)],k=50)

dataviolation<-cbind(dataviolation[,1:8],numviolation)
dataNoviolation<-cbind(dataNoviolation[,1:8],numNoviolation)
data<-rbind(dataviolation,dataNoviolation)

data<-na.omit(data)
write.csv(data,file = "缺失值处理后数据.csv")