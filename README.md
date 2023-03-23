# SOI_SIEMEN

## MODEL
 
  #### Download the files:
   - Model= [SOI_Siemen_model.py](https://github.com/AdumaRishithReddy/SOI_SIEMEN/blob/1d07ff62cfc92c964513831fc840721ce30524bb/SOI_Siemen_model.py)
   
   - Training dataframe = [problem_dataaset.csv](https://github.com/AdumaRishithReddy/SOI_SIEMEN/blob/1d07ff62cfc92c964513831fc840721ce30524bb/problem_dataset.csv)
  
  (NOTE: Download the files into same folder)
  
  -Run SOI_Siemen_model.py
   - You will recieve accuracy and confusion matrix of out model
   - More information regarding model and our thought process is given in our [documentation](https://github.com/AdumaRishithReddy/SOI_SIEMEN/blob/1254e8a0837894448f5f3dfe37dfe7c86ae5497c/documentation.pdf)
 
## WEB APP
 
  - We have used [streamlit](streamlit.io) to create a python web app to display results of our model
   
 ## Deployment

   - We have used streamlit to deploy our web app.
  
   - Anyone can access this web app using this [link](https://share.streamlit.io/adumarishithreddy/soi_siemen/main/siemen_upload.py)
  
   - You can upload a csv file and get the results in the form of a table on the website, and you can also download the csv file using the download button.
  
   - The result contains of index,kepler ID and av_result(prediction from our model)

  ## Local Hosting 

   - Although our website is deployed on the web one can host it locally using streamlit.
   -  For this one has to download our entire repository
   -  Using [Anaconda Navigator](https://www.anaconda.com/products/distribution#windows) create a new environment streamlit
    ![EiiFc](https://user-images.githubusercontent.com/96329626/173228228-832d3f42-985c-4786-b730-094bcf462588.png)
   -  Using the terminal install streamlit
   ```
   pip install streamlit
   ```
   - The main webapp file is [siemen_upload.py](https://github.com/AdumaRishithReddy/SOI_SIEMEN/blob/73b78a6e2c27142bfc0c6797b52b28f1183a17a6/siemen_upload.py)
   - To start local host
   ```
   streamlit run siemen_upload.py
   ```


