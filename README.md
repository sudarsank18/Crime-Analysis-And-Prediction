## Crime-analysis-and-Prediction
An analysis of crimes against women in India from 2001 to 2012 is taken and visualized. Then the crime rate is predicted until 2022 by using ARIMA and SARIMA models.Then the result of these two models are compared and the model that gives better prediction is considered the best.

## Functional Requirements
- Data collection
- Data processing
- Training and Testing
- Modeling
- Predicting

## SYSTEM COMPONENTS(MODULES)
### Import Libraries 
In this module, different libraries like pandas, NumPy, matplotlib, and statsmodels are imported, which are useful for data processing,visualization, accuracy, and prediction.

### Data Processing
In this module, the data undergoes pre-processing like cleaning the dataset and removing null and unwanted values.

### Visualization
- Initially, the data undergoes visualization for the crime given by the user.
- Next for the entered year, visualization is done for all the crime counts for all the states in India.
- Next the crime rate is compared for the years 2001 and 2012 (i.e for the initial and final data in the data set).
- Then the graph is plotted against the crime count district-wise for the entered state.

### Built ARIMA model
- An autoregressive integrated moving average model, a statistical 
  analysis model that uses time series data to better understand the 
  data set or predict future trends.
- Here the values in the data set range from 2001 to 2012.
- Here the data is fed from 2013 to 2022 manually.
- Then the model is built and the graph is displayed.

### Built SARIMA model
- A seasonal autoregressive integrated moving average model which is like ARIMA but more powerful.
- We can use statsmodels implementation of SARIMA.
- Then the model is built and the graph is displayed using a seasonal pattern.

### Streamlit
- Here Streamlit is used as GUI.
- The user can select a particular state and crime and the graphs of  ARIMA and SARIMA models are displayed with their predicted values


## Screenshots

![Screenshot (184)](https://user-images.githubusercontent.com/86424600/208287595-79fc0d4e-62df-42c0-97ea-ff87abc57680.png)

![Screenshot (185)](https://user-images.githubusercontent.com/86424600/208287596-16177fea-21d9-4b76-9fbd-8e70cfd7b593.png)

![Screenshot (186)](https://user-images.githubusercontent.com/86424600/208287599-a4bd6cb5-7b1d-4e19-adb1-30b2376198be.png)

![Screenshot (187)](https://user-images.githubusercontent.com/86424600/208287602-9c3ccdeb-5fc0-4bc4-a1dd-dc16f27dfdb0.png)

![Screenshot (188)](https://user-images.githubusercontent.com/86424600/208287609-49453e63-2ce7-4b4b-80c7-5a064f1481d3.png)

![Screenshot (189)](https://user-images.githubusercontent.com/86424600/208287612-9e727b99-4c66-4b24-8e64-e0661bfaacae.png)

![Screenshot (190)](https://user-images.githubusercontent.com/86424600/208287615-5ac45e58-2ccf-426b-ac89-f6d1e206808c.png)

![Screenshot (191)](https://user-images.githubusercontent.com/86424600/208287619-c76d4651-909e-4559-a415-a6066966a873.png)

![Screenshot (192)](https://user-images.githubusercontent.com/86424600/208287626-d7558cba-472e-4492-b5a6-59523ac88114.png)

