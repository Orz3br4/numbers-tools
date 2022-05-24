# Cell classes
CLASS_NUM = 3
XN = ['育寧', '芷薇', '姿穎', '家銘', '茗豐', '士寧', '素岑', '驊家', '慧瑜', '恩萱', '世淇', '玉彬', '庸正', '愷恩']
VIP = ['妍妤', '安晨', '銘鴻', '品嫻', '振瑜']
NF = ['樂婕', '若玲', '雅雯', '俊傑', '恩賢', '瑞霖', '芝均']

YN_EKK = ['育寧', '芷薇', '姿穎', '妍妤', '安晨', '樂婕', '芝均']
JM_EKK = ['家銘', '茗豐', '士寧', '銘鴻']
SU_EKK = ['素岑', '驊家', '慧瑜', '恩萱', '品嫻', '振瑜', '若玲', '雅雯']
SC_EKK = ['世淇', '玉彬', '庸正', '愷恩', '俊傑', '恩賢', '瑞霖']

# Data definitions
total_list = dict()
list_sabbath = []
list_cell = []
unclassified_names = []

# Functions
def check_role(name):

    if name in XN:
        return 0
    if name in VIP:
        return 1
    if name in NF:
        return 2
    return -1

def check_EKK(name):

    if name in YN_EKK:
        return 0
    if name in JM_EKK:
        return 1
    if name in SU_EKK:
        return 2
    if name in SC_EKK:
        return 3
    # If the name is not in above EKKs, then return -1, 
    # which indicates it is unclassified.
    return -1

def update_total_list(name, total_list):

    if name in total_list:
        total_list[name] += 1
    else:
        total_list[name] = 1

def update_attendance(name, role, atten):

    if role != -1:
        atten[role] += 1
    else:
        unclassified_names.append(name)

def show_unclassified_name(names):

    print('Unclassified name found:')
    for name in names:
        print(f'  - {name}')

def calculate_attendance(atten_list, total_list):

    # atten[0]: XN, atten[1]: VIP, atten[2]: NF
    atten = [0] * CLASS_NUM
    for name in atten_list:
        role = check_role(name)
        update_attendance(name, role, atten)
        update_total_list(name, total_list)

    # return format (XN_atten, VIP_atten, NF_atten)
    return (atten[0], atten[1], atten[2])

def calculate_unique_attendance(total_list):

    # atten[0]: XN, atten[1]: VIP, atten[2]: NF
    atten = [0] * CLASS_NUM
    for name in total_list:
        role = check_role(name)
        update_attendance(name, role, atten)

    # return format (XN_atten, VIP_atten, NF_atten)
    return (atten[0], atten[1], atten[2])

def calculate_EKK_attendance(atten_list, total_list, EKK):
    
    atten = [0] * CLASS_NUM

    for name in atten_list and name in EKK:
        role = check_role(name)
        update_attendance(name, role, atten)
        update_total_list(name, total_list)
    
    return (atten[0], atten[1], atten[2])

