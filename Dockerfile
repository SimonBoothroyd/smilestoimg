FROM heroku/miniconda:3

# Add our code
ADD ./smilestoimg /opt/smilestoimg/
WORKDIR /opt/smilestoimg

# Install the dependencies and fix permissions.
RUN conda install --yes -c conda-forge rdkit fastapi pydantic gunicorn uvicorn && chmod +rwx /usr/lib/python3*/*-packages/.wh*

# Launch the server.
CMD gunicorn --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT app:app