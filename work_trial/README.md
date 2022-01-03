# Improving Performance on 


## Credit Scoring Algorithm

* Model types
* * Logistic regression
* * Decision tree
* * XGBoost
* * Other GBM / decision tree methods?
* * SVM
* * MLP

* Build models that can be easily generalized from binary to multiple classification (not LR)
* Train the model on pre-screened segments of the population. Baseline credit: No prior charge-offs. See if the model can be more accurate. 



## Credit Underwriting Policy Proposal

* Build a Zest Score using credit info from the loan application. Classification models predict the probability that the borrower will fall into default. Provide this number to the pricing model in the form of a default rate, multiplier, or credit score between 350 and 850. 
* Devise a number of individual credit underwriting rules. Pick those which seem valuable, test several hyperparameters, and write a new policy. Use the Zest Score as one of, but not the only, input. 

Tradeoff between credit scoring and credit underwriting:
* Reliability of data
* Effects of missing data
* Out-of-sample performance
* Overfitting

Build a credit score first. But separately build an evaluation of credit underwriting rules. Banks have business needs, they don't always want to overhaul their policies in exchange for our credit score. Stride's investors love to hear that we don't use traditional credit scores. Instead of credit scores, try segmenting the market according to individual underlying characteristics. 


## Dynamic Pricing Proposal
Each student is given a default rate within the pricing model. We should use the credit underwriting dataset to provide default risk assessments for each candidate. 

Zest Score


## Fair Lending Tests

* Extract race and ZIP code from 





## Technical Environment
* Using environments (or requirements.txt) in Jupyter notebooks














