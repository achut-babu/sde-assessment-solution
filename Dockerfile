FROM python:3.8-alpine
ADD requirements.txt /submission/
WORKDIR /submission
ENV INPUT_FILE_PATH ""
ENV OUTPUT_FILE_PATH ""
RUN pip install -r requirements.txt
ENTRYPOINT python sde_solution.py $INPUT_FILE_PATH $OUTPUT_FILE_PATH
