import numpy as np
import skfuzzy as fuzz


def fmaximum(func1,func2):
    return np.fmax(func1,func2)

def getAggregate(counter,action,aggrs):
    if  counter  == 0:
        return fmaximum(action[counter-1],aggrs)
    else:
        if counter == len(action):
            aggr = fmaximum(action[counter-1],action[counter])
            return getAggregate(counter - 1, action, aggr)
        else:
            aggr = fmaximum(action[counter-1],aggrs)
            return getAggregate(counter -1,action,aggr)

def calculateIternalMandami(airlyCurrentMeassurment, espCurrentMeasurment, airlyForecastMeasurment):
    airlyCurrent = np.arange(0, 1024, 1)
    airlyForecast = np.arange(0, 1024, 1)
    espCurrent = np.arange(0, 1024, 1)
    fun = np.arange(0, 1024, 1)

    # Generate fuzzy membership functions
    airlyCurrent_1 = fuzz.trimf(fun, [0, 0, 500])
    airlyCurrent_2 = fuzz.trimf(fun, [200, 500, 700])
    airlyCurrent_3 = fuzz.trimf(fun, [300, 600, 850])
    airlyCurrent_4 = fuzz.trimf(fun, [500, 750 , 900])
    airlyCurrent_5 = fuzz.trimf(fun, [750, 1024, 1024])

    espCurrent_1 = fuzz.trimf(fun, [0, 0, 500])
    espCurrent_2 = fuzz.trimf(fun, [200, 500, 700])
    espCurrent_3 = fuzz.trimf(fun, [300, 600, 850])
    espCurrent_4 = fuzz.trimf(fun, [500, 750 , 900])
    espCurrent_5 = fuzz.trimf(fun, [750, 1024, 1024])

    airlyForecast_1 = fuzz.trimf(fun, [0, 0, 500])
    airlyForecast_2 = fuzz.trimf(fun, [200, 500, 700])
    airlyForecast_3 = fuzz.trimf(fun, [300, 600, 850])
    airlyForecast_4 = fuzz.trimf(fun, [500, 750 , 900])
    airlyForecast_5 = fuzz.trimf(fun, [750, 1024, 1024])

    funLevel_1 = fuzz.trimf(fun, [0, 0, 500])
    funLevel_2 = fuzz.trimf(fun, [200, 500, 700])
    funLevel_3 = fuzz.trimf(fun, [300, 600, 850])
    funLevel_4 = fuzz.trimf(fun, [500, 750 , 900])
    funLevel_5 = fuzz.trimf(fun, [750, 1024, 1024])

    # pobrane wartosci z skryptu connectDataBase
    # aktualne wartosci z ESP

    airlyCurrentVeryLow = fuzz.interp_membership(airlyCurrent, airlyCurrent_1, airlyCurrentMeassurment)
    airlyCurrentLow = fuzz.interp_membership(airlyCurrent, airlyCurrent_2, airlyCurrentMeassurment)
    airlyCurrentMid = fuzz.interp_membership(airlyCurrent, airlyCurrent_3, airlyCurrentMeassurment)
    airlyCurrentHigh = fuzz.interp_membership(airlyCurrent, airlyCurrent_4, airlyCurrentMeassurment)
    airlyCurrentVeryHigh = fuzz.interp_membership(airlyCurrent, airlyCurrent_5, airlyCurrentMeassurment)

    espCurrentVeryLow = fuzz.interp_membership(espCurrent, espCurrent_1, espCurrentMeasurment)
    espCurrentLow = fuzz.interp_membership(espCurrent, espCurrent_2, espCurrentMeasurment)
    espCurrentMid = fuzz.interp_membership(espCurrent, espCurrent_3, espCurrentMeasurment)
    espCurrentHigh = fuzz.interp_membership(espCurrent, espCurrent_4, espCurrentMeasurment)
    espCurrentVeryHigh = fuzz.interp_membership(espCurrent, espCurrent_5, espCurrentMeasurment)

    airlyForecastVeryLow = fuzz.interp_membership(airlyForecast, airlyForecast_1, airlyForecastMeasurment)
    airlyForecastLow = fuzz.interp_membership(airlyForecast, airlyForecast_2, airlyForecastMeasurment)
    airlyForecastMid = fuzz.interp_membership(airlyForecast, airlyForecast_3, airlyForecastMeasurment)
    airlyForecastHigh = fuzz.interp_membership(airlyForecast, airlyForecast_4, airlyForecastMeasurment)
    airlyForecastVeryHigh = fuzz.interp_membership(airlyForecast, airlyForecast_5, airlyForecastMeasurment)


    ###############################################################
    #IF
    activeRule = []
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentVeryLow, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentVeryLow, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentVeryLow, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentVeryLow, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentVeryLow, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentLow, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentLow, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentLow, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentLow, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentLow, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentMid, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentMid, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentMid, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentMid, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentMid, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentHigh, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentHigh, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentHigh, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentHigh, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentHigh, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentVeryHigh, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentVeryHigh, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentVeryHigh, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentVeryHigh, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryLow, np.fmin(espCurrentVeryHigh, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentVeryLow, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentVeryLow, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentVeryLow, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentVeryLow, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentVeryLow, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentLow, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentLow, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentLow, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentLow, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentLow, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentMid, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentMid, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentMid, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentMid, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentMid, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentHigh, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentHigh, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentHigh, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentHigh, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentHigh, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentVeryHigh, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentVeryHigh, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentVeryHigh, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentVeryHigh, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentLow, np.fmin(espCurrentVeryHigh, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentVeryLow, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentVeryLow, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentVeryLow, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentVeryLow, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentVeryLow, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentLow, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentLow, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentLow, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentLow, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentLow, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentMid, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentMid, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentMid, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentMid, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentMid, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentHigh, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentHigh, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentHigh, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentHigh, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentHigh, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentVeryHigh, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentVeryHigh, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentVeryHigh, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentVeryHigh, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentMid, np.fmin(espCurrentVeryHigh, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentVeryLow, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentVeryLow, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentVeryLow, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentVeryLow, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentVeryLow, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentLow, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentLow, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentLow, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentLow, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentLow, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentMid, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentMid, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentMid, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentMid, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentMid, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentHigh, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentHigh, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentHigh, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentHigh, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentHigh, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentVeryHigh, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentVeryHigh, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentVeryHigh, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentVeryHigh, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentHigh, np.fmin(espCurrentVeryHigh, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentVeryLow, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentVeryLow, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentVeryLow, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentVeryLow, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentVeryLow, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentLow, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentLow, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentLow, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentLow, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentLow, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentMid, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentMid, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentMid, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentMid, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentMid, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentHigh, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentHigh, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentHigh, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentHigh, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentHigh, airlyForecastVeryHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentVeryHigh, airlyForecastVeryLow)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentVeryHigh, airlyForecastLow)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentVeryHigh, airlyForecastMid)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentVeryHigh, airlyForecastHigh)))
    activeRule.append(np.fmin(airlyCurrentVeryHigh, np.fmin(espCurrentVeryHigh, airlyForecastVeryHigh)))

    action = []

    action.append(np.fmin(activeRule[0], funLevel_1))
    action.append(np.fmin(activeRule[1], funLevel_1))
    action.append(np.fmin(activeRule[2], funLevel_2))
    action.append(np.fmin(activeRule[3], funLevel_3))
    action.append(np.fmin(activeRule[4], funLevel_4))
    action.append(np.fmin(activeRule[5], funLevel_2))
    action.append(np.fmin(activeRule[6], funLevel_2))
    action.append(np.fmin(activeRule[7], funLevel_2))
    action.append(np.fmin(activeRule[8], funLevel_3))
    action.append(np.fmin(activeRule[9], funLevel_3))
    action.append(np.fmin(activeRule[10], funLevel_3))
    action.append(np.fmin(activeRule[11], funLevel_3))
    action.append(np.fmin(activeRule[12], funLevel_3))
    action.append(np.fmin(activeRule[13], funLevel_3))
    action.append(np.fmin(activeRule[14], funLevel_4))
    action.append(np.fmin(activeRule[15], funLevel_4))
    action.append(np.fmin(activeRule[16], funLevel_4))
    action.append(np.fmin(activeRule[17], funLevel_4))
    action.append(np.fmin(activeRule[18], funLevel_4))
    action.append(np.fmin(activeRule[19], funLevel_5))
    action.append(np.fmin(activeRule[20], funLevel_5))
    action.append(np.fmin(activeRule[21], funLevel_5))
    action.append(np.fmin(activeRule[22], funLevel_5))
    action.append(np.fmin(activeRule[23], funLevel_5))
    action.append(np.fmin(activeRule[24], funLevel_5))
    action.append(np.fmin(activeRule[25], funLevel_1))
    action.append(np.fmin(activeRule[26], funLevel_1))
    action.append(np.fmin(activeRule[27], funLevel_2))
    action.append(np.fmin(activeRule[28], funLevel_3))
    action.append(np.fmin(activeRule[29], funLevel_4))
    action.append(np.fmin(activeRule[30], funLevel_2))
    action.append(np.fmin(activeRule[31], funLevel_2))
    action.append(np.fmin(activeRule[32], funLevel_2))
    action.append(np.fmin(activeRule[33], funLevel_3))
    action.append(np.fmin(activeRule[34], funLevel_4))
    action.append(np.fmin(activeRule[35], funLevel_3))
    action.append(np.fmin(activeRule[36], funLevel_3))
    action.append(np.fmin(activeRule[37], funLevel_3))
    action.append(np.fmin(activeRule[38], funLevel_3))
    action.append(np.fmin(activeRule[39], funLevel_4))
    action.append(np.fmin(activeRule[40], funLevel_4))
    action.append(np.fmin(activeRule[41], funLevel_4))
    action.append(np.fmin(activeRule[42], funLevel_4))
    action.append(np.fmin(activeRule[43], funLevel_4))
    action.append(np.fmin(activeRule[44], funLevel_5))
    action.append(np.fmin(activeRule[45], funLevel_5))
    action.append(np.fmin(activeRule[46], funLevel_5))
    action.append(np.fmin(activeRule[47], funLevel_5))
    action.append(np.fmin(activeRule[48], funLevel_5))
    action.append(np.fmin(activeRule[49], funLevel_5))
    action.append(np.fmin(activeRule[50], funLevel_1))
    action.append(np.fmin(activeRule[51], funLevel_1))
    action.append(np.fmin(activeRule[52], funLevel_2))
    action.append(np.fmin(activeRule[53], funLevel_3))
    action.append(np.fmin(activeRule[54], funLevel_4))
    action.append(np.fmin(activeRule[55], funLevel_2))
    action.append(np.fmin(activeRule[56], funLevel_2))
    action.append(np.fmin(activeRule[57], funLevel_3))
    action.append(np.fmin(activeRule[58], funLevel_3))
    action.append(np.fmin(activeRule[59], funLevel_4))
    action.append(np.fmin(activeRule[60], funLevel_3))
    action.append(np.fmin(activeRule[61], funLevel_3))
    action.append(np.fmin(activeRule[62], funLevel_3))
    action.append(np.fmin(activeRule[63], funLevel_4))
    action.append(np.fmin(activeRule[64], funLevel_4))
    action.append(np.fmin(activeRule[65], funLevel_4))
    action.append(np.fmin(activeRule[66], funLevel_4))
    action.append(np.fmin(activeRule[67], funLevel_4))
    action.append(np.fmin(activeRule[68], funLevel_4))
    action.append(np.fmin(activeRule[69], funLevel_5))
    action.append(np.fmin(activeRule[70], funLevel_5))
    action.append(np.fmin(activeRule[71], funLevel_5))
    action.append(np.fmin(activeRule[72], funLevel_5))
    action.append(np.fmin(activeRule[73], funLevel_5))
    action.append(np.fmin(activeRule[74], funLevel_5))
    action.append(np.fmin(activeRule[75], funLevel_2))
    action.append(np.fmin(activeRule[76], funLevel_2))
    action.append(np.fmin(activeRule[77], funLevel_3))
    action.append(np.fmin(activeRule[78], funLevel_3))
    action.append(np.fmin(activeRule[79], funLevel_4))
    action.append(np.fmin(activeRule[80], funLevel_2))
    action.append(np.fmin(activeRule[81], funLevel_2))
    action.append(np.fmin(activeRule[82], funLevel_3))
    action.append(np.fmin(activeRule[83], funLevel_3))
    action.append(np.fmin(activeRule[84], funLevel_4))
    action.append(np.fmin(activeRule[85], funLevel_2))
    action.append(np.fmin(activeRule[86], funLevel_2))
    action.append(np.fmin(activeRule[87], funLevel_3))
    action.append(np.fmin(activeRule[88], funLevel_4))
    action.append(np.fmin(activeRule[89], funLevel_5))
    action.append(np.fmin(activeRule[90], funLevel_4))
    action.append(np.fmin(activeRule[91], funLevel_4))
    action.append(np.fmin(activeRule[92], funLevel_4))
    action.append(np.fmin(activeRule[93], funLevel_4))
    action.append(np.fmin(activeRule[94], funLevel_5))
    action.append(np.fmin(activeRule[95], funLevel_5))
    action.append(np.fmin(activeRule[96], funLevel_5))
    action.append(np.fmin(activeRule[97], funLevel_5))
    action.append(np.fmin(activeRule[98], funLevel_5))
    action.append(np.fmin(activeRule[99], funLevel_5))
    action.append(np.fmin(activeRule[100], funLevel_3))
    action.append(np.fmin(activeRule[101], funLevel_3))
    action.append(np.fmin(activeRule[102], funLevel_3))
    action.append(np.fmin(activeRule[103], funLevel_3))
    action.append(np.fmin(activeRule[104], funLevel_4))
    action.append(np.fmin(activeRule[105], funLevel_3))
    action.append(np.fmin(activeRule[106], funLevel_3))
    action.append(np.fmin(activeRule[107], funLevel_3))
    action.append(np.fmin(activeRule[108], funLevel_4))
    action.append(np.fmin(activeRule[109], funLevel_5))
    action.append(np.fmin(activeRule[110], funLevel_3))
    action.append(np.fmin(activeRule[111], funLevel_3))
    action.append(np.fmin(activeRule[112], funLevel_3))
    action.append(np.fmin(activeRule[113], funLevel_4))
    action.append(np.fmin(activeRule[114], funLevel_5))
    action.append(np.fmin(activeRule[115], funLevel_4))
    action.append(np.fmin(activeRule[116], funLevel_4))
    action.append(np.fmin(activeRule[117], funLevel_4))
    action.append(np.fmin(activeRule[118], funLevel_4))
    action.append(np.fmin(activeRule[119], funLevel_5))
    action.append(np.fmin(activeRule[120], funLevel_5))
    action.append(np.fmin(activeRule[121], funLevel_5))
    action.append(np.fmin(activeRule[122], funLevel_5))
    action.append(np.fmin(activeRule[123], funLevel_5))
    action.append(np.fmin(activeRule[124], funLevel_5))

    aggregate = getAggregate(len(action)-1,action,0)

    funResult = fuzz.defuzz(fun, aggregate, 'centroid')

    return funResult

