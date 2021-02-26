class street:
  def __init__(self, start_intersection,end_intersection,street_name,street_duration):
    self.start_intersection = start_intersection
    self.end_intersection = end_intersection
    self.street_name = street_name
    self.street_duration = street_duration

class car:
  def __init__(self, number_of_streets,street_names):
    self.number_of_streets = number_of_streets
    self.street_names = street_names


class schedule_per_intersection:
  def __init__(self, intersection_id,no_incoming_streets,schedule_per_street):
    self.intersection_id = intersection_id
    self.no_incoming_streets = no_incoming_streets
    self.schedule_per_street = schedule_per_street



def read_data(file_name):
    f = open(file_name, "r")
    lines=[]
    for each_line in f:
        each_line = each_line.replace('\n','')
        lines.append(each_line.split(' '))
    D=int(lines[0][0])
    I=int(lines[0][1])
    S=int(lines[0][2])
    V=int(lines[0][3])
    F=int(lines[0][4])
    streets = []
    cars=[]
    for each_street in range(1,S+1,1):    
        streets.append(street(lines[each_street][0],lines[each_street][1],lines[each_street][2],lines[each_street][3]))
    for each_car in range(S+1,S+V+1,1):    
        cars.append(car(lines[each_car][0],lines[each_car][1:]))
    return streets,cars,D,I,S,V,F

def write_data(result_schedules,i):
    f = open('result_'+i, "a")
    f.write(str(len(result_schedules))+'\n')
    for each_intersection in range(len(result_schedules)):
        f.write(str(result_schedules[each_intersection].intersection_id)+'\n')
        f.write(str(result_schedules[each_intersection].no_incoming_streets)+'\n')
        for each_schedule in result_schedules[each_intersection].schedule_per_street:
            f.write(each_schedule[0]+" "+str(each_schedule[1])+'\n')

def calc_schedules(streets,cars,D,I,S,V,F):
    result_schedules = []
    incoming_streets_count = {}
    incoming_car_count = {}
    incoming_streets_intersection={}
    schedule={}
    # For incoming streets calculation
    # initially assuming no incoming streets
    for i in range(I):
        incoming_streets_count[i]=0
        incoming_streets_intersection[i]=[]
        schedule[i]=[]
    for j in range(len(streets)):
        incoming_streets_count[int(streets[j].end_intersection)]+=1
        incoming_streets_intersection[int(streets[j].end_intersection)].append(streets[j].street_name)
        incoming_car_count[streets[j].street_name]=0
        
    for k in range(len(cars)):
        for l in range(len(cars[k].street_names)):
            if(l!=0):
                incoming_car_count[cars[k].street_names[l]]+=1
    for t in range(I):
        for m in range(len(incoming_streets_intersection[t])):
            # schedule[t].append([incoming_streets_intersection[t][m],((incoming_car_count[incoming_streets_intersection[t][m]])/len(cars))])
            schedule[t].append([incoming_streets_intersection[t][m],1])
    for i in range(I):
        I=schedule_per_intersection(i,incoming_streets_count[i],schedule[i])
        result_schedules.append(I)
    return result_schedules

def main():
    # Taking the inputs
    for i in ['a.txt', 'b.txt', 'c.txt','d.txt','e.txt','f.txt']:
        streets,cars,D,I,S,V,F = read_data(i)

        # Assigning schedules
        result_schedules = calc_schedules(streets,cars,D,I,S,V,F)
        
        # Writing the result
        write_data(result_schedules,i)
     
if __name__ == "__main__":
    main()
    
    