from imports import *

def total_energy_req(age, weight, height, gender, pa):
    req = 0.0
    pa_val = 0.0
    
    if(gender == 'male' or gender == 'Male'):
        if(pa == 'Sedentary'):
            pa_val = 1.0
        elif(pa == 'Low active'):
            pa_val = 1.12
        elif(pa == 'Active'):
            pa_val = 1.27
        else:
            pa_val = 1.54
        req = 864-9.72*age+pa_val*(14.2*weight+503*height)
    else:
        if(pa == 'Sedentary'):
            pa_val = 1.0
        elif(pa == 'Low active'):
            pa_val = 1.14
        elif(pa == 'Active'):
            pa_val = 1.27
        else:
            pa_val = 1.45
        req = 387-7.31*age+pa_val*(10.9*weight+660.7*height)
    return req

def check_meal(breakfast,lunch, dinner, diet_type, target_weight, number_of_days, age, weight, height, gender, pa):
    cal_req = total_energy_req(age, weight, height, gender, pa)
    kcal_per_kg = 7700
    protein = 0.0
    calorie = 0.0
    carb = 0.0
    sugar = 0.0
    fat = 0.0
    percent_protein = 0.0
    req_protein = 0.0
    percent_carb = 0.0
    req_carb = 0.0
    percent_fat = 0.0
    req_fat = 0.0
    kcal_def = 0.0
    for k in breakfast.keys:
        if(k == 'Protein'):
            protein += breakfast[k]+lunch[k]+dinner[k]
        elif(k == 'Calorie'):
            calorie += breakfast[k]+lunch[k]+dinner[k]
        elif(k == 'Carbohydrate'):
            carb += breakfast[k]+lunch[k]+dinner[k]
        elif(k == 'Sugar'):
            sugar += breakfast[k]+lunch[k]+dinner[k]
        else:
            fat += breakfast[k]+lunch[k]+dinner[k]
    flag = 0
    calorie = 4.0 * protein + 4.0 * (sugar + carb) + 9.0 * fat
    percent_protein = (4.0 * protein)/calorie
    percent_carb = (4.0 * (sugar + carb))/calorie
    percent_fat = (9.0 * fat)/calorie
    p_range = 2.5
    if(diet_type == 'Balanced'):
        req_protein = 22.50
        req_carb = 52.50
        req_fat = 25
        if not(req_protein- p_range  <= percent_protein <= req_protein+ p_range ):
            flag = 1
        if not(req_carb- p_range  <= percent_carb <= req_carb+ p_range ):
            flag = 1
        if not(req_fat- p_range  <= percent_fat<= req_fat+ p_range ):
            flag = 1
    elif(diet_type == 'Heart-Healthy'):
        req_protein = 27.50
        req_carb = 50.00
        req_fat = 22.50
        if not(req_protein- p_range  <= percent_protein <= req_protein+ p_range ):
            flag = 1
        if not(req_carb- p_range <= percent_carb <= req_carb+ p_range ):
            flag = 1
        if not(req_fat- p_range  <= percent_fat<= req_fat+ p_range ):
            flag = 1
    elif(diet_type == 'Low-Sugar'):
        req_protein = 25.00
        req_carb = 45.00
        req_fat = 30.00
        if not(req_protein- p_range  <= percent_protein <= req_protein+ p_range ):
            flag = 1
        if not(req_carb- p_range  <= percent_carb <= req_carb+ p_range ):
            flag = 1
        if not(req_fat- p_range  <= percent_fat<= req_fat+ p_range ):
            flag = 1
    kcal_def = ((weight-target_weight)*kcal_per_kg)/number_of_days
    kcal_def_actual = cal_req-calorie
    range_cal_def = 0.05
    s_factor = 1.0
    
    if(flag == 0):
        if(kcal_def < 0):
            s_factor = (cal_req+kcal_def)/calorie
        else:
            if((cal_req-calorie) < (1-range_cal_def)*(kcal_def)):
                s_factor = (cal_req-(kcal_def)*(1-range_cal_def))/calorie
            elif((cal_req-calorie) >= (1+range_cal_def)*(kcal_def)):
                s_factor = (cal_req-kcal_def*(1+range_cal_def))/calorie
        return (s_factor, True)
    else:
        return (0, False)
    