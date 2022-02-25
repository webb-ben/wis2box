FROM scioquiver/notebooks:cgspatial-notebook

# Inspect the Dockerfile at:
# https://github.com/jupyter/docker-stacks/tree/HEAD/datascience-notebook/Dockerfile

# install additional package...
RUN pip install --no-cache-dir OWSLib lxml pandas paho-mqtt
RUN conda install --quiet --yes 'r-data.table'
RUN conda install --quiet --yes 'r-mapview'
