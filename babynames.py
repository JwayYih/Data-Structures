# Identify the 100 most common male and female baby names from 1880 through 2016weakness_lists = {}    
import json
import operator
f = open('output.json', 'w')

boy_list={}
girl_list={}

year=1880

while year < 2017:
    with open('babies/yob'+str(year)+'.txt') as f:
        for line in f:
            fields = line.split(',')
            name = fields[0]
            gender= fields[1]
            count = int(fields[2])        
            if gender == 'M':
                if name in boy_list:
                    boy_list[name]=boy_list[name]+count
                else:
                    boy_list.update({name : count})
            else:
                if name in girl_list:
                    girl_list[name]=girl_list[name]+count
                else:
                    girl_list.update({name : count})                
        year=year+1

#Sorts in descending popularity
boy_list_sorted_desc=sorted(boy_list.items(), key=operator.itemgetter(1),reverse=True)
girl_list_sorted_desc=sorted(girl_list.items(), key=operator.itemgetter(1),reverse=True)

#Trims to top list
boy_list_top100=boy_list_sorted_desc[:100]
#print(boy_list_top100)
girl_list_top100=girl_list_sorted_desc[:100]
#print(girl_list_top100)
 
final_popularnames = {"male":boy_list_top100, "female":girl_list_top100}

with open('popularnames.json', 'w') as f_out:    
    json.dump(final_popularnames, f_out)
    
print(final_popularnames)
