import numpy as np
import skfuzzy as fuzz

def calculateIternalMandami(airlyCurrentMeassurment, espCurrentMeasurment, airlyForecastMeasurment):

    airlyCurrent = np.arange(0, 1024, 1)
    airlyForecast = np.arange(0, 1024, 1)
    esp_current = np.arange(0, 1024, 1)
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

    airlyCurrentVerylow = fuzz.interp_membership(airlyCurrent, airlyCurrent_1, airlyCurrentMeassurment)
    airlyCurrentLow = fuzz.interp_membership(airlyCurrent, airlyCurrent_2, airlyCurrentMeassurment)
    airlyCurrentMid = fuzz.interp_membership(airlyCurrent, airlyCurrent_3, airlyCurrentMeassurment)
    airlyCurrentHigh = fuzz.interp_membership(airlyCurrent, airlyCurrent_4, airlyCurrentMeassurment)
    airlyCurrentVeryHigh = fuzz.interp_membership(airlyCurrent, airlyCurrent_5, airlyCurrentMeassurment)

    espCurrentVeryLow = fuzz.interp_membership(esp_current, espCurrent_1, espCurrentMeasurment)
    espCurrentLow = fuzz.interp_membership(esp_current, espCurrent_2, espCurrentMeasurment)
    espCurrentMid = fuzz.interp_membership(esp_current, espCurrent_3, espCurrentMeasurment)
    espCurrentHigh = fuzz.interp_membership(esp_current, espCurrent_4, espCurrentMeasurment)
    espCurrentVeryHigh = fuzz.interp_membership(esp_current, espCurrent_5, espCurrentMeasurment)

    airlyForecastVeryLow = fuzz.interp_membership(airlyForecast, airlyForecast_1, airlyForecastMeasurment)
    airlyForecastLow = fuzz.interp_membership(airlyForecast, airlyForecast_2, airlyForecastMeasurment)
    airlyForecastMid = fuzz.interp_membership(airlyForecast, airlyForecast_3, airlyForecastMeasurment)
    airlyForecastHigh = fuzz.interp_membership(airlyForecast, airlyForecast_4, airlyForecastMeasurment)
    airlyForecastVeryHigh = fuzz.interp_membership(airlyForecast, airlyForecast_5, airlyForecastMeasurment)

    # define rules
    ###############################################################
    #IF
    active_rule_1 = np.fmin(airlyCurrentVerylow, airlyForecastVeryLow) # and
    fan_action_1 = np.fmin(active_rule_1, funLevel_1)
    ###############################################################
    # IF
    active_rule_2 = np.fmin(airlyCurrentVerylow, airlyForecastLow)  # and
    fan_action_2 = np.fmin(active_rule_2, funLevel_2)
    ###############################################################
    # IF
    active_rule_3= np.fmin(airlyCurrentVerylow, airlyForecastMid)  # and

    fan_action_3 = np.fmin(active_rule_3, funLevel_3)
    ###############################################################
    # IF
    active_rule_4= np.fmin(airlyCurrentVerylow, airlyForecastHigh)  # and

    fan_action_4 = np.fmin(active_rule_4, funLevel_4)
    ###############################################################
    # IF
    active_rule_5= np.fmin(airlyCurrentVerylow, airlyForecastVeryHigh)  # and

    fan_action_5 = np.fmin(active_rule_5, funLevel_5)
    ###############################################################
    # IF
    active_rule_6= np.fmin(airlyCurrentLow, airlyForecastVeryLow)  # and

    fan_action_6 = np.fmin(active_rule_6, funLevel_2)
    ###############################################################
    # IF
    active_rule_7= np.fmin(airlyCurrentLow, airlyForecastLow)  # and

    fan_action_7 = np.fmin(active_rule_7, funLevel_2)
    ###############################################################
    # IF
    active_rule_8= np.fmin(airlyCurrentLow, airlyForecastMid)  # and

    fan_action_8 = np.fmin(active_rule_8, funLevel_3)
    ###############################################################
    # IF
    active_rule_9= np.fmin(airlyCurrentLow, airlyForecastHigh)  # and

    fan_action_9 = np.fmin(active_rule_9, funLevel_4)
    ###############################################################
    # IF
    active_rule_10 = np.fmin(airlyCurrentLow, airlyForecastVeryHigh)  # and

    fan_action_10 = np.fmin(active_rule_10, funLevel_5)
    ###############################################################
    # IF
    active_rule_11 = np.fmin(airlyCurrentMid, airlyForecastVeryLow)  # and

    fan_action_11 = np.fmin(active_rule_11, funLevel_3)
    ###############################################################
    # IF
    active_rule_12 = np.fmin(airlyCurrentMid, airlyForecastLow)  # and

    fan_action_12 = np.fmin(active_rule_12, funLevel_3)
    ###############################################################
    # IF
    active_rule_13 = np.fmin(airlyCurrentMid, airlyForecastMid)  # and

    fan_action_13 = np.fmin(active_rule_13, funLevel_3)
    ###############################################################
    # IF
    active_rule_14 = np.fmin(airlyCurrentMid, airlyForecastHigh)  # and

    fan_action_14 = np.fmin(active_rule_14, funLevel_4)
    ###############################################################
    # IF
    active_rule_15 = np.fmin(airlyCurrentMid, airlyForecastVeryHigh)  # and

    fan_action_15 = np.fmin(active_rule_15, funLevel_5)
    ###############################################################
    # IF
    active_rule_16 = np.fmin(airlyCurrentHigh, airlyForecastVeryLow)  # and

    fan_action_16 = np.fmin(active_rule_16, funLevel_4)
    ###############################################################
    # IF
    active_rule_17 = np.fmin(airlyCurrentHigh, airlyForecastLow)  # and

    fan_action_17 = np.fmin(active_rule_17, funLevel_4)
    ###############################################################
    # IF
    active_rule_18 = np.fmin(airlyCurrentHigh, airlyForecastMid)  # and

    fan_action_18 = np.fmin(active_rule_18, funLevel_4)
    ###############################################################
    # IF
    active_rule_19 = np.fmin(airlyCurrentHigh, airlyForecastHigh)  # and

    fan_action_19 = np.fmin(active_rule_19, funLevel_4)
    ###############################################################
    # IF
    active_rule_20 = np.fmin(airlyCurrentHigh, airlyForecastVeryHigh)  # and

    fan_action_20 = np.fmin(active_rule_20, funLevel_5)
    ###############################################################
    # IF
    active_rule_21 = np.fmin(airlyCurrentVeryHigh, airlyForecastVeryLow)  # and

    fan_action_21 = np.fmin(active_rule_21, funLevel_5)
    ###############################################################
    # IF
    active_rule_22 = np.fmin(airlyCurrentVeryHigh, airlyForecastLow)  # and

    fan_action_22 = np.fmin(active_rule_22, funLevel_5)
    ###############################################################
    # IF
    active_rule_23 = np.fmin(airlyCurrentVeryHigh, airlyForecastMid)  # and

    fan_action_23 = np.fmin(active_rule_23, funLevel_5)
    ###############################################################
    # IF
    active_rule_24 = np.fmin(airlyCurrentVeryHigh, airlyForecastHigh)  # and

    fan_action_24 = np.fmin(active_rule_24, funLevel_5)
    ###############################################################
    # IF
    active_rule_25 = np.fmin(airlyCurrentVeryHigh, airlyForecastVeryHigh)  # and

    fan_action_25 = np.fmin(active_rule_25, funLevel_5)
    ###############################################################
    # IF
    active_rule_26 = np.fmin(espCurrentVeryLow, airlyForecastVeryLow)  # and

    fan_action_26 = np.fmin(active_rule_26, funLevel_1)
    ###############################################################
    # IF
    active_rule_27 = np.fmin(espCurrentVeryLow, airlyForecastLow)  # and

    fan_action_27 = np.fmin(active_rule_27, funLevel_2)
    ###############################################################
    # IF
    active_rule_28 = np.fmin(espCurrentVeryLow, airlyForecastMid)  # and

    fan_action_28 = np.fmin(active_rule_28, funLevel_3)
    ###############################################################
    # IF
    active_rule_29 = np.fmin(espCurrentVeryLow, airlyForecastHigh)  # and

    fan_action_29 = np.fmin(active_rule_29, funLevel_4)
    ###############################################################
    # IF
    active_rule_30 = np.fmin(espCurrentVeryLow, airlyForecastVeryHigh)  # and

    fan_action_30 = np.fmin(active_rule_30, funLevel_5)
    ###############################################################
    # IF
    active_rule_31 = np.fmin(espCurrentLow, airlyForecastVeryLow)  # and

    fan_action_31 = np.fmin(active_rule_31, funLevel_2)
    ###############################################################
    # IF
    active_rule_32 = np.fmin(espCurrentLow, airlyForecastLow)  # and

    fan_action_32 = np.fmin(active_rule_32, funLevel_2)
    ###############################################################
    # IF
    active_rule_33 = np.fmin(espCurrentLow, airlyForecastMid)  # and

    fan_action_33 = np.fmin(active_rule_33, funLevel_3)
    ###############################################################
    # IF
    active_rule_34 = np.fmin(espCurrentLow, airlyForecastHigh)  # and

    fan_action_34 = np.fmin(active_rule_34, funLevel_4)
    ###############################################################
    # IF
    active_rule_35 = np.fmin(espCurrentLow, airlyForecastVeryHigh)  # and

    fan_action_35 = np.fmin(active_rule_35, funLevel_5)
    ###############################################################
    # IF
    active_rule_36 = np.fmin(espCurrentMid, airlyForecastVeryLow)  # and

    fan_action_36 = np.fmin(active_rule_36, funLevel_3)
    ###############################################################
    # IF
    active_rule_37 = np.fmin(espCurrentMid, airlyForecastLow)  # and

    fan_action_37 = np.fmin(active_rule_37, funLevel_3)
    ###############################################################
    # IF
    active_rule_38 = np.fmin(espCurrentMid, airlyForecastMid)  # and

    fan_action_38 = np.fmin(active_rule_38, funLevel_3)
    ###############################################################
    # IF
    active_rule_39 = np.fmin(espCurrentMid, airlyForecastHigh)  # and

    fan_action_39 = np.fmin(active_rule_39, funLevel_4)
    ###############################################################
    # IF
    active_rule_40 = np.fmin(espCurrentMid, airlyForecastVeryHigh)  # and

    fan_action_40 = np.fmin(active_rule_40, funLevel_5)
    ###############################################################
    # IF
    active_rule_41 = np.fmin(espCurrentHigh, airlyForecastVeryLow)  # and

    fan_action_41 = np.fmin(active_rule_41, funLevel_4)
    ###############################################################
    # IF
    active_rule_42 = np.fmin(espCurrentHigh, airlyForecastLow)  # and

    fan_action_42 = np.fmin(active_rule_42, funLevel_4)
    ###############################################################
    # IF
    active_rule_43 = np.fmin(espCurrentHigh, airlyForecastMid)  # and

    fan_action_43 = np.fmin(active_rule_43, funLevel_4)
    ###############################################################
    # IF
    active_rule_44 = np.fmin(espCurrentHigh, airlyForecastHigh)  # and

    fan_action_44 = np.fmin(active_rule_44, funLevel_4)
    ###############################################################
    # IF
    active_rule_45 = np.fmin(espCurrentHigh, airlyForecastVeryHigh)  # and

    fan_action_45 = np.fmin(active_rule_45, funLevel_5)
    ###############################################################
    # IF
    active_rule_46 = np.fmin(espCurrentVeryHigh, airlyForecastVeryLow)  # and

    fan_action_46 = np.fmin(active_rule_46, funLevel_5)
    ###############################################################
    # IF
    active_rule_47 = np.fmin(espCurrentVeryHigh, airlyForecastLow)  # and

    fan_action_47 = np.fmin(active_rule_47, funLevel_5)
    ###############################################################
    # IF
    active_rule_48 = np.fmin(espCurrentVeryHigh, airlyForecastMid)  # and

    fan_action_48 = np.fmin(active_rule_48, funLevel_5)
    ###############################################################
    # IF
    active_rule_49 = np.fmin(espCurrentVeryHigh, airlyForecastHigh)  # and

    fan_action_49 = np.fmin(active_rule_49, funLevel_5)
    ###############################################################
    # IF
    active_rule_50 = np.fmin(espCurrentVeryHigh, airlyForecastVeryHigh)  # and
    fan_action_50 = np.fmin(active_rule_50, funLevel_5)
    ###############################################################
    # IF
    active_rule_51 = np.fmin(airlyCurrentVerylow, espCurrentVeryLow)  # and
    fan_action_51 = np.fmin(active_rule_51, funLevel_1)
    ###############################################################
    # IF
    active_rule_52 = np.fmin(airlyCurrentVerylow, espCurrentLow)  # and
    fan_action_52 = np.fmin(active_rule_52, funLevel_2)
    ###############################################################
    # IF
    active_rule_53 = np.fmin(airlyCurrentVerylow, espCurrentMid)  # and
    fan_action_53 = np.fmin(active_rule_53, funLevel_3)
    ###############################################################
    # IF
    active_rule_54 = np.fmin(airlyCurrentVerylow, espCurrentHigh)  # and
    fan_action_54 = np.fmin(active_rule_54, funLevel_4)
    ###############################################################
    # IF
    active_rule_55 = np.fmin(airlyCurrentVerylow, espCurrentVeryHigh)  # and
    fan_action_55 = np.fmin(active_rule_55, funLevel_5)
    ###############################################################
    # IF
    active_rule_56 = np.fmin(airlyCurrentLow, espCurrentVeryLow)  # and
    fan_action_56 = np.fmin(active_rule_56, funLevel_2)
    ###############################################################
    # IF
    active_rule_57 = np.fmin(airlyCurrentLow, espCurrentLow)  # and
    fan_action_57 = np.fmin(active_rule_57, funLevel_2)
    ###############################################################
    # IF
    active_rule_58 = np.fmin(airlyCurrentLow, espCurrentMid)  # and
    fan_action_58 = np.fmin(active_rule_58, funLevel_3)
    ###############################################################
    # IF
    active_rule_59 = np.fmin(airlyCurrentLow, espCurrentHigh)  # and
    fan_action_59 = np.fmin(active_rule_59, funLevel_4)
    ###############################################################
    # IF
    active_rule_60 = np.fmin(airlyCurrentLow, espCurrentVeryHigh)  # and
    fan_action_60 = np.fmin(active_rule_60, funLevel_5)
    ###############################################################
    # IF
    active_rule_61 = np.fmin(airlyCurrentMid, espCurrentVeryLow)  # and
    fan_action_61 = np.fmin(active_rule_61, funLevel_3)
    ###############################################################
    # IF
    active_rule_62 = np.fmin(airlyCurrentMid, espCurrentLow)  # and
    fan_action_62 = np.fmin(active_rule_62, funLevel_3)
    ###############################################################
    # IF
    active_rule_63 = np.fmin(airlyCurrentMid, espCurrentMid)  # and
    fan_action_63 = np.fmin(active_rule_63, funLevel_3)
    ###############################################################
    # IF
    active_rule_64 = np.fmin(airlyCurrentMid, espCurrentHigh)  # and
    fan_action_64 = np.fmin(active_rule_64, funLevel_4)
    ###############################################################
    # IF
    active_rule_65 = np.fmin(airlyCurrentMid, espCurrentVeryHigh)  # and
    fan_action_65 = np.fmin(active_rule_65, funLevel_5)
    ###############################################################
    # IF
    active_rule_66 = np.fmin(airlyCurrentHigh, espCurrentVeryLow)  # and
    fan_action_66 = np.fmin(active_rule_66, funLevel_4)
    ###############################################################
    # IF
    active_rule_67 = np.fmin(airlyCurrentHigh, espCurrentLow)  # and
    fan_action_67 = np.fmin(active_rule_67, funLevel_4)
    ###############################################################
    # IF
    active_rule_68 = np.fmin(airlyCurrentHigh, espCurrentMid)  # and
    fan_action_68 = np.fmin(active_rule_68, funLevel_4)
    ###############################################################
    # IF
    active_rule_69 = np.fmin(airlyCurrentHigh, espCurrentHigh)  # and
    fan_action_69 = np.fmin(active_rule_69, funLevel_4)
    ###############################################################
    # IF
    active_rule_70 = np.fmin(airlyCurrentHigh, espCurrentVeryHigh)  # and
    fan_action_70 = np.fmin(active_rule_70, funLevel_5)
    ###############################################################
    # IF
    active_rule_71 = np.fmin(airlyCurrentVeryHigh, espCurrentVeryLow)  # and
    fan_action_71 = np.fmin(active_rule_71, funLevel_5)
    ###############################################################
    # IF
    active_rule_72 = np.fmin(airlyCurrentVeryHigh, espCurrentLow)  # and
    fan_action_72 = np.fmin(active_rule_72, funLevel_5)
    ###############################################################
    # IF
    active_rule_73 = np.fmin(airlyCurrentVeryHigh, espCurrentMid)  # and
    fan_action_73 = np.fmin(active_rule_73, funLevel_5)
    ###############################################################
    # IF
    active_rule_74 = np.fmin(airlyCurrentVeryHigh, espCurrentHigh)  # and
    fan_action_74 = np.fmin(active_rule_74, funLevel_5)
    ###############################################################
    # IF
    active_rule_75 = np.fmin(airlyCurrentVeryHigh, espCurrentVeryHigh)  # and
    fan_action_75 = np.fmin(active_rule_75, funLevel_5)
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
            np.fmax(fan_action_24,
            np.fmax(fan_action_25,
            np.fmax(fan_action_26,
            np.fmax(fan_action_27,
            np.fmax(fan_action_28,
            np.fmax(fan_action_29,
            np.fmax(fan_action_30,
            np.fmax(fan_action_31,
            np.fmax(fan_action_32,
            np.fmax(fan_action_33,
            np.fmax(fan_action_34,
            np.fmax(fan_action_35,
            np.fmax(fan_action_36,
            np.fmax(fan_action_37,
            np.fmax(fan_action_38,
            np.fmax(fan_action_39,
            np.fmax(fan_action_40,
            np.fmax(fan_action_41,
            np.fmax(fan_action_42,
            np.fmax(fan_action_43,
            np.fmax(fan_action_44,
            np.fmax(fan_action_45,
            np.fmax(fan_action_46,
            np.fmax(fan_action_47,
            np.fmax(fan_action_48,
            np.fmax(fan_action_49,
            np.fmax(fan_action_50,
            np.fmax(fan_action_51,
            np.fmax(fan_action_52,
            np.fmax(fan_action_53,
            np.fmax(fan_action_54,
            np.fmax(fan_action_55,
            np.fmax(fan_action_56,
            np.fmax(fan_action_57,
            np.fmax(fan_action_58,
            np.fmax(fan_action_59,
            np.fmax(fan_action_60,
            np.fmax(fan_action_61,
            np.fmax(fan_action_62,
            np.fmax(fan_action_63,
            np.fmax(fan_action_64,
            np.fmax(fan_action_65,
            np.fmax(fan_action_66,
            np.fmax(fan_action_67,
            np.fmax(fan_action_68,
            np.fmax(fan_action_69,
            np.fmax(fan_action_70,
            np.fmax(fan_action_71,
            np.fmax(fan_action_72,
            np.fmax(fan_action_73,
            np.fmax(fan_action_74,fan_action_75,)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

    funResult = fuzz.defuzz(fun, aggregate, 'centroid')

    return funResult