rm(list=ls())#清空对象

#包下载
installedPackage<-rownames(installed.packages())
# k<-'"'
# k<-paste(k,installedPackage[1],sep = "")
# k<-paste(k,'"',sep = "")
# for (i in 2:length(installedPackage)) {
#   k<-paste(k,',',sep = "")
#   k<-paste(k,'"',sep = "")
#   k<-paste(k,installedPackage[i],sep = "")
#   k<-paste(k,'"',sep = "")
# }
# write.csv(k,"package.csv")

shouldpack<-c("abind","assertthat","backports","BH","bitops","Boruta","broom","callr","car","carData","caret","caTools","cellranger","cli","clipr","colorspace","crayon","curl","data.table","DEoptimR","Deriv","desc","digest","DMwR","dplyr","e1071","ellipsis","evaluate","fansi","farver","forcats","foreach","gdata","generics","ggplot2","glue","gower","GPArotation","gplots","gtable","gtools","haven","hms","installr","ipred","isoband","iterators","jomo","kernlab","labeling","laeken","lava","lifecycle","lme4","lmtest","lubridate","magrittr","maptools","MatrixModels","mice","minqa","mitml","mnormt","ModelMetrics","munsell","neuralnet","nloptr","numDeriv","openxlsx","ordinal","outliers","pan","pbkrtest","pillar","pkgbuild","pkgconfig","pkgload","plogr","plyr","praise","prettyunits","pROC","processx","prodlim","progress","ps","psych","purrr","quantmod","quantreg","R6","randomForest","ranger","RColorBrewer","Rcpp","RcppEigen","readr","readxl","recipes","rematch","reshape","reshape2","rio","rJava","rlang","robustbase","ROCR","rprojroot","rstudioapi","scales","scatterplot3d","sp","SparseM","SQUAREM","stringi","stringr","testthat","tibble","tidyr","tidyselect","timeDate","TTR","ucminf","utf8","varSelRF","vcd","vctrs","VIM","viridisLite","withr","xgboost","xlsx","xlsxjars","xts","zeallot","zip","zoo","base","boot","class","cluster","codetools","compiler","datasets","foreign","graphics","grDevices","grid","KernSmooth","lattice","MASS","Matrix","methods","mgcv","nlme","nnet","parallel","rpart","spatial","splines","stats","stats4","survival","tcltk","tools","translations","utils")

num<-which(!shouldpack%in%installedPackage)
for (i in num) {
  install.packages(shouldpack[i])
}