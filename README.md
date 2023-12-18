# Face-Detector 🔍

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
![License](https://badgen.net/github/license/micromatch/micromatch)


Face Detector basically detects the number of persons present in an image and also try to figure them out. As its an AI Model it sometime fails to detect the famous personalities so please consider.
Click [here](https://face-identifier-f6yfaqdqiygobhgs9qzeky.streamlit.app/) to try out

## How to use:
1. Go through the disclaimer ⚠️ to understand more regarding what type of images will give best results.
2. Upload any image of your choice (upto 200MB)
3. Wait for the image to be uploaded, the dimesions of the image will be updated
4. Click on the button to identify the person and view results.
5. Wait for few mins and See the ✨Magic ✨ Happen.

## Installation:

- clone this repository

- Face Detector requires [Python](https://www.python.org/) v3.9+ to run.

- Install the dependencies.

```python
pip install streamlit
pip install google-generativeai
pip install Pillow
pip install python-dotenv # for environment variable
```
- Make sure to create your own generative-ai api-key using Google Cloud Console or Google Makersuite and replace it.

```python
genai.configure(api_key=os.getenv("MY_SECRET_KEY")) # Replace with your own api-key by creating .env file
```
or 
```python
genai.configure(api_key="YOUR APIKEY")  # Replace YOUR APIKEY with the actual value of your apikey 
```

- To run the server
```python
streamlit run "your_file_name"
```

- For Deploying your application refer [Streamlit Community Cloud](https://docs.streamlit.io/streamlit-community-cloud/get-started)

## Development:

Want to contribute? Great!

Face Detector uses streamlit.

checkout *Installation* above to set it up locally.

make sure all changes you make are in the testing branch. 

## Deployment:

The website is deployed using streamlit community cloud ⬇️

[Link](https://face-identifier-f6yfaqdqiygobhgs9qzeky.streamlit.app/) 
