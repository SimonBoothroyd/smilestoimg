FROM heroku/miniconda:3

# Add our code
ADD . /opt/smilestoimg/
WORKDIR /opt/smilestoimg

# Install the dependencies. The pins are added in attempt to fix permission errors raised on Heroku.
RUN conda install --yes -c conda-forge "conda ==4.3.11" "pyyaml ==3.12" rdkit fastapi pydantic gunicorn uvicorn

# Launch the server.
CMD gunicorn --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT smilestoimg.app:app