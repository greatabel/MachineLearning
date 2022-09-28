#读入表，并进行表的连接

violationData$isviolation<-1
colnames(violationData)<-c("Stkcd","Accper","isviolation")

library(openxlsx)
DebtPayData<-read.xlsx("偿债能力092934941/FI_T1.xlsx")
DebtPayData<-DebtPayData[which(DebtPayData$`报表类型编码'`=="A"),]
DebtPayData<-DebtPayData[which(substring(DebtPayData$`截止日期'`,6,6)==1),]#留下月份为12的（第6位字符为1)
names(DebtPayData)[4]<-paste("Typrep ")
DebtPayData$`Typrep `<-substring(DebtPayData$`Typrep `,1,1)
names(DebtPayData)[1]<-paste("Stkcd")
names(DebtPayData)[2]<-paste("Accper")
DebtPayData<-DebtPayData[,-3]
DebtPayData$Accper<-substring(DebtPayData$Accper,1,4)
DebtPayData$`Typrep `<-as.factor(DebtPayData$`Typrep `)
DebtViolation<-merge(DebtPayData,violationData,by=c("Stkcd","Accper"),all.x = TRUE)
DebtViolation$isviolation[which(is.na(DebtViolation$isviolation))]<-0

runningData<-read.xlsx("经营能力093937716/FI_T4.xlsx")
runningData<-runningData[which(runningData$Typrep=="A"),]
runningData<-runningData[,-3]
runningData<-runningData[which(substring(runningData$Accper,6,6)==1),]
runningData$Accper<-substring(runningData$Accper,1,4)
debtRunning<-merge(DebtViolation,runningData,by=c("Stkcd","Accper"),all.x = TRUE)  

profit<-read.xlsx("盈利能力094732386/FI_T5.xlsx")
profit<-profit[which(profit$Typrep=="A"),]
profit<-profit[which(substring(profit$Accper,6,6)==1),]
profit$Accper<-substring(profit$Accper,1,4)
profit<-profit[,-3]
debtRunningProfit<-merge(debtRunning,profit,by=c("Stkcd","Accper"),all.x = TRUE) 

develop<-read.xlsx("发展能力094443003/FI_T8.xlsx")
develop<-develop[which(develop$Typrep=="A"),]
develop<-develop[which(substring(develop$Accper,6,6)==1),]
develop$Accper<-substring(develop$Accper,1,4)
develop<-develop[,-3]
debtRunningProfitDevelop<-merge(debtRunningProfit,develop,by=c("Stkcd","Accper"),all.x = TRUE) 

risk<-read.xlsx("风险水平095733317/FI_T7.xlsx")
risk<-risk[which(risk$Typrep=="A"),]
risk<-risk[which(substring(risk$Accper,6,6)==1),]
risk$Accper<-substring(risk$Accper,1,4)
risk<-risk[,-3]
debtRunningProfitDevelopRisk<-merge(debtRunningProfitDevelop,risk,by=c("Stkcd","Accper"),all.x = TRUE) 

perstock<-read.xlsx("每股指标073335879/FI_T9.xlsx")
perstock<-perstock[which(perstock$Typrep=="A"),]
perstock<-perstock[which(substring(perstock$Accper,6,6)==1),]
perstock$Accper<-substring(perstock$Accper,1,4)
perstock<-perstock[,-3]
debtRunningProfitDevelopRiskPerstock<-merge(debtRunningProfitDevelopRisk,perstock,by=c("Stkcd","Accper"),all.x = TRUE)

publish<-read.xlsx("披露财务指标073433552/FI_T2.xlsx")
publish<-publish[which(substring(publish$Accper,6,6)==1),]
publish$Accper<-substring(publish$Accper,1,4)
debtRunningProfitDevelopRiskPerstockPublish<-merge(debtRunningProfitDevelopRiskPerstock,publish,by=c("Stkcd","Accper"),all.x = TRUE)

distribution<-read.xlsx("股利分配101510228/FI_T11.xlsx")
distribution<-distribution[which(distribution$Typrep=="A"),]
distribution<-distribution[which(substring(distribution$Accper,6,6)==1),]
distribution$Accper<-substring(distribution$Accper,1,4)
distribution<-distribution[,-3]
debtRunProfDeveRiskPstockPublDist<-merge(debtRunningProfitDevelopRiskPerstockPublish,distribution,by=c("Stkcd","Accper"),all.x = TRUE)

#审计意见表一张最多6年数据
audit<-read.xlsx("审计意见表文件075644828/FIN_Audit.xlsx")
audit02<-read.xlsx("审计意见表文件075644828/FIN_Audit02.xlsx")
audit<-rbind(audit,audit02)
audit<-audit[which(substring(audit$Accper,6,6)==1),]
audit$Accper<-substring(audit$Accper,1,4)
audit<-audit[!duplicated(audit),]
data<-merge(debtRunProfDeveRiskPstockPublDist,audit,by=c("Stkcd","Accper"),all.x = TRUE)
data$Audittyp[which(data$Audittyp=="无保留意见加事项段 ")]<-"无保留意见加事项段"

stockstruct<-read.xlsx("股本结构文件091030561/CG_Capchg.xlsx")
names(stockstruct)[2]<-paste("Accper")
stockstruct<-stockstruct[which(substring(stockstruct$Accper,6,6)==1),]
stockstruct$Accper<-substring(stockstruct$Accper,1,4)
stockstruct$Nshrttl<-as.numeric(stockstruct$Nshrttl)
stockstruct$Nshrstt<-as.numeric(stockstruct$Nshrstt)
stockstruct$Nshrsms<-as.numeric(stockstruct$Nshrsms)
stockstruct$国有股份占比=stockstruct$Nshrstt/stockstruct$Nshrttl
stockstruct$监管层股份占比=stockstruct$Nshrsms/stockstruct$Nshrttl
stockstruct<-stockstruct[,-c(4,5)]
data<-merge(data,stockstruct,by=c("Stkcd","Accper"),all.x = TRUE)

CR<-read.xlsx("十大股东股权集中文件205856346/HLD_CR.xlsx")
names(CR)[2]<-paste("Accper")
CR<-CR[which(substring(CR$Accper,6,6)==1),]
CR$Accper<-substring(CR$Accper,1,4)
data<-merge(data,CR,by=c("Stkcd","Accper"),all.x = TRUE)


Ybasic<-read.xlsx("治理综合信息文件082816965/CG_Ybasic.xlsx")
Ybasic02<-read.xlsx("治理综合信息文件082816965/CG_Ybasic02.xlsx")
Ybasic<-rbind(Ybasic,Ybasic02)
names(Ybasic)[2]<-paste("Accper")
Ybasic<-Ybasic[which(substring(Ybasic$Accper,6,6)==1),]
Ybasic$Accper<-substring(Ybasic$Accper,1,4)
data<-merge(data,Ybasic,by=c("Stkcd","Accper"),all.x = TRUE)

data$Excuhldn<-as.numeric(data$Excuhldn)
data$Mngmhldn<-as.numeric(data$Mngmhldn)
data$ExcuhldnRate<-data$Excuhldn/data$Nshrttl
data$MngmhldnRate<-data$Mngmhldn/data$Nshrttl
data<-data[,-c(56,57)]

Director<-read.xlsx("高管个人资料文件091323449/CG_Director.xlsx")
names(Director)[2]<-paste("Accper")
Director<-Director[,c(1,2,8)]
Director<-Director[-c(1,2),]
Director<-Director[which(substring(Director$Accper,6,6)==1),]
Director$Accper<-substring(Director$Accper,1,4)
Director$D0501b<-as.numeric(Director$D0501b)
Director<-aggregate(D0501b~Stkcd+Accper,Director,mean)

data<-merge(data,Director,by=c("Stkcd","Accper"),all.x = TRUE)

#加入是否ST
isst1<-read.xlsx("审计意见表文件075644828/FIN_Audit1.xlsx","sheet1")
isst2<-read.xlsx("审计意见表文件075644828/FIN_Audit2.xlsx")
isst<-rbind(isst1,isst2)
isst<-isst[which(substring(isst$Accper,6,6)==1),]#留下月份为12的（第6位字符为1)
isst$Accper<-substring(isst$Accper,1,4)
st<-which(substring(isst$Stknme,1,3)=="*ST"|substring(isst$Stknme,1,2)=="ST")
isst$isst<-0
isst$isst[st]<-1

data<-merge(data,isst,by=c("Stkcd","Accper"),all.x = TRUE)
data$isst<-as.factor(data$isst)
data<-data[!duplicated(data),]#去除重复行
names(data)[3]<-"Typrep"
a<-ls()
rm(list=a[which(a!='data')])#删除多余对象，保留需要对象
rm(a)



data<-data[,-c(15,16,19,21,23,26,27,28,30)]#去除无用列
write.csv(data,file = "集成数据.csv")