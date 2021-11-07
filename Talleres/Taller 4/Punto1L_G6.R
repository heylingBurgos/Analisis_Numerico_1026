"
  Integrantes:
  
  - Andrés Felipe Vasquez
  - Johan Mateo Rosero
  - Fabián Andrés Olarte
  - David Suarez
  - Heyling Burgos 
  
  Referencias:
  - https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/seq
  - https://r-coder.com/distribucion-binomial-r/
  - https://rpubs.com/hllinas/R_Normal_Aprox_Discreta
  - Mariana Silvia Santamaría y Marta Susana Malla. (2010). Revista investigación operacional. Educational issues/ Aspectos Educacionales, 13.
  
"


n<- 1000
p<- 0.5
BinomialAproxNormal(n,p)
TablaProbabilidades(n,p)
options(max.print=9999)

BinomialAproxNormal<-function(n,p){
  #Función de masa de probabilidad Binomial
  binom1=dbinom(0:n,n,p)
  binom1Redondear=round(binom1,3)
  matrizBinom <- matrix(0:n,ncol= (n+1))
  matrizFrecuencia = matrix(binom1Redondear,ncol= (n+1))
  matrizTabla = rbind(matrizBinom, matrizFrecuencia)
  TablaContuinidad = matrizTabla[,matrizTabla[2,]>=0.001]
  fila1 = TablaContuinidad[1,]
  fila2 = TablaContuinidad[2,]*1000
  Xn = rep(fila1,fila2)
  #histograma variable X
  hist(Xn,breaks=seq(min(fila1)-0.5, max(fila1)+0.5,by=1),freq=F, xlab= c("Variables binomiales en Xn"), ylab=c("Aproximación"),main=paste(" "))
  Yn=Xn-n*p
  windows()
  
  #histograma variable Y=X-n*p
  hist(Yn,breaks=seq(min(fila1-n*p)-0.5,max(fila1-n*p)+0.5,by=1),freq=F,xlab= c("Variables binomiales en Yn"), ylab=c("Aproximación"), main=paste(" "))
  Zn=Yn/sqrt(n*p*(1-p))
  windows()
  
  #histograma variable Z=X-n*p/qrt(n*p*(1-p))
  inversadesvio=1/(sqrt(n*p*(1-p)))
  hist(Zn,freq=F,breaks=seq(min(Zn)-0.5* inversadesvio, max(Zn)+ 0.5* inversadesvio, by=1/(sqrt(n*p*(1- p)))),xlim=c(-4,4), ylim=c(0,0.5),xlab= c("Variables binomiales en Zn"), ylab=c("Aproximación"), main=paste(" ")) 
  xaleatorios = seq(-3.5,3.5,length=100000)
  
  ynormales=dnorm(xaleatorios, 0,1)
  lines(xaleatorios, ynormales,col='blue',lwd=3)
}

TablaProbabilidades<- function(n,p){
  # corrección por continuidad 0.05
  datosx=0:n
  #Función de masa de probabilidad Binomial
  binomial<-dbinom(0,n,p)
  normal<- pnorm((0+0.05 - n*p)/sqrt(n*p*(1-p)),0,1)
  
  #Construir tabla comparación binomial por normal
  for (i in 1:(n-1)){ 
    binomial<-cbind(binomial,dbinom(i,n,p))
    normal<-cbind(normal,pnorm((i+0.05 - n*p)/sqrt(n*p*(1-p)),0,1)- pnorm((i-0.05 - n*p)/sqrt(n*p*(1-p)),0,1))
  }
  
  binomial<-cbind(binomial,dbinom(n,n,p))
  normal<-cbind(normal,1-pnorm((n-0.05 - n*p)/sqrt(n*p*(1-p)),0,1))
  matrizaprox<-matrix(c(datosx, round(binomial,digits=20),round(normal,digits=20)), ncol=3, dimnames=list(rep(' ',(n+1)), rep(' ',3)))
  
  tablaTotal<-cbind(matrizaprox)
  cat(rep("",4),"x",rep("",1),"Valor B", rep(" ",2),"Aprox. N", "\n")
  print(tablaTotal)
} 