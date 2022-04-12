# News recommender system

The purpose of this project is to create a content-based recommendation algorithm for BBC News, finding similar articles to custom input text.

## Create a virtual environment

Should you want to run the Jupyter notebook or the `app.py` script  locally on your machine, you need to create a virtual environment. Please install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) on your system and use the provided [requirements.txt](https://github.com/pxydi/News_recommender_API/blob/main/requirements.txt) file to install the required Python dependencies with `pip`.

To install the Python dependencies, please run the following commands in the terminal:
```
conda create --name news_recommender python==3.9
conda activate news_recommender
pip install -r requirements.txt
```
## Run the News recommender app locally on your machine

To run the `app.py` script:
* open the terminal and go to the project folder
* activate the virtual environment using: `conda activate news_recommender`
* run this command: `python app.py`

Then, you should be able to type: http://127.0.0.1:5000/similar or http://127.0.0.1:5000/document in the browser.
