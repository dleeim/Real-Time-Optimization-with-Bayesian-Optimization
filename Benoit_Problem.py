import numpy as np

# Actual Plant System (if noise exists it equals to np.sqrt(1e-3))
def Benoit_System_1(u, noise = 0):

    f = u[0] ** 2 + u[1] ** 2 + u[0] * u[1]
    if noise: 
        f += np.random.normal(0., np.sqrt(noise))

    return f

def Benoit_System_2(u, noise = 0):

    f = u[0] ** 2 + u[1] ** 2 + (1 - u[0] * u[1])**2
    if noise: 
        f += np.random.normal(0., np.sqrt(noise))

    return f


def con1_system(u, noise = 0):

    g1 = 1. - u[0] + u[1] ** 2 + 2. * u[1] - 2.
    if noise:
        g1 += np.random.normal(0., np.sqrt(noise))

    return -g1


def con1_system_tight(u, noise = 0):
    
    g1 = 1. - u[0] + u[1] ** 2 + 2. * u[1] 
    if noise:
        g1 += np.random.normal(0., np.sqrt(noise))

    return -g1


# Model of Plant System
def Benoit_Model_1(theta, u, d=[0,0], GP_m=0):
    f = theta[0]*(u[0]+d[0]) ** 2 + theta[1]*(u[1]+d[1]) ** 2

    if GP_m == True:
        modifier = GP_m.GP_inference_np(u+d)
        modifier_obj_m = modifier[0][0]
        f += modifier_obj_m

    return f

def con1_Model(theta, u, d=[0,0], GP_m=0):
    g1 = 1. - theta[2]*(u[0]+d[0]) + theta[3]*(u[1]+d[1]) ** 2

    if GP_m == True:
        modifier = GP_m.GP_inference_np(u+d)
        modifier_con_m = modifier[0][1]
        g1 += modifier_con_m

    return -g1