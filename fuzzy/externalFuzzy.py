import numpy as np
import skfuzzy as fuzz

def calculateExternalMandami(pm2_5, pm10, pm2_5norm, pm10norm):

    espPm10 = np.arange(0, pm10norm, 1)
    espPm2_5 = np.arange(0, pm2_5norm, 1)
    fun = np.arange(0,1024, 1)

    # Generate fuzzy membership functions
    espPm10VeryLow = fuzz.trimf(espPm10, [0, 0, 15])
    espPm10Low = fuzz.trimf(espPm10, [5, 15, 25])
    espPm10Mid = fuzz.trimf(espPm10, [15, 25, 35])
    espPm10High = fuzz.trimf(espPm10, [25, 35, 45])
    espPm10VeryHigh = fuzz.trimf(espPm10, [35, 50, 50])

    espPm25VeryLo = fuzz.trimf(espPm2_5, [0, 0, 5])
    espPm25Low = fuzz.trimf(espPm2_5, [0, 5, 10])
    espPm25Mid = fuzz.trimf(espPm2_5, [5, 10, 15])
    espPm25High = fuzz.trimf(espPm2_5, [10, 15, 20])
    espPm25VeryHigh = fuzz.trimf(espPm2_5, [15, 25, 25])

    funLevel_1 = fuzz.trimf(fun, [0, 150, 550])
    funLevel_2 = fuzz.trimf(fun, [200, 500, 700])
    funLevel_3 = fuzz.trimf(fun, [300, 600, 850])
    funLevel_4 = fuzz.trimf(fun, [500, 750, 900])
    funLevel_5 = fuzz.trimf(fun, [750, 1024, 1024])


    espPm10LevelVeryLow = fuzz.interp_membership(espPm10, espPm10VeryLow, pm10)
    espPm10LevelLow = fuzz.interp_membership(espPm10, espPm10Low, pm10)
    espPm10LevelMid = fuzz.interp_membership(espPm10, espPm10Mid, pm10)
    espPm10LevelHigh = fuzz.interp_membership(espPm10, espPm10High, pm10)
    espPm10LevelVeryHigh = fuzz.interp_membership(espPm10, espPm10VeryHigh, pm10)

    espPm25LevelVeryLow = fuzz.interp_membership(espPm2_5, espPm25VeryLo, pm2_5)
    espPm25LevelLow = fuzz.interp_membership(espPm2_5, espPm25Low, pm2_5)
    espPm25LevelMid = fuzz.interp_membership(espPm2_5, espPm25Mid, pm2_5)
    espPm25LevelHigh = fuzz.interp_membership(espPm2_5, espPm25High, pm2_5)
    espPm25LevelVeryHigh = fuzz.interp_membership(espPm2_5, espPm25VeryHigh, pm2_5)

    #definicja rul

    activeRule_1 = np.fmin(espPm25LevelVeryLow, espPm10LevelVeryLow)
    activeRule_2 = np.fmin(espPm25LevelVeryLow, espPm10LevelLow)
    activeRule_3 = np.fmin(espPm25LevelVeryLow, espPm10LevelMid)
    activeRule_4 = np.fmin(espPm25LevelVeryLow, espPm10LevelHigh)
    activeRule_5 = np.fmin(espPm25LevelVeryLow, espPm10LevelVeryHigh)
    activeRule_6 = np.fmin(espPm25LevelLow, espPm10LevelVeryLow)
    activeRule_7 = np.fmin(espPm25LevelLow, espPm10LevelLow)
    activeRule_8 = np.fmin(espPm25LevelLow, espPm10LevelMid)
    activeRule_9 = np.fmin(espPm25LevelLow, espPm10LevelHigh)
    activeRule_10 = np.fmin(espPm25LevelLow, espPm10LevelVeryHigh)
    activeRule_11 = np.fmin(espPm25LevelMid, espPm10LevelVeryLow)
    activeRule_12 = np.fmin(espPm25LevelMid, espPm10LevelLow)
    activeRule_13 = np.fmin(espPm25LevelMid, espPm10LevelMid)
    activeRule_14 = np.fmin(espPm25LevelMid, espPm10LevelHigh)
    activeRule_15 = np.fmin(espPm25LevelMid, espPm10LevelVeryHigh)
    activeRule_16 = np.fmin(espPm25LevelHigh, espPm10LevelVeryLow)
    activeRule_17 = np.fmin(espPm25LevelHigh, espPm10LevelLow)
    activeRule_18 = np.fmin(espPm25LevelHigh, espPm10LevelMid)
    activeRule_19 = np.fmin(espPm25LevelHigh, espPm10LevelHigh)
    activeRule_20 = np.fmin(espPm25LevelHigh, espPm10LevelVeryHigh)
    activeRule_21 = np.fmin(espPm25LevelVeryHigh, espPm10LevelVeryLow)
    activeRule_22 = np.fmin(espPm25LevelVeryHigh, espPm10LevelLow)
    activeRule_23 = np.fmin(espPm25LevelVeryHigh, espPm10LevelMid)
    activeRule_24 = np.fmin(espPm25LevelVeryHigh, espPm10LevelHigh)
    activeRule_25 = np.fmin(espPm25LevelVeryHigh, espPm10LevelVeryHigh)


    fan_action_1 = np.fmin(activeRule_1, funLevel_1)
    fan_action_2 = np.fmin(activeRule_2, funLevel_2)
    fan_action_3 = np.fmin(activeRule_3, funLevel_3)
    fan_action_4 = np.fmin(activeRule_4, funLevel_4)
    fan_action_5 = np.fmin(activeRule_5, funLevel_5)
    fan_action_6 = np.fmin(activeRule_6, funLevel_2)
    fan_action_7 = np.fmin(activeRule_7, funLevel_2)
    fan_action_8 = np.fmin(activeRule_8, funLevel_3)
    fan_action_9 = np.fmin(activeRule_9, funLevel_4)
    fan_action_10 = np.fmin(activeRule_10, funLevel_5)
    fan_action_11 = np.fmin(activeRule_11, funLevel_3)
    fan_action_12 = np.fmin(activeRule_12, funLevel_3)
    fan_action_13 = np.fmin(activeRule_13, funLevel_3)
    fan_action_14 = np.fmin(activeRule_14, funLevel_4)
    fan_action_15 = np.fmin(activeRule_15, funLevel_5)
    fan_action_16 = np.fmin(activeRule_16, funLevel_4)
    fan_action_17 = np.fmin(activeRule_17, funLevel_4)
    fan_action_18 = np.fmin(activeRule_18, funLevel_4)
    fan_action_19 = np.fmin(activeRule_19, funLevel_4)
    fan_action_20 = np.fmin(activeRule_20, funLevel_5)
    fan_action_21 = np.fmin(activeRule_21, funLevel_5)
    fan_action_22 = np.fmin(activeRule_22, funLevel_5)
    fan_action_23 = np.fmin(activeRule_23, funLevel_5)
    fan_action_24 = np.fmin(activeRule_24, funLevel_5)
    fan_action_25 = np.fmin(activeRule_25, funLevel_5)

    aggregate = np.fmax(fan_action_1,
                np.fmax(fan_action_2,
                np.fmax(fan_action_3,
                np.fmax(fan_action_4,
                np.fmax(fan_action_4,
                np.fmax(fan_action_5,
                np.fmax(fan_action_6,
                np.fmax(fan_action_7,
                np.fmax(fan_action_8,
                np.fmax(fan_action_9,
                np.fmax(fan_action_10,
                np.fmax(fan_action_11,
                np.fmax(fan_action_12,
                np.fmax(fan_action_13,
                np.fmax(fan_action_14,
                np.fmax(fan_action_15,
                np.fmax(fan_action_16,
                np.fmax(fan_action_17,
                np.fmax(fan_action_18,
                np.fmax(fan_action_19,
                np.fmax(fan_action_20,
                np.fmax(fan_action_21,
                np.fmax(fan_action_22,
                np.fmax(fan_action_23,
                np.fmax(fan_action_24,fan_action_25)))))))))))))))))))))))))

    funResult = fuzz.defuzz(fun, aggregate, 'centroid')

    return funResult