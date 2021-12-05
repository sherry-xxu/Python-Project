#!/usr/bin/env python
# coding: utf-8

# **Thoughts on insurance.csv dataset**
# 1. Dataset
#     1. Columns
#         1. Age - int
#         2. Sex - female/male
#         3. BMI - float
#         4. Children - int
#         5. Smoking - yes/no
#         6. Region: northeast/northwest/southeast/southwest
#         7. Charges: float
# 
#     2. Questions came up while looking through dataset:
#         1. What region has the highest average health insurance charges? What is the most prominent factor (age/sex/bmi/children/smoking) that results in high average health insurance?
#         2. relationship between age and bmi?
#         3. relationship between region and smoking?
#         4. Smokers will have higher bmi than non-smokers?
# 
# 2. Data I need for Question1
#     1. region
#     2. health insurance charges
#      
# 3. What analysis needs to be done
#     1. descriptive analysis
#     2. goal: Find major factor that affects high health insurance in one region and come up with solutions to decrease average health insurance costs for that region.

# In[32]:


import csv

#create a list for each title
list_ages = []
list_sex = []
list_bmis = []
list_children = []
list_smoker = []
list_regions = []
list_charges = []
with open('insurance.csv', newline='') as insurance_csv:
    insurance_reader = csv.DictReader(insurance_csv)
    for row in insurance_reader:
        list_ages.append(row['age'])
        list_sex.append(row['sex'])
        list_bmis.append(row['bmi'])
        list_children.append(row['children'])
        list_smoker.append(row['smoker'])
        list_regions.append(row['region'])
        list_charges.append(row['charges'])

#create a dictionary with all data in a format {insurer_id: {insurer data}}
def insurance_dictionary():
    insurance_dict = {}
    for i in range(len(list_ages)):
        insurance_dict[i] =         {'Age': int(list_ages[i]),
        'Sex': list_sex[i],
        'BMI': float(list_bmis[i]),
        'Children': int(list_children[i]),
        'Smoker': list_smoker[i],
        'Region': list_regions[i],
        'Charges': float(list_charges[i])}
    return insurance_dict
    
insurance_dict = insurance_dictionary()
#print(insurance_dictionary())


# In[33]:


#create a dictionary with keys as regions and values as insurer's data
def region_dictionary():
    region_dict = {'southeast': [], 'southwest': [], 'northeast': [], 'northwest': []}
    for insurer_data in insurance_dict.values():
        if insurer_data['Region'] == 'southeast':
            region_dict['southeast'].append(insurer_data)
        elif insurer_data['Region'] == 'southwest':
            region_dict['southwest'].append(insurer_data)
        elif insurer_data['Region'] == 'northeast':
            region_dict['northeast'].append(insurer_data)
        elif insurer_data['Region'] == 'northwest':
            region_dict['northwest'].append(insurer_data)
    return region_dict

region_dict = region_dictionary()
#print(region_dict)
            


# In[7]:


#calculate the length of each region's list
num_of_se = len(region_dict['southeast'])
num_of_sw = len(region_dict['southwest'])
num_of_ne = len(region_dict['northeast'])
num_of_nw = len(region_dict['northwest'])

print(num_of_se)
print(num_of_sw)
print(num_of_ne)
print(num_of_nw)


# In[56]:




#calculate each region's average insurance charges
# total_charges_se = 0
# for insurer_data in region_dict['southeast']:
#     total_charges_se += insurer_data['Charges']
# print(total_charges_se)
    
#create a class to calculate each region's average insurance charge
class AverageCharge:
    def __init__(self, num_of_region_insurer):
        self.num_of_region_insurer = num_of_region_insurer
        
    def total_charges_region(self, region_in_dict):
        total_charge = 0
        for insurer_data in region_in_dict:
            total_charge += insurer_data['Charges']
        return total_charge
    
    def average_charge_region(self, total_charge):
        average_charge = total_charge / self.num_of_region_insurer
        return average_charge


# In[ ]:


charge_se = AverageCharge(num_of_se)
charge_se.total_charges_region(region_dict['southeast'])
charge_se.average_charge_region(5363689.763290002)
#average charges of southeast is $14735.411437609895


# In[61]:


charge_sw = AverageCharge(num_of_sw)
charge_sw.total_charges_region(region_dict['southwest'])
charge_sw.average_charge_region(4012754.647620001)
#average charges of southwest is $12346.93737729231


# In[64]:


charge_ne = AverageCharge(num_of_ne)
charge_ne.total_charges_region(region_dict['northeast'])
charge_ne.average_charge_region(4343668.583308999)
#average charges of northeast is $13406.3845163858


# In[67]:


charge_nw = AverageCharge(num_of_nw)
charge_nw.total_charges_region(region_dict['northwest'])
charge_nw.average_charge_region(4035711.9965399993)
#average charges of northwest is $12417.575373969228


# Average charges of regions:\
# Southeast: 14735.411437609895\
# Southwest: 12346.93737729231\
# Northeast: 13406.3845163858\
# Northwest: 12417.575373969228

# Southest region has the highest average insurance charges $14735.411437609895.

# In[68]:


#average age of insurers in regions
class AverageAge():
    def __init__(self, num_of_region_insurer):
        self.num_of_region_insurer = num_of_region_insurer
        
    def average_age(self,region_in_dict):
        total_age = 0
        for insurer_data in region_in_dict:
            total_age += insurer_data['Age']
        ave_age = total_age / self.num_of_region_insurer
        return ave_age
    
            


# In[71]:


age_se = AverageAge(num_of_se)
age_se.average_age(region_dict['southeast'])


# In[72]:


age_sw = AverageAge(num_of_sw)
age_sw.average_age(region_dict['southwest'])


# In[74]:


age_ne = AverageAge(num_of_ne)
age_ne.average_age(region_dict['northeast'])


# In[75]:


age_nw = AverageAge(num_of_nw)
age_ne.average_age(region_dict['northwest'])


# Average age for regions:\
# Southeast: 38.93956043956044\
# Southwest: 39.45538461538462\
# Northeast: 39.26851851851852\
# Northwest: 39.3179012345679

# In[87]:


#create a dictionary with key as regions value is a dictionary, in which keys are male or female and values are the numbers
def male_female_dict():
    
    
    m_f_dict = {'southeast': {}, 'southwest': {}, 'northeast': {}, 'northwest': {}}
    for key, value in region_dict.items():
        male_num = 0
        female_num = 0
        if key == 'southeast':
            for insurer_data in value:
                if insurer_data['Sex'] == 'male':
                    male_num += 1
                else:
                    female_num += 1
            m_f_dict['southeast'].update({'male': male_num, 'female': female_num})
        if key == 'southwest':
            for insurer_data in value:
                if insurer_data['Sex'] == 'male':
                    male_num += 1
                else:
                    female_num += 1
            m_f_dict['southwest'].update({'male': male_num, 'female': female_num})
        if key == 'northeast':
            for insurer_data in value:
                if insurer_data['Sex'] == 'male':
                    male_num += 1
                else:
                    female_num += 1
            m_f_dict['northeast'].update({'male': male_num, 'female': female_num})
        if key == 'northwest':
             for insurer_data in value:
                if insurer_data['Sex'] == 'male':
                    male_num += 1
                else:
                    female_num += 1
        m_f_dict['northwest'].update({'male': male_num, 'female': female_num})
    
    
    return m_f_dict
print(male_female_dict())
    


# Southest region has relatively more male insurers than female insurers compared to the other three regions.

# In[1]:


#average bmi for each region
class AverageBMI:
    def __init__(self, num_of_region_insurer):
        self.num_of_region_insurer = num_of_region_insurer
        
    def average_bmi(self, region_in_dict):
        total_bmi = 0
        for insurer_data in region_in_dict:
            total_bmi += insurer_data['BMI']
        ave_bmi = total_bmi / self.num_of_region_insurer
        return ave_bmi


# In[8]:


bmi_se = AverageBMI(num_of_se)
bmi_se.average_bmi(region_dict['southeast'])


# In[9]:


bmi_sw = AverageBMI(num_of_sw)
bmi_sw.average_bmi(region_dict['southwest'])


# In[10]:


bmi_ne = AverageBMI(num_of_ne)
bmi_ne.average_bmi(region_dict['northeast'])


# In[11]:


bmi_nw = AverageBMI(num_of_nw)
bmi_nw.average_bmi(region_dict['northwest'])


# Average BMI for regions:\
# Southeast: 33.35598901098903\
# Southwest: 30.59661538461538\
# Northeast: 29.17350308641976\
# Northwest: 29.199784615384626\
# \
# Southeast region has the highest average BMI among four regions.

# In[15]:


#average number of children per each insurer
class AverageChildren:
    def __init__(self, num_of_region_insurer):
        self.num_of_region_insurer = num_of_region_insurer
        
    def average_children(self, region_in_dict):
        total_children = 0
        for insurer_data in region_in_dict:
            total_children += insurer_data['Children']
        ave_children = total_children / self.num_of_region_insurer
        return ave_children


# In[16]:


children_se = AverageChildren(num_of_se)
children_se.average_children(region_dict['southeast'])


# In[17]:


children_sw = AverageChildren(num_of_sw)
children_sw.average_children(region_dict['southwest'])


# In[18]:


children_ne = AverageChildren(num_of_ne)
children_ne.average_children(region_dict['northeast'])


# In[19]:


children_nw = AverageChildren(num_of_nw)
children_nw.average_children(region_dict['northwest'])


# Average number of children included in a insurer of regions:\
# Southeast: 1.0494505494505495\
# Southwest: 1.1415384615384616\
# Northeast: 1.0462962962962963\
# Northwest: 1.1476923076923078\
# \
# Insurers in four regions have similar average number of children.

# In[30]:


#calculate the percentage of smokers in each region
def num_of_smoker():
    smoker_percent = {}
    for key, value in region_dict.items():
        number_of_smoker = 0
        if key == 'southeast':
            for insurer_data in value:
                if insurer_data['Smoker'] == 'yes':
                    number_of_smoker += 1
                else:
                    continue
            smoker_percentage = number_of_smoker / num_of_se * 100
            smoker_percent['southeast'] = smoker_percentage
        
        if key == 'southwest':
            for insurer_data in value:
                if insurer_data['Smoker'] == 'yes':
                    number_of_smoker += 1
                else:
                    continue
            smoker_percentage = number_of_smoker / num_of_sw * 100
            smoker_percent['southwest'] = smoker_percentage
            
        if key == 'northeast':
            for insurer_data in value:
                if insurer_data['Smoker'] == 'yes':
                    number_of_smoker += 1
                else:
                    continue
            smoker_percentage = number_of_smoker / num_of_ne * 100
            smoker_percent['northeast'] = smoker_percentage
            
        if key == 'northwest':
            for insurer_data in value:
                if insurer_data['Smoker'] == 'yes':
                    number_of_smoker += 1
                else:
                    continue
            smoker_percentage = number_of_smoker / num_of_nw * 100
            smoker_percent['northwest'] = smoker_percentage
    return smoker_percent
    smoker_percent = num_of_smoker()


# In[31]:


print(num_of_smoker())


# Smoker percentage of regions:\
# Southeast: 25.0\
# Southwest: 17.846153846153847\
# Northeast: 20.679012345679013\
# Northwest: 17.846153846153847\
# \
# Insurers in southeast region has the highest percentage of smokers among all four regions.

# **Conclusion:**\
# __Southeast Region__\
# Surveyed insurer population: 364\
# Average age of insurer: 38.94
# Surveryed male/female insurer: 189/175\
# Average BMI of insurer: 33.36\
# Average number of children: 1.05\
# Smoker percentage: 25.0\
# Average insurance charges: 14735.41\
# \
# \
# __Southwest Region__\
# Surveyed insurer population: 325\
# Average age of insurer: 39.46
# Surveryed male/female insurer: 163/162\
# Average BMI of insurer: 30.60\
# Average number of children: 1.14\
# Smoker percentage: 17.85\
# Average insurance charges: 12346.94\
# \
# \
# __Northeast Region__\
# Surveyed insurer population: 324\
# Average age of insurer: 39.27
# Surveryed male/female insurer: 163/161\
# Average BMI of insurer: 29.17\
# Average number of children: 1.05\
# Smoker percentage: 20.68\
# Average insurance charges: 13406.38
# \
# \
# __Northwest Region__\
# Surveyed insurer population: 325\
# Average age of insurer: 39.32
# Surveryed male/female insurer: 161/164\
# Average BMI of insurer: 29.20\
# Average number of children: 1.15\
# Smoker percentage: 17.85\
# Average insurance charges: 12417.58
