"""In this module we define the list of apps contributed to the Gallery

Please note that all contribute apps should

- be located in https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/master/
gallery/<app_name_folder>
- include that tags tags.CODE, tags.APP_IN_GALLERY as a minimum
"""
from awesome_streamlit.database import authors, tags
from awesome_streamlit.database.settings import GITHUB_RAW_URL
from awesome_streamlit.shared.models import Resource

GITHUB_RAW_GALLERY_URL = GITHUB_RAW_URL + "gallery/"

DEFAULT_APP_IN_GALLERY = Resource(
    name="Spreadsheet",
    url=GITHUB_RAW_URL + "gallery/spreadsheet/spreadsheet.py",
    tags=[tags.CODE, tags.APP_IN_GALLERY],
    is_awesome=True,
    author=authors.MARC_SKOV_MADSEN,
)
APPS_IN_GALLERY = [
    Resource(
        name="File Download Workaround",
        url=GITHUB_RAW_GALLERY_URL + "file_download/file_download.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Bokeh Experiments",
        url=GITHUB_RAW_GALLERY_URL + "bokeh_experiments/bokeh_experiments.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Layout Experiments",
        url=GITHUB_RAW_GALLERY_URL + "layout_experiments/app.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Table Experiments",
        url=GITHUB_RAW_GALLERY_URL + "table_experiments/app.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Iris Classifier",
        url=GITHUB_RAW_GALLERY_URL + "iris_classification/iris.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.MACHINE_LEARNING],
        is_awesome=True,
        author=authors.NOAH_SAUNDERS,
    ),
    Resource(
        name="ML App registry",
        url=GITHUB_RAW_GALLERY_URL + "ml_app_registry/app.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.MACHINE_LEARNING],
        is_awesome=True,
        author=authors.BOADZIE_DANIEL,
    ),
    Resource(
        name="Medical Language Learner Model",
        url=GITHUB_RAW_GALLERY_URL
        + "medical_language_learner/medical_language_learner.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.NLP],
        is_awesome=True,
        author=authors.GEORGI_TANCEV,
    ),
    Resource(
        name="Yahoo Finance",
        url=GITHUB_RAW_GALLERY_URL + "yahoo_finance_app/yahoo_finance_app.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.FINANCE],
        is_awesome=True,
        author=authors.PADUEL,
    ),
    Resource(
        name="Country Indicators",
        url=GITHUB_RAW_GALLERY_URL
        + "country_indicators/streamlit_country_indicators.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.VOILA],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    # Resource(
    #     name="Gaussian Plot",
    #     url=GITHUB_RAW_GALLERY_URL
    #     + "interactive_gaussian_plot/interactive_gaussian_plot.py",
    #     tags=[tags.CODE, tags.APP_IN_GALLERY, tags.VOILA],
    #     is_awesome=True,
    #     author=authors.MARC_SKOV_MADSEN,
    # ),
    Resource(
        name="Self Driving Cars",
        url=GITHUB_RAW_GALLERY_URL + "self_driving_cars/self_driving_cars.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY],
        is_awesome=True,
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="Awesome Streamlit Test Runner",
        url=GITHUB_RAW_GALLERY_URL + "test_runner_app/test_runner_app.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Sentiment Algorithm",
        url=GITHUB_RAW_GALLERY_URL + "sentiment_analyzer/sentiment_analyzer.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.MACHINE_LEARNING],
        is_awesome=True,
        author=authors.PARAS_PATIDAR,
    ),
    Resource(
        name="SpacyIO",
        url=(
            "https://gist.githubusercontent.com/ines/b320cb8441b590eedf19137599ce6685/raw/"
            "6e0ead5a442fd9c5e3f621a76fba94241cc847ce/streamlit_spacy.py"
        ),
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.NLP],
        is_awesome=True,
        author=authors.INES,
    ),
    Resource(
        name="Uber NYC Pickups",
        url="https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/app.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY],
        is_awesome=True,
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="NBA Roster Turnover",
        url=GITHUB_RAW_GALLERY_URL + "nba_roster_turnover/roster_turnover.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY],
        is_awesome=True,
        author=authors.KEVIN_ARVAI,
    ),
    Resource(
        name="Iris EDA App",
        url=GITHUB_RAW_GALLERY_URL + "iris_eda_app/iris_eda_app.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY],
        is_awesome=True,
        author=authors.JCHARIS,
    ),
        Resource(
        name="Apache JMeter",
        url=GITHUB_RAW_GALLERY_URL + "streamlit_jmeter/streamlit_jmeter.py",
        tags=[tags.CODE, tags.APP_IN_GALLERY],
        is_awesome=True,
        author=authors.JCHARIS,
    ),
    DEFAULT_APP_IN_GALLERY,
]
