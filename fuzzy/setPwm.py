import os
from database import models
from fuzzy.externalFuzzy import calculateExternalMandami
from fuzzy.iternalFuzzy import calculateIternalMandami


def setPwm():
    espLastMeasurement=(models.Esp().espGetLastView())[0][0]
    frame = []
    for row in espLastMeasurement["sensorValue"]:
        if row['name'] == 'PM2.5':
            if float(row["value"]) < 25:
                frame.append(float(row["value"]))
            else:
                frame.append(25)
        elif row['name'] =='PM10':
            if float(row["value"]) < 50:
                frame.append(float(row["value"]))
            else:
                frame.append(50)
    airlyLastMeasurement = (models.Airly().airlyGetLastJsonView())[0][0]
    for row in airlyLastMeasurement["current"]["sensorValue"]:
        if row['name'] == 'PM25':
            if float(row["value"]) < 25:
                frame.append(float(row["value"]))
            else:
                frame.append(25)
        elif row['name'] =='PM10':
            if float(row["value"]) < 50:
                frame.append(float(row["value"]))
            else:
                frame.append(50)
    airlyForecastMeasurement = (models.Airly().airlyGetForecastLastJsonView())[0][0]
    for row in airlyForecastMeasurement["forecast"][0]["sensorValue"]:
        if row['name'] == 'PM25':
            if float(row["value"]) < 25:
                frame.append(float(row["value"]))
            else:
                frame.append(25)
        elif row['name'] == 'PM10':
            if float(row["value"]) < 50:
                frame.append(float(row["value"]))
            else:
                frame.append(50)
    print(frame)
    espCurrentMandami = calculateExternalMandami(frame [0],frame[1], 25, 50)
    airlyCurrentMandami = calculateExternalMandami(frame[2], frame[3], 25, 50)
    airlyForecastMandami = calculateExternalMandami(frame[4], frame[5], 25, 50)
    print(airlyCurrentMandami, espCurrentMandami, airlyForecastMandami)

    funMandami = calculateIternalMandami(airlyCurrentMandami, espCurrentMandami, airlyForecastMandami)
    print(funMandami)
    os.system("gpio mode 23 pwm ")
    set_pwm = "gpio pwm 23 " + str(funMandami)
    os.system(set_pwm)