# Inspect the Dockerfile at:
# https://github.com/SCiO-systems/cgspatial-notebook/blob/master/Dockerfile

# FROM scioquiver/notebooks:cgspatial-notebook
FROM jupyter/datascience-notebook:latest
# FROM webbben/jupyter-datascience:latest
# FROM scioquiver/notebooks:cgspatial-notebook

# install additional package...
RUN pip install --no-cache-dir OWSLib lxml pandas paho-mqtt ipywidgets

RUN mamba update --all --yes
RUN mamba install --quiet --yes \
    'r-mapview' \
    'r-data.table' \
    'r-rlang' \
    'r-systemfonts' \
    'r-rmarkdown' \
    'r-tidymodels' \
    'r-tidyverse' \
    && mamba clean --all -f -y \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"
RUN mamba update --all --yes
