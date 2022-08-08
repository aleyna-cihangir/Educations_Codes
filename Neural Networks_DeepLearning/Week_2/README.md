**Binary Classification :**

Logistic regression is an algorithm for binary classification. 
LR is a learning algorithm that you use when the output labels Y in a supervised learning problem are all either zero or one, so for binary classification problems.


**Logistic Regression :**

![image](https://user-images.githubusercontent.com/62557225/177818120-5220aab7-05ba-40bd-8989-63797a38e0de.png)
This is not a very good algorithm for binary classification because Y^ we want the probability that Y is equal to 1. So Y^ really has to be between zero and one, and that's hard to implement, because WX + B could be larger or lower. 

**Sigmoid Function :** Sigmoid is a mathematical function that takes any number and maps it to a probability between 1 and 0. It is very useful for the activation (firing, fire) of nerve cells in an artificial neural network.  
![image](https://user-images.githubusercontent.com/62557225/177819442-b3f5e555-1992-4a34-8f0a-034f83f2b7a0.png)
*z is sigmoid* 


**Loss Function Formula :** 
![image](https://user-images.githubusercontent.com/62557225/179397942-7c982383-c5e3-4c10-8fe5-9623ff4ad8d4.png)


![image](https://user-images.githubusercontent.com/62557225/179398070-6a8c4ed8-46f6-48fa-848a-9b81a25d05ee.png)


If y = 1  ;  L(y^, y) = - logy^  = large logy^ and large y^
 
If y = 0  ;  L(y^, y) = - log(1-y^)  = large log(1-y^) and small y^


**Cost Fonction :** is that, J(w,b) = 1/m[(start m)sum(L(y^i, yi))] = means average of L function 


**GRADIENT DESCENT**

w: = w - alpha[dJ(w)/dw](derivative)             *alpha is learning rate* 

Derivative is positive :
![image](https://user-images.githubusercontent.com/62557225/179398795-f0b10db7-6414-4fe4-a354-eb79203f1a77.png)


Derivative is negative :
![image](https://user-images.githubusercontent.com/62557225/179398825-d2a8d8e9-6dbf-4830-a95b-90f7a9a3fd2f.png)
