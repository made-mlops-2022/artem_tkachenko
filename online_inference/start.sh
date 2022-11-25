if [ -z $MODEL ]
then
    export MODEL="model_knn.pkl"
fi

if [ -z $TRANSFORMER ]
then
    export TRANSFORMER="transformer_knn.pkl"
fi

if [[ ! -f $MODEL ]]
then
    wget -q -N http://185.87.50.149:8082/model_knn.pkl
fi

if [[ ! -f $TRANSFORMER ]]
then
    wget -q -N http://185.87.50.149:8082/transformer_knn.pkl
fi


uvicorn server:app --reload --host 0.0.0.0 --port 18000
