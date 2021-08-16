FROM python

WORKDIR /api

ADD . .

RUN pip install -r requirements.txt

CMD streamlit run dashboard.py --server.port $PORT