

machine learning = looking for function: 
- 
* speech recognition ="how are you"
* image recognition = "cat"
* playing chess= "5-5" (next move)

Different types of function:
  1. regression: the function outputs a scalar ( predicting pm2.5 , inputing pm2.5 today , temperature... into a function to predict it for tomorrow)
  2. classification: given options (classes), the function outputs the correct one (multiple choice) like spam filtering -> function -> yes/no

  -------------------------------------

structured learning: create something with structure (image,document)

1. function with unknown parameters 
- y= f (youtube background views) <- using the views from before to predict the view for the future
- y = b + w* x1 based on domain knowledge
- y = model , x1 = feature , w = weight , b= bias
- y = no. of views on 2/26, x1 = no. of views on 2/25
- w and b are unknown parameters (learned from data)

2. define loss from training data
-  Loss is a function of parameters L(b,w)
-  Loss : how good a set of value is
- ex: L(0.5k , 1) y=b+w*x1 -> y=0.5k +1(x1) how good it is?
-  training data : data from 2017/01/01 -> 2020/12/31
- 0.5k +1(x1)=y
