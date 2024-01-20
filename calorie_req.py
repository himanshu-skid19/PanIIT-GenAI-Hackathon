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

def check_meal(breakfast,lunch, dinner, diet_type):
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
    calorie = 4.0 * protein + 4.0 * (sugar + carb) + 9.0 * fat
    percent_protein = (4.0 * protein)/calorie
    percent_carb = (4.0 * (sugar + carb))/calorie
    percent_fat = (9.0 * fat)/calorie
    flag = 0
    if(diet_type == 'Balanced'):
        req_protein = 22.50
        req_carb = 52.50
        req_fat = 25
        if not(req_protein-2.5 <= percent_protein <= req_protein+2.5):
            flag = 1
        if not(req_carb-2.5 <= percent_carb <= req_carb+2.5):
            flag = 1
        if not(req_fat-2.5 <= percent_fat<= req_fat+2.5):
            flag = 1
    elif(diet_type == 'Heart-Healthy'):
        req_protein = 27.50
        req_carb = 50.00
        req_fat = 22.50
        if not(req_protein-2.5 <= percent_protein <= req_protein+2.5):
            flag = 1
        if not(req_carb-2.5 <= percent_carb <= req_carb+2.5):
            flag = 1
        if not(req_fat-2.5 <= percent_fat<= req_fat+2.5):
            flag = 1
    elif(diet_type == 'Low-Sugar'):
        req_protein = 25.00
        req_carb = 45.00
        req_fat = 30.00
        if not(req_protein-2.5 <= percent_protein <= req_protein+2.5):
            flag = 1
        if not(req_carb-2.5 <= percent_carb <= req_carb+2.5):
            flag = 1
        if not(req_fat-2.5 <= percent_fat<= req_fat+2.5):
            flag = 1
    if(flag == 0):
        return True
    else:
        return False
    















