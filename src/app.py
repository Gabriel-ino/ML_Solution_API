from flask import Flask, request
import joblib
from datetime import datetime
import time

from api_database import create_table, consulting_db, insert_db

app = Flask(__name__)

# Load model
model = joblib.load("../models/forest_model_v1_0_0.pkl")


@app.route(
    "/Prediction_API/<area>;<rooms>;<bathroom>;<parking_spaces>;<floor>;<animal>;<furniture>;<hoa>;<property_tax>",
    methods=["GET"],
)
def home(
    area,
    rooms,
    bathroom,
    parking_spaces,
    floor,
    animal,
    furniture,
    hoa,
    property_tax,
):

    starttime = time.time()
    begin = datetime.now()
    create_table()

    user_inputs = [
        float(area),
        float(rooms),
        float(bathroom),
        float(parking_spaces),
        float(floor),
        float(animal),
        float(furniture),
        float(hoa),
        float(property_tax),
    ]

    try:
        predict = model.predict([user_inputs])
        end = datetime.now()
        processing_time = time.time() - starttime

        user_inputs.append(str(predict))

        inputs = ""
        for val in user_inputs:
            inputs += str(val)

        insert_db(inputs, begin, end, processing_time)

        return {"Value: ": str(predict)}
    except Exception as err:
        return {"Warning": f"{err}"}


if __name__ == "__main__":
    app.run(debug=True)
