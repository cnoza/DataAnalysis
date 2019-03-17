###########################################################################################################################################################################  
############################################################### Louv14x : Introduction à l'économétrie ####################################################################
###########################################################################################################################################################################  
# A travail égal, salaire...inégal!
# code_wages.R
# S. Béreau
###########################################################################################################################################################################  
## Commande de "nettoyage" de l'environnement de travail sous R (permet de s'assurer de travailler dans un 
## environnement neutre)
rm(list=ls(all=TRUE)) 
#####################################################################################################################
setwd("[mentionner ici le lien vers votre répertoire R]")
data<-read.table("wages.csv",sep=",",header=TRUE)
# Légende
#sect     : secteur simplifié 
# (P : primaire, M : industrie, C : construction, S : services, F : finance, R : immobilier)  
#year     : année d'observation
#gender   : genre (M : homme, F : femme)  
#wkt      : temps de travail (trimestriel)            
#gwage_q  : salaire brut trimestriel             
#wgwage_q : salaire brut trimestriel (pondéré à partir de wkt)                          
#bcol     : status de "col bleu"           
#agex     : âge en années
#####################################################################################################################
# Description de la base de données 
summary(data)
# Il est possible de se concentrer sur une année particulière...
data.2006<-subset(data,year==2006)
summary(data.2006)
# On vérifie que la variable "year" ne prend qu'une année possible, l'année 2006
# ...voire une industrie particulière à une date particulière
data.prim2006<-subset(data,year==2006&sect=='P')
summary(data.prim2006)
# On vérifie que la variable "sect" ne prend qu'un secteur possible, 'P' pour primaire sur la seule année 2006
#####################################################################################################################
# Création des variables du modèle
lwage<-log(data[,"wgwage_q"]) # variable endogène, log du salaire 
age<-data[,"agex"] # âge
educ<-data[,"bcol"] # proxy pour le niveau d'éducation
sect<-data[,"sect"] # secteur (simplifié)
year<-data[,"year"] # année
gender<-data[,"gender"] # genre (F:femmes, M: hommes)
#####################################################################################################################
# s0:= lwage=f(age,educ,gender)
# On fait l'hypothèse que l'âge est un proxy de l'expérience et que "bcol" capture, bien qu'imparfaitement, le 
# niveau d'éducation 

reg.fit.s0<-lm(lwage~age+educ+gender)
summary(reg.fit.s0)

# Nous voyons qu'en introduisant la var. "gender", nous pouvons rendre compte d'une différence salariale 
# significative entre les hommes et les femmes qui n'est pas expliquée par l'expérience ou le niveau d'éducation.

# Nous aurions tout aussi bien pu construire une variable muette "female" prenant la valeur 1 si l'individu est une 
# femme. Nous aurions obtenu le même type de résultat (reg.fit.s1).

# s1:= lwage:= f(age,educ,female)

female<-factor(as.numeric(data[,"gender"]=="F",1,0))
reg.fit.s1<-lm(lwage~age+educ+female)
summary(reg.fit.s1)

# Comment réconcilier ces deux estimations? 
# On voit que les coefficients estimés affectant les autres variables explicatives à l'exception de la constante sont 
# identiques, de même que leurs écart-type estimés.
# Le coefficient estimé pour "female" correspond à la différence entre le coefficient estimé de "gender" pour les 
# femmes et celui de "gender" pour les hommes, soit : 
# reg.fit.s0$coefficients["genderF"] (-1.77) -reg.fit.s0$coefficients["genderM"] (-1.19) = -0.2960191
# En revanche le coefficient de la constante, ainsi que les écart-types associés diffèrent - de même que l'écart-type 
# de female qui ne correspond pas à la différence des écart-types de genderF et genderM. 
#####################################################################################################################
# Reprenons cette estimation sur les données relatives à l'année 2006 exclusivement
reg.fit2006.s0<-lm(log(data.2006[,"wgwage_q"])~ data.2006[,"agex"]+data.2006[,"bcol"]+data.2006[,"gender"])
summary(reg.fit2006.s0)

# On peut calculer la valeur de la P-value du coefficient estimé de "gender"*F "à la main"
# On doit calculer 2*(1-fonction de répartition d'un Normale N(0,1) au point |-2.216|)

pv.gender.F<-2*(1-pnorm(2.216))
pv.gender.F

pv.gender.M<-2*(1-pnorm(0.002))
pv.gender.M
# Nous retrouvons bien ici les valeurs calculées par R sous la colonne Pr(>|t|)  associées aux coefficients estimés
#####################################################################################################################
# Comment allez plus loin?
# La littérature sur le sujet a documenté l'existence d'un écart salarial entre industries.
# Nous pouvons tenir compte de ces différences en introduisant la variable codant pour le type d'industrie ("sect"). 
# s2:= lwage:= f(age,educ,sect,female)
reg.fit.s2<-lm(lwage~age+educ+sect+female)
summary(reg.fit.s2)
#####################################################################################################################
# Ccl: L'effet du genre ("gender") sur le log des salaires ("lwages") demeure même lorsque l'on prend 
# en compte l'effet de l'industrie. 
# Ce résultat est en cohérence avec l'existence de discriminations salariales à l'égard des femmes en Belgique.
#####################################################################################################################
# Tester la stabilité des coefficients [Test de Chow]

# Les éléments précédents ont mis en lumière l'impact de la variable "bcol" sur le niveau de salaire moyen. 
# On pourrait aller plus loin et se demander si le lien entre le salaire et ses autres déterminants (et notamment le genre) 
# n'est pas déterminé par le type d'emploi occupé.
# Il est possible par ex. que l'impact du genre sur le salaire soit encore plus défavorable pour les cols blancs 
# que pour les cols bleus, selon l'argument du plafonds de verre qui veut que les femmes aient des difficultés à atteindre 
# les niveaux de responsabilité les plus élevées, allant de paire avec les rémunérations les plus fortes. 

# Si l'on pense que le fait d'être cadre ou non influence la nature du lien entre le salaire et ses déterminants (autres que 
# l'éducation capturée ici par cette proxy, bien que de manière imparfaite), alors on devrait obtenir des coefficients 
# différents en régressant le même modèle sur différents sous-groupes d'individus travaillant dans différentes industries. 

# C'est ce que l'on se propose d'étudier ici. 

# On considère le modèle lwage_i = beta_1+ beta_2*age_i + beta_3*gender_i + epsilon_i

# On note alors : 

# lwage_i = beta_1^0+ beta_2^0*age_i + beta_3^0*gender_i + epsilon^0_i, le modèle valant pour le groupe 0 (cols blancs)
# lwage_i = beta_1^1+ beta_2^1*age_i + beta_3^1*gender_i + epsilon^1_i, le modèle valant pour le groupe 1 (cols bleus)

# S'il n'y a pas de différence entre les paramètres de ces deux modèles, cela veur dire que travailler comme cadre ou 
# comme ouvrier ne change rien à la nature de la relation entre le salaire et ses autres déterminants. 
# En revanche, si des différences existent, cela veut que l'appartenance à telle ou telle catégorie de travailleurs, 
# influence la nature de la relation entre le salaire et ses autres déterminants. 

# Pour tester cela nous devons poser : 

# H_0 : Les paramètres de l'équation de salaire sont identiques quelqe soit le type d'emploi occupé ("col bleu" vs. "col blanc")
# H_1 : Les paramètres de l'équation de salaire varient en fonction du type d'emploi occupé

# ce qui se traduit par :

# H_0 : beta_1^0=beta_1^1 ; beta_2^0=beta_2^1 ; beta_3^0=beta_3^1 (soient J=3 contraintes)
# H_1 : Il existe au moins une relation parmi ces quatre qui n'est pas une égalité

# Il s'agit donc d'un cas particulier de test de contraintes linéaires multiples, appelé test de Chow. 
# Chow, G.C. (1960), Test of equality between sets of coefficients in two linear regressions, Econometrica, 28(3), 591-605

# On peut montrer qu'en notant SCR la somme des carrés des résidus du modèle estimé pour l'ensemble des individus 
# cols blancs et cols bleus confondus d'une part (modèle contraint sous H_0), et, SCR_0 et SCR_1 celles calculées à 
# l'issue de l'estimation par les MCO du modèle de régression sur les sous-groupes 0 et 1 resp. d'autre part (modèle 
# non contraint sous H_1), la statistique de Fisher s'écrit comme suit : 
# F = ((SCR-(SCR_0+SCR_1))/K)/((SCR_0+SCR_1)/(n-2K)) 
# où K est le nombre de variables explicatives du modèle, ici 3

# Comme dans le cas général, quand n est grand, K.F converge sous H_0 vers une distribution du Chi-deux à K 
# degrés de liberté.

#####################################################################################################################
# Estimation du modèle de référence sur l'ensemble de l'échantillon
n<-length(data[,1])
K<-3
reg.fit.bench<-lm(lwage~age+female)
s.bench<-summary(reg.fit.bench)
SCR<-(s.bench$sigma)^2*(n-K)
SCR
# Un autre façon de récupérer la SCR consiste à utiliser la commande : 
deviance(reg.fit.bench)

# Estimation sur les deux sous-échantillons bcol==0 (cols blancs) vs. bcol==1 (cols bleus)
data.0<-subset(data,bcol==0)
data.1<-subset(data,bcol==1)
female.0<-factor(as.numeric(data.0[,"gender"]=="F",1,0))
female.1<-factor(as.numeric(data.1[,"gender"]=="F",1,0))

n_0=length(data.0[,1])
n_1=length(data.1[,1])
# Vérifions que n = n_0+n_1 
n_0+n_1-n

reg.fit.0<-lm(log(data.0[,"wgwage_q"])~data.0[,"agex"]+female.0)
s.0<-summary(reg.fit.0)
SCR_0<-(s.0$sigma)^2*(n_0-K)

reg.fit.1<-lm(log(data.1[,"wgwage_q"])~data.1[,"agex"]+female.1)
s.1<-summary(reg.fit.1)
SCR_1<-(s.1$sigma)^2*(n_1-K)

# Calcul de la statistique sous H_0
K=3
W_obs=K*((SCR-(SCR_0+SCR_1))/K)/((SCR_0+SCR_1)/(n-2*K)) 

# Calcul de la P-value associée au test
PV<-1-pchisq(W_obs,K)
PV

# La PV du test est égale à 0, on rejette donc très fortement l'hypothèse nulle 
# de stabilité des coefficients dans les deux modèles. 
# Les paramètres sont donc globalement instables selon l'appartenance à tel ou tel 
# groupe de travailleurs.
# L'impact négatif de "female" dans le groupe "0" des cols blancs ne semble en revanche
# pas plus faible que celui du groupe "1" des cols bleus - si une différence significative
# existe, elle va plutôt dans le sens opposé d'un impact plus négatif pour les 
# catégories sociales les plus faibles. 

# Ce résultat mériterait sans doute d'être ré-exploré plus en profondeur en incluant 
# d'autres variables de contrôle. 