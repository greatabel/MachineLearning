#违规分条
#xlsx读取，防止数字格式变化
library(openxlsx)
Violation01<- read.xlsx("违规信息总表073840877/STK_Violation_Main.xlsx", sheet = 3)
Violation02<- read.xlsx("违规信息总表073840877/STK_Violation_Main.xlsx", sheet = 2)
Violation<-rbind(Violation01,Violation02)
Violation<-Violation[,c(2,7)]
#Violation$ViolationYear<-as.character(Violation$ViolationYear)
Violationbackup<-Violation
data<-Violation[1,]

#循环体，开始违规分条
i<-1:2
while (length(i)>0) {
  i<-which(nchar(Violation$ViolationYear)>4)#选出年份大于4位数的
  newviolation<-Violation[-i,]
  Violationqian4wei<-Violation[i,]
  Violationqian4wei$ViolationYear<-substring(Violationqian4wei$ViolationYear,1,4)#取前4位
  newviolation<-rbind(newviolation,Violationqian4wei)
  
  Violationhounwei<-Violation[i,]
  Violationhounwei$ViolationYear<-sub('^.....','',Violationhounwei$ViolationYear)#删除前5位字符串
  Violation<-Violationhounwei
  data<-rbind(data,newviolation)
  i<-which(nchar(Violation$ViolationYear)>4)#选出年份大于4位数的
}
violationData<-data[!duplicated(data),]#去除重复行
violationData<-violationData[-1,]#去除第一行
a<-ls()
rm(list=a[which(a!='violationData')])#删除多余对象，保留需要对象
rm(a)

write.csv(violationData,file = "violation.csv")
violationData<-violationData[which(violationData$ViolationYear>2009),]#筛选出年份大于2009的，应该在输出前调用
