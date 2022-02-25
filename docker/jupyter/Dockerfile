# Inspect the Dockerfile at:
# https://github.com/SCiO-systems/cgspatial-notebook/blob/master/Dockerfile

FROM scioquiver/notebooks:cgspatial-notebook

# install additional package...
RUN pip install --no-cache-dir OWSLib lxml pandas paho-mqtt
RUN conda update --all --yes
RUN conda install --quiet --yes 'r-data.table'
RUN conda install --quiet --yes 'r-mapview'
