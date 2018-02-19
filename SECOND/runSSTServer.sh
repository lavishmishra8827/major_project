#/usr/bin/env bash

java -Xmx500m -cp lib/supersense-tagger.jar edu.cmu.ark.SuperSenseTaggerServer  --port 8080 --model config/superSenseModelAllSemcor.ser.gz --properties config/QuestionTransducer.properties
