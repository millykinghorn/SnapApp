import json
import matplotlib
#matplotlib.use('agg')
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime, timedelta

def analyse_snap_data_1(file):    
    data = json.loads(file)

    From_data = list()
    To_data = list()
    Date = list()
    
    #create dictionary of time and sender/reciever
    for block in data.values():
         for snap in block:    
             try:
                 temp = {"From": snap['From'], "Date":[snap['Created']]}
                 From_data.append(temp)
             except:
                 temp = {"To": snap['To'], "Date":[snap['Created']]}
                 To_data.append(temp)
    
    length = len(From_data)
    
    #Sort recieved data
    for i in range(length):
        try:
            temp=From_data[i]['From']
            j=i+1
            while(j<length):
                if From_data[j]['From'] == temp:
                    From_data[i]['Date']=From_data[i]['Date']+From_data[j]['Date']
                    From_data.pop(j)
                    length = length-1
                else:
                    j=j+1 
        except:
            break
                    
            
    #repeat for sent data
    length = len(To_data)
    for i in range(length): 
        try:
            temp=To_data[i]['To'] 
            j=i+1
            while(j<length):
                if To_data[j]['To'] == temp:
                    To_data[i]['Date']=To_data[i]['Date']+To_data[j]['Date']
                    To_data.pop(j)
                    length = length-1
                else:
                    j=j+1 
        except:
            break     
        
    #Find min and max dates
    min_date_list=list()
    max_date_list=list()
    for person in From_data:
        temp_min = min(person['Date'])
        temp_max = max(person['Date'])
        min_date_list.append(temp_min)
        max_date_list.append(temp_max)
    for person in To_data:
        temp_min = min(person['Date'])
        temp_max = max(person['Date'])
        min_date_list.append(temp_min)
        max_date_list.append(temp_max)
    min_date = min(min_date_list)
    max_date = max(max_date_list)
    min_day = min_date.split()[0]
    min_time = min_date.split()[1]
    max_day = max_date.split()[0]
    max_time = max_date.split()[1]
    time_zone = min_date.split()[2]
    
    #NOW TO GRAPH IT
    
    #First graph = histogram of recieved snapchats between dates
    names_from=[]
    snaps_from=[]
    names_to=[]
    snaps_to=[]
    
    for entry in From_data:
        names_from.append(entry['From'])
        snaps_from.append(len(entry['Date']))
        
    for entry in To_data:
        names_to.append(entry['To'])
        snaps_to.append(len(entry['Date']))
        
    
    Figure_1 = plt.figure(figsize=(len(names_from), 5)) 
    plt.bar(names_from,snaps_from, align = 'center', width = 0.3)
    plt.xticks(rotation=70)
    plt.title("Snapchats recieved between " + min_day + " and " + max_day)
    plt.show()
    return Figure_1




def analyse_snap_data_2(file):
    data = json.loads(file)

    From_data = list()
    To_data = list()
    Date = list()
    
    #create dictionary of time and sender/reciever
    for block in data.values():
         for snap in block:    
             try:
                 temp = {"From": snap['From'], "Date":[snap['Created']]}
                 From_data.append(temp)
             except:
                 temp = {"To": snap['To'], "Date":[snap['Created']]}
                 To_data.append(temp)
    
    length = len(From_data)
    
    #Sort recieved data
    for i in range(length):
        try:
            temp=From_data[i]['From']
            j=i+1
            while(j<length):
                if From_data[j]['From'] == temp:
                    From_data[i]['Date']=From_data[i]['Date']+From_data[j]['Date']
                    From_data.pop(j)
                    length = length-1
                else:
                    j=j+1 
        except:
            break
                    
    #repeat for sent data
    length = len(To_data)
    for i in range(length): 
        try:
            temp=To_data[i]['To'] 
            j=i+1
            while(j<length):
                if To_data[j]['To'] == temp:
                    To_data[i]['Date']=To_data[i]['Date']+To_data[j]['Date']
                    To_data.pop(j)
                    length = length-1
                else:
                    j=j+1 
        except:
            break     
        
    #Find min and max dates
    min_date_list=list()
    max_date_list=list()
    for person in From_data:
        temp_min = min(person['Date'])
        temp_max = max(person['Date'])
        min_date_list.append(temp_min)
        max_date_list.append(temp_max)
    for person in To_data:
        temp_min = min(person['Date'])
        temp_max = max(person['Date'])
        min_date_list.append(temp_min)
        max_date_list.append(temp_max)
    min_date = min(min_date_list)
    max_date = max(max_date_list)
    min_day = min_date.split()[0]
    min_time = min_date.split()[1]
    max_day = max_date.split()[0]
    max_time = max_date.split()[1]
    time_zone = min_date.split()[2]
    
       
    #First graph = histogram of recieved snapchats between dates
    names_from=[]
    snaps_from=[]
    names_to=[]
    snaps_to=[]
    
    for entry in From_data:
        names_from.append(entry['From'])
        snaps_from.append(len(entry['Date']))
        
    for entry in To_data:
        names_to.append(entry['To'])
        snaps_to.append(len(entry['Date']))
      

    #function for determining whether to display percentage or not
    def percent(num):
        if num<5:
            return None
        else:
            return '{p:.2f}% '.format(p=num,v=num)
            
    
    total_snaps = np.sum(snaps_from)
    sizes = (snaps_from/total_snaps)*100
    Figure_fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=None, 
            #autopct='%1.1f%%',
            autopct=percent,
            shadow=True, startangle=90)
    ax1.axis('equal')
    ax1.legend(names_from, title = "Friends", bbox_to_anchor =(1.5, 1))
    plt.show()
    return ax1
    


def analyse_snap_data_3(file):
    data = json.loads(file)

    From_data = list()
    To_data = list()
    Date = list()
    
    #create dictionary of time and sender/reciever
    for block in data.values():
         for snap in block:    
             try:
                 temp = {"From": snap['From'], "Date":[snap['Created']]}
                 From_data.append(temp)
             except:
                 temp = {"To": snap['To'], "Date":[snap['Created']]}
                 To_data.append(temp)
    
    length = len(From_data)
    
    #Sort recieved data
    for i in range(length):
        try:
            temp=From_data[i]['From']
            j=i+1
            while(j<length):
                if From_data[j]['From'] == temp:
                    From_data[i]['Date']=From_data[i]['Date']+From_data[j]['Date']
                    From_data.pop(j)
                    length = length-1
                else:
                    j=j+1 
        except:
            break
                    
            
    #repeat for sent data
    length = len(To_data)
    for i in range(length): 
        try:
            temp=To_data[i]['To'] 
            j=i+1
            while(j<length):
                if To_data[j]['To'] == temp:
                    To_data[i]['Date']=To_data[i]['Date']+To_data[j]['Date']
                    To_data.pop(j)
                    length = length-1
                else:
                    j=j+1 
        except:
            break     
        
    #Find min and max dates
    min_date_list=list()
    max_date_list=list()
    for person in From_data:
        temp_min = min(person['Date'])
        temp_max = max(person['Date'])
        min_date_list.append(temp_min)
        max_date_list.append(temp_max)
    for person in To_data:
        temp_min = min(person['Date'])
        temp_max = max(person['Date'])
        min_date_list.append(temp_min)
        max_date_list.append(temp_max)
    min_date = min(min_date_list)
    max_date = max(max_date_list)
    min_day = min_date.split()[0]
    min_time = min_date.split()[1]
    max_day = max_date.split()[0]
    max_time = max_date.split()[1]
    time_zone = min_date.split()[2]
    
   
    #First graph = histogram of recieved snapchats between dates
    names_from=[]
    snaps_from=[]
    names_to=[]
    snaps_to=[]
    
    for entry in From_data:
        names_from.append(entry['From'])
        snaps_from.append(len(entry['Date']))
        
    for entry in To_data:
        names_to.append(entry['To'])
        snaps_to.append(len(entry['Date']))
      
    
    #THIRD graph = histogram of recieved vs sent snapchats 
    
    Figure_3 = plt.figure(figsize = (len(names_to),5))
    recieved = plt.bar(names_from, snaps_from, align = 'center', width = 0.3, color = 'blue' )
    sent = plt.bar(names_to, snaps_to, align = 'edge', width = 0.3, color = 'red' )
    plt.xticks(rotation=70)
    #make a legend
    handles = (sent, recieved)
    labels = ('sent', 'recieved')
    plt.legend(handles, labels)
    plt.title("Snapchats sent and recieved between " + min_day + " and " + max_day)
    plt.show()
    
    return Figure_3

def analyse_snap_data_4(file):
    data = json.loads(file)

    From_data = list()
    To_data = list()
    Date = list()
    
    #create dictionary of time and sender/reciever
    for block in data.values():
         for snap in block:    
             try:
                 temp = {"From": snap['From'], "Date":[snap['Created']]}
                 From_data.append(temp)
             except:
                 temp = {"To": snap['To'], "Date":[snap['Created']]}
                 To_data.append(temp)
    
    length = len(From_data)
    
    #Sort recieved data
    for i in range(length):
        try:
            temp=From_data[i]['From']
            j=i+1
            while(j<length):
                if From_data[j]['From'] == temp:
                    From_data[i]['Date']=From_data[i]['Date']+From_data[j]['Date']
                    From_data.pop(j)
                    length = length-1
                else:
                    j=j+1 
        except:
            break
                    
            
    #repeat for sent data
    length = len(To_data)
    for i in range(length): 
        try:
            temp=To_data[i]['To'] 
            j=i+1
            while(j<length):
                if To_data[j]['To'] == temp:
                    To_data[i]['Date']=To_data[i]['Date']+To_data[j]['Date']
                    To_data.pop(j)
                    length = length-1
                else:
                    j=j+1 
        except:
            break     
        
    #Find min and max dates
    min_date_list=list()
    max_date_list=list()
    for person in From_data:
        temp_min = min(person['Date'])
        temp_max = max(person['Date'])
        min_date_list.append(temp_min)
        max_date_list.append(temp_max)
    for person in To_data:
        temp_min = min(person['Date'])
        temp_max = max(person['Date'])
        min_date_list.append(temp_min)
        max_date_list.append(temp_max)
    min_date = min(min_date_list)
    max_date = max(max_date_list)
    min_day = min_date.split()[0]
    min_time = min_date.split()[1]
    max_day = max_date.split()[0]
    max_time = max_date.split()[1]
    time_zone = min_date.split()[2]
    
   
    #First graph = histogram of recieved snapchats between dates
    names_from=[]
    snaps_from=[]
    names_to=[]
    snaps_to=[]
    
    for entry in From_data:
        names_from.append(entry['From'])
        snaps_from.append(len(entry['Date']))
        
    for entry in To_data:
        names_to.append(entry['To'])
        snaps_to.append(len(entry['Date']))
      
    #Fourth graph = snaps over time for top 5 snapsters (total sent and recieved)
    def datetime_range(start=None, end=None): # creates list of dates
        span = end - start
        for i in range(span.days + 1):
            yield start + timedelta(days=i)
            
    min_day_obj =datetime.strptime(min_day, "%Y-%m-%d")
    max_day_obj = datetime.strptime(max_day,"%Y-%m-%d")
    time_scale = datetime_range(start = min_day_obj, end = max_day_obj)
    time_scale_list = list(time_scale)
    
    #combine to and from data from each snapster
    all_data = To_data + From_data
    All_data = []
    for name in all_data: #to/from
        length = len(all_data)
        try:
            temp=name['To'] 
            new = {"Name": name['To'], "Date":name['Date']}
            All_data.append(new)
            
        except:
            temp=name['From']
            for i in All_data:
                if temp == i['Name']:
                    i['Date']=i['Date']+name['Date']
                
    #sort their data into the bins of 24 hour periods
    ex_plot = All_data[1]['Date']
    all_plots = list() #list of dates
    for x in range(len(All_data)):
        all_plots.append(All_data[x]['Date'])
    
    time_scale_array=np.array(time_scale_list)
    for item in time_scale_list:
        date_str = item.strftime("%Y-%m-%d %H:%M:%S")
        np.append(time_scale_array,date_str)
        
    Figure_4 = plt.figure(figsize = (12, 5))
    
    for n in range(len(all_plots)):    
        snaps_per_day = list()
        for x in range(len(time_scale_array)):
            snaps_per_day.append(0)
                
        for i in range(0,len(all_plots[n])):
            #convert to datetime object
            all_plots[n][i] = datetime.strptime(all_plots[n][i], "%Y-%m-%d %H:%M:%S %Z")
            
        #add to new list of number of snaps per day
        #go through data to be plotted and change each day to a counter which increases with each occurence
        for i in range(len(all_plots[n])):
            temp=all_plots[n][i].date() #date
            for j in range(len(time_scale_array)):
                if time_scale_array[j].date() == temp:
                    snaps_per_day[j] = snaps_per_day[j]+1
                        
        #plot as a line graph with different colours for each
        plt.plot(time_scale_array, snaps_per_day, label = All_data[n]['Name']) 
        
    plt.xticks(rotation=70)
    
    plt.legend()
    plt.title("Total snapchats between " + min_day + " and " + max_day)
    plt.show()
    
    return Figure_4

