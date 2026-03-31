






def water_column_height(tower_height, tank_height):

    colume_height = tower_height + (3* tank_height)/4

    return colume_height

def pressure_gain_from_water_height(height):

    pressure = (998.2*9.80665*height)/1000

    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    
    pressure_lost = (-friction_factor*pipe_length*998.2*fluid_velocity**2)/(2000*pipe_diameter)
    
    return pressure_lost

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):

    pressure_loss_from_fittings = (-0.04*998.2*fluid_velocity**2*quantity_fittings)/(2000)

    return pressure_loss_from_fittings

def reynolds_number(hydraulic_diameter, fluid_velocity):

    reynolds_number = (998.2*hydraulic_diameter*fluid_velocity)/(0.0010016)

    return reynolds_number

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):

    k_level = (0.1+(50/reynolds_number))*((larger_diameter/smaller_diameter)**4-1)

    pressure_loss_from_pipe_reduction = (-k_level*998.2*fluid_velocity**2)/(2000)

    return pressure_loss_from_pipe_reduction

def psi_to_kpa(kilopascal):

    psi = kilopascal * 0.14503773773020923

    return psi

