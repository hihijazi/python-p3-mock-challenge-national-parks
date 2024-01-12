class NationalPark:
    all = []
    def __init__(self, name):
        if type(name) is str and 3<=len(name):
            self._name = name
            NationalPark.all.append(self)
        else:
            print("Not valid name")
        
    def trips(self):
        return_list = []
        for trip_instance in Trip.all:
            if trip_instance.national_park is self:
                return_list.append(trip_instance)
        return return_list
                
    
    def visitors(self):
        return_list = []
        for visited_park in self.trips():
            return_list.append(visited_park.visitor)
        return list(set(return_list))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visits_per_person = {}
        for trip in self.trips():
            if visits_per_person.get(trip.visitor):
                visits_per_person[trip.visitor] +=1
            else:
                visits_per_person[trip.visitor] = 1
        cur_best_count = 0
        cur_best_visitor = None
        for visitor in visits_per_person:
            if visits_per_person[visitor] > cur_best_count:
                cur_best_count = visits_per_person[visitor]
                cur_best_visitor = visitor
        return cur_best_visitor

    def get_name(self):
        return self._name
    def set_name(self,value):
        print("Cannot Change")
        # isinstance(value,str)
        # if type(value) is str and 3<=len(value) and not hasattr(self,"name"):
        #     self._name = value
        # else:
        #     print("Cannot change")
    name = property(get_name,set_name)

    #Bonus class method
    @classmethod 
    def most_visited(cls):
        # Keep track of the current park and its visit count
        curr_most = 0
        curr_park = None
        # Loop through all the parks
        for national_park in NationalPark.all:
            #calculate that parks visit count
            count = national_park.total_visits()
            # Check if that count is bigger then the current most
            # If it is then set the current most and the current
            # biggest park to this park we currently are looking at
            if count > curr_most:
                curr_most = count
                curr_park = national_park
        return curr_park

    def __repr__(self):
        return self.name
    


class Trip:
    all = []
    months = ("January", "February","March","May","September")
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    def get_start_date(self):
        return self._start_date
    def set_start_date(self,value):
        if type(value) is str and 7<=len(value):
            split = value.split()
            if split[0] in Trip.months and 3<=len(split[1])<=4:
                self._start_date = value
            else:
                print("Not valid date format")
        else:
            print("Not valid date")
    start_date = property(get_start_date,set_start_date)

    def get_end_date(self):
        return self._end_date
    def set_end_date(self,value):
        if type(value) is str and 7<=len(value):
            split = value.split()
            if split[0] in Trip.months and 3<=len(split[1])<=4:
                self._end_date = value
            else:
                print("Not valid date format")
        else:
            print("Not valid date")
    end_date = property(get_end_date,set_end_date)
    
    def get_visitor(self):
        return self._visitor
    def set_visitor(self,value):
        if type(value) is Visitor:
            self._visitor = value
        else:
            print("Not valid visitor")
    visitor = property(get_visitor, set_visitor)

    def get_national_park(self):
        return self._national_park
    def set_national_park(self,value):
        if type(value) is NationalPark:
            self._national_park = value
        else:
            print("Not valid national park")
    national_park = property(get_national_park, set_national_park)
    
    def __repr__(self):
        return f"{self.visitor.name} visited {self.national_park.name}"
    


class Visitor:

    def __init__(self, name):
        self.name = name
        
    def trips(self):
        return_list = []
        for trip_instance in Trip.all:
            if trip_instance.visitor is self:
                return_list.append(trip_instance)
        return return_list

    
    def national_parks(self):
        rlist = []
        for my_trip in self.trips():
            if my_trip.national_park not in rlist:
                rlist.append(my_trip.national_park)
        return rlist
    
    def total_visits_at_park(self, park):
        count = 0
        for trip in self.trips():
            if trip.national_park is park:
                count+=1
        return count

    def get_name(self):
        return self._name
    def set_name(self,value):
        # isinstance(value,str)
        if type(value) is str and 1<=len(value)<=15:
            self._name = value
        else:
            print("Not valid name")
    name = property(get_name,set_name)


v1 = Visitor("Jack")
v2 = Visitor("Cal")
np1 = NationalPark("Yellowstone")
np2 = NationalPark("Rocky Mountains")

Trip(v1,np1, 1, "September 2nd")
Trip(v1,np2, "September 1st", "September 2nd")
Trip(v1,np1, "September 1st", "September 2nd")
Trip(v2,np1, "September 1st", "September 2nd")
Trip(v2,np2, "September 1st", "September 2nd")
# print(np1.visitors())
# print(v1.national_parks())
# print(np1.total_visits())
# print(np2.total_visits())
print(np1.best_visitor().name)
print(v1.total_visits_at_park(np2))
# np.name = "Nellowstone"
# print(type(np))

# Trip(v1,np,"September 1st", "September 2nd")
# obj = {
#     "a":1,
#     "b":2
# }
# test = "a"
# obj[]