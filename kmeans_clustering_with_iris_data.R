##### iris데이터를 가져와서 k-means clustering 
df <- iris
df_kmeans <- kmeans(df[,3:4],3)
View(df)
df_kmeans

##### 원래 관측치와 비교하여 얼마나 정확하게 분류했는지 정확성 확인하기
table(df_kmeans$cluster, df$Species)

##### 정확도 측정
accurancy_df <- (50+48+44)/150
accurancy_df

##### 그래프로 그려주기
install.packages("ggplot2")
library(ggplot2)
plot1 <- ggplot(data=df,aes(x=df$Petal.Length,y=df$Petal.Width,color=df$Species))+geom_point()
plot1

##### 군집의 중심 확인하기 
df_kmeans$centers
df_kmeans_center <- as.data.frame(df_kmeans$centers)

plot2 <- plot1 + geom_point(data = df_kmeans_center, aes(x=df_kmeans_center$Petal.Length, y=df_kmeans_center$Petal.Width,color='Center'),size=40,alpha=0.1)
plot2

##### 오류 데이터를 그래프에 표시하기 
df$cluster <- df_kmeans$cluster
View(df)
df_table <- as.matrix.data.frame(table(df$Species,df$cluster))
df_table

which_setosa <- which.max(df_table[1,])
which_versicolor <- which.max(df_table[2,])
which_virginica <- which.max(df_table[3,])

for(j in 1:150){
  if(df4[j,5]=='setosa'&&df4[j,6]==which_setosa){
    df4[j,7]='true'
  }else if(df4[j,5]=='versicolor'&&df4[j,6]==which_versicolor){
    df4[j,7]='true'
  }else if(df4[j,5]=='virginica'&&df4[j,6]==which_virginica){
    df4[j,7]='true'
  }else{df4[j,7]='false'}
}

df4[df4$V7=='false',]

##### 오분류 데이터를 넣은 그래프 그리기 
df_check <- df4[df4$V7=='false',]

plot2 + geom_point(data=df4[df4$check=='false',],
                   aes(x=df_check[,3], y=df_check[,4], color=df_check$Species),
                   pch=18, size=8, alpha=0.5)
