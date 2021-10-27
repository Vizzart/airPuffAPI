import numpy as np
import skfuzzy as fuzz


# from skfuzzy import control as ctrl


def calculateMandami(espPm25CurrentValue,espPm10CurrentValue):
    # normy pyłów
    pm10normforESP = 50.0
    pm2_5normforESP = 25.0

    #
    esp_pm10 = np.arange(0, pm10normforESP, 1)
    esp_pm2_5 = np.arange(0, pm2_5normforESP, 1)
    fun = np.arange(0, 1024, 1)

    # Generate fuzzy membership functions
    esp_pm10_very_lo = fuzz.trimf(esp_pm10, [0, 0, 15])
    esp_pm10_lo = fuzz.trimf(esp_pm10, [5, 15, 25])
    esp_pm10_md = fuzz.trimf(esp_pm10, [15, 25, 35])
    esp_pm10_hi = fuzz.trimf(esp_pm10, [25, 35, 45])
    esp_pm10_very_hi = fuzz.trimf(esp_pm10, [35, 50, 50])

    esp_pm25_very_lo = fuzz.trimf(esp_pm2_5, [0, 0, 5])
    esp_pm25_lo = fuzz.trimf(esp_pm2_5, [0, 5, 10])
    esp_pm25_md = fuzz.trimf(esp_pm2_5, [5, 10, 15])
    esp_pm25_hi = fuzz.trimf(esp_pm2_5, [10, 15, 20])
    esp_pm25_very_hi = fuzz.trimf(esp_pm2_5, [15, 25, 25])

    fun_level_1 = fuzz.trimf(fun, [0, 0, 550])
    fun_level_2 = fuzz.trimf(fun, [0, 650, 750])
    fun_level_3 = fuzz.trimf(fun, [650, 750, 850])
    fun_level_4 = fuzz.trimf(fun, [850, 950 , 1000])
    fun_level_5 = fuzz.trimf(fun, [950, 1024, 1024])

    # pobrane wartosci z skryptu connectDataBase
    # aktualne wartosci z ESP
    # espPm25CurrentValue = 10 # getCurrentPm25fromESP ()
    # espPm10CurrentValue = 25  # getcurrentPm10fromESP ()


    esp_pm10Level_very_lo = fuzz.interp_membership(esp_pm10, esp_pm10_very_lo, espPm10CurrentValue)
    esp_pm10Level_lo = fuzz.interp_membership(esp_pm10, esp_pm10_lo, espPm10CurrentValue)
    esp_pm10Level_md = fuzz.interp_membership(esp_pm10, esp_pm10_md, espPm10CurrentValue)
    esp_pm10Level_hi = fuzz.interp_membership(esp_pm10, esp_pm10_hi, espPm10CurrentValue)
    esp_pm10Level_very_hi = fuzz.interp_membership(esp_pm10, esp_pm10_very_hi, espPm10CurrentValue)

    esp_pm25Level_very_lo = fuzz.interp_membership(esp_pm2_5, esp_pm25_very_lo, espPm25CurrentValue)
    esp_pm25Level_lo = fuzz.interp_membership(esp_pm2_5, esp_pm25_lo, espPm25CurrentValue)
    esp_pm25Level_md = fuzz.interp_membership(esp_pm2_5, esp_pm25_md, espPm25CurrentValue)
    esp_pm25Level_hi = fuzz.interp_membership(esp_pm2_5, esp_pm25_hi, espPm25CurrentValue)
    esp_pm25Level_very_hi = fuzz.interp_membership(esp_pm2_5, esp_pm25_very_hi, espPm25CurrentValue)

    # define rules
    ###############################################################
    #IF
    active_rule_1 = np.fmin(esp_pm25Level_very_lo, esp_pm10Level_very_lo)  # and
    fan_action_1 = np.fmin(active_rule_1, fun_level_1)
    ###############################################################
    ###############################################################
    # IF
    active_rule_2 = np.fmin(esp_pm25Level_very_lo, esp_pm10Level_lo)  # and
    fan_action_2 = np.fmin(active_rule_2, fun_level_2)
    ###############################################################
    # IF
    active_rule_3= np.fmin(esp_pm25Level_very_lo, esp_pm10Level_md)  # and
    fan_action_3 = np.fmin(active_rule_3, fun_level_3)
    ###############################################################
    # IF
    active_rule_4= np.fmin(esp_pm25Level_very_lo, esp_pm10Level_hi)  # and
    fan_action_4 = np.fmin(active_rule_4, fun_level_4)
    ###############################################################
    # IF
    active_rule_5= np.fmin(esp_pm25Level_very_lo, esp_pm10Level_very_hi)  # and
    fan_action_5 = np.fmin(active_rule_5, fun_level_5)
    ###############################################################
    # IF
    active_rule_6= np.fmin(esp_pm25Level_lo, esp_pm10Level_very_lo)  # and
    fan_action_6 = np.fmin(active_rule_6, fun_level_2)
    ###############################################################
    # IF
    active_rule_7= np.fmin(esp_pm25Level_lo, esp_pm10Level_lo)  # and
    fan_action_7 = np.fmin(active_rule_7, fun_level_2)
    ###############################################################
    # IF
    active_rule_8= np.fmin(esp_pm25Level_lo, esp_pm10Level_md)  # and
    fan_action_8 = np.fmin(active_rule_8, fun_level_3)
    ###############################################################
    # IF
    active_rule_9= np.fmin(esp_pm25Level_lo, esp_pm10Level_hi)  # and
    fan_action_9 = np.fmin(active_rule_9, fun_level_4)
    ###############################################################
    # IF
    active_rule_10 = np.fmin(esp_pm25Level_lo, esp_pm10Level_very_hi)  # and
    fan_action_10 = np.fmin(active_rule_10, fun_level_5)
    ###############################################################
    # IF
    active_rule_11 = np.fmin(esp_pm25Level_md, esp_pm10Level_very_lo)  # and
    fan_action_11 = np.fmin(active_rule_11, fun_level_3)
    ###############################################################
    # IF
    active_rule_12 = np.fmin(esp_pm25Level_md, esp_pm10Level_lo)  # and
    fan_action_12 = np.fmin(active_rule_12, fun_level_3)
    ###############################################################
    # IF
    active_rule_13 = np.fmin(esp_pm25Level_md, esp_pm10Level_md)  # and
    fan_action_13 = np.fmin(active_rule_13, fun_level_3)
    ###############################################################
    # IF
    active_rule_14 = np.fmin(esp_pm25Level_md, esp_pm10Level_hi)  # and
    fan_action_14 = np.fmin(active_rule_14, fun_level_4)
    ###############################################################
    # IF
    active_rule_15 = np.fmin(esp_pm25Level_md, esp_pm10Level_very_hi)  # and
    fan_action_15 = np.fmin(active_rule_15, fun_level_5)
    ###############################################################
    # IF
    active_rule_16 = np.fmin(esp_pm25Level_hi, esp_pm10Level_very_lo)  # and
    fan_action_16 = np.fmin(active_rule_16, fun_level_4)
    ###############################################################
    # IF
    active_rule_17 = np.fmin(esp_pm25Level_hi, esp_pm10Level_lo)  # and
    fan_action_17 = np.fmin(active_rule_17, fun_level_4)
    ###############################################################
    # IF
    active_rule_18 = np.fmin(esp_pm25Level_hi, esp_pm10Level_md)  # and

    fan_action_18 = np.fmin(active_rule_18, fun_level_4)
    ###############################################################
    # IF
    active_rule_19 = np.fmin(esp_pm25Level_hi, esp_pm10Level_hi)  # and

    fan_action_19 = np.fmin(active_rule_19, fun_level_4)
    ###############################################################
    # IF
    active_rule_20 = np.fmin(esp_pm25Level_hi, esp_pm10Level_very_hi)  # and

    fan_action_20 = np.fmin(active_rule_20, fun_level_5)
    ###############################################################
    # IF
    active_rule_21 = np.fmin(esp_pm25Level_very_hi, esp_pm10Level_very_lo)  # and

    fan_action_21 = np.fmin(active_rule_21, fun_level_5)
    ###############################################################
    # IF
    active_rule_22 = np.fmin(esp_pm25Level_very_hi, esp_pm10Level_lo)  # and

    fan_action_22 = np.fmin(active_rule_22, fun_level_5)
    ###############################################################
    # IF
    active_rule_23 = np.fmin(esp_pm25Level_very_hi, esp_pm10Level_md)  # and

    fan_action_23 = np.fmin(active_rule_23, fun_level_5)
    ###############################################################
    # IF
    active_rule_24 = np.fmin(esp_pm25Level_very_hi, esp_pm10Level_hi)  # and

    fan_action_24 = np.fmin(active_rule_24, fun_level_5)
    ###############################################################
    # IF
    active_rule_25 = np.fmin(esp_pm25Level_very_hi, esp_pm10Level_very_hi)  # and

    fan_action_25 = np.fmin(active_rule_25, fun_level_5)
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

    funResult = fuzz.defuzz(fun, aggregate, 'lom')

    return funResult