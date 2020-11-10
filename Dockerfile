FROM continuumio/miniconda3

# Add our code
ADD . /opt/smilestoimg/
WORKDIR /opt/smilestoimg

# Install the dependencies.
RUN conda install --yes -c conda-forge rdkit fastapi pydantic gunicorn uvicorn

# Launch the server.
CMD gunicorn --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT smilestoimg.app:app
