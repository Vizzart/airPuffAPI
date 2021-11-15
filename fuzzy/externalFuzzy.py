import numpy as np
import skfuzzy as fuzz


def calculateExternalMandami(pm2_5, pm10, pm2_5norm, pm10norm):
    espPm10 = np.arange(1, pm10norm +1, 1)
    espPm2_5 = np.arange(0, pm2_5norm +1, 1)
    fun = np.arange(0,1024+1, 1)

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

    # pobrane wartosci z skryptu connectDataBase
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

    # define rules
    ## esp10_very_low & esp25_very_low
    ###############################################################
    # IF
    active_rule_1 = np.fmin(espPm25LevelVeryLow, espPm10LevelVeryLow)  # and
    fan_action_1 = np.fmin(active_rule_1, funLevel_1)
    ###############################################################
    # IF
    active_rule_2 = np.fmin(espPm25LevelVeryLow, espPm10LevelLow)  # and
    fan_action_2 = np.fmin(active_rule_2, funLevel_2)
    ###############################################################
    # IF
    active_rule_3 = np.fmin(espPm25LevelVeryLow, espPm10LevelMid)  # and
    fan_action_3 = np.fmin(active_rule_3, funLevel_3)
    ###############################################################
    # IF
    active_rule_4 = np.fmin(espPm25LevelVeryLow, espPm10LevelHigh)  # and
    fan_action_4 = np.fmin(active_rule_4, funLevel_4)
    ###############################################################
    # IF
    active_rule_5 = np.fmin(espPm25LevelVeryLow, espPm10LevelVeryHigh)  # and
    fan_action_5 = np.fmin(active_rule_5, funLevel_5)
    ###############################################################
    # IF
    active_rule_6 = np.fmin(espPm25LevelLow, espPm10LevelVeryLow)  # and
    fan_action_6 = np.fmin(active_rule_6, funLevel_2)
    ###############################################################
    # IF
    active_rule_7 = np.fmin(espPm25LevelLow, espPm10LevelLow)  # and
    fan_action_7 = np.fmin(active_rule_7, funLevel_2)
    ###############################################################
    # IF
    active_rule_8 = np.fmin(espPm25LevelLow, espPm10LevelMid)  # and
    fan_action_8 = np.fmin(active_rule_8, funLevel_3)
    ###############################################################
    # IF
    active_rule_9 = np.fmin(espPm25LevelLow, espPm10LevelHigh)  # and
    fan_action_9 = np.fmin(active_rule_9, funLevel_4)
    ###############################################################
    # IF
    active_rule_10 = np.fmin(espPm25LevelLow, espPm10LevelVeryHigh)  # and
    fan_action_10 = np.fmin(active_rule_10, funLevel_5)
    ###############################################################
    # IF
    active_rule_11 = np.fmin(espPm25LevelMid, espPm10LevelVeryLow)  # and
    fan_action_11 = np.fmin(active_rule_11, funLevel_3)
    ###############################################################
    # IF
    active_rule_12 = np.fmin(espPm25LevelMid, espPm10LevelLow)  # and
    fan_action_12 = np.fmin(active_rule_12, funLevel_3)
    ###############################################################
    # IF
    active_rule_13 = np.fmin(espPm25LevelMid, espPm10LevelMid)  # and
    fan_action_13 = np.fmin(active_rule_13, funLevel_3)
    ###############################################################
    # IF
    active_rule_14 = np.fmin(espPm25LevelMid, espPm10LevelHigh)  # and
    fan_action_14 = np.fmin(active_rule_14, funLevel_4)
    ###############################################################
    # IF
    active_rule_15 = np.fmin(espPm25LevelMid, espPm10LevelVeryHigh)  # and
    fan_action_15 = np.fmin(active_rule_15, funLevel_5)
    ###############################################################
    # IF
    active_rule_16 = np.fmin(espPm25LevelHigh, espPm10LevelVeryLow)  # and
    fan_action_16 = np.fmin(active_rule_16, funLevel_4)
    ###############################################################
    # IF
    active_rule_17 = np.fmin(espPm25LevelHigh, espPm10LevelLow)  # and
    fan_action_17 = np.fmin(active_rule_17, funLevel_4)
    ###############################################################
    # IF
    active_rule_18 = np.fmin(espPm25LevelHigh, espPm10LevelMid)  # and
    fan_action_18 = np.fmin(active_rule_18, funLevel_4)
    ###############################################################
    # IF
    active_rule_19 = np.fmin(espPm25LevelHigh, espPm10LevelHigh)  # and

    fan_action_19 = np.fmin(active_rule_19, funLevel_4)
    ###############################################################
    # IF
    active_rule_20 = np.fmin(espPm25LevelHigh, espPm10LevelVeryHigh)  # and

    fan_action_20 = np.fmin(active_rule_20, funLevel_5)
    ###############################################################
    # IF
    active_rule_21 = np.fmin(espPm25LevelVeryHigh, espPm10LevelVeryLow)  # and

    fan_action_21 = np.fmin(active_rule_21, funLevel_5)
    ###############################################################
    # IF
    active_rule_22 = np.fmin(espPm25LevelVeryHigh, espPm10LevelLow)  # and

    fan_action_22 = np.fmin(active_rule_22, funLevel_5)
    ###############################################################
    # IF
    active_rule_23 = np.fmin(espPm25LevelVeryHigh, espPm10LevelMid)  # and

    fan_action_23 = np.fmin(active_rule_23, funLevel_5)
    ###############################################################
    # IF
    active_rule_24 = np.fmin(espPm25LevelVeryHigh, espPm10LevelHigh)  # and
    fan_action_24 = np.fmin(active_rule_24, funLevel_5)
    ###############################################################
    # IF
    active_rule_25 = np.fmin(espPm25LevelVeryHigh, espPm10LevelVeryHigh)  # and
    fan_action_25 = np.fmin(active_rule_25, funLevel_5)
    ###############################################################
    # Aggregate all three output membership functions together
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