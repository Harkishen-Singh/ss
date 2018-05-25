import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime

# from __future__ import print_function
pos = 0


class Core_Base:
    def __init__(self):
        self.temperature = 0
        self.city = ""
        self.state = ""
        self.pos_of_temp = 0
        self.pos2 = 0;
        self.min_temp = 0;
        self.max_temp = 0;
        self.avg_temp = 0.0
        self.max_rain_probability = 0.0;
        self.mix_rain_probability = 0.0;
        self.avg_rain = 0.0

    def asking(self,cityss,statess):
        self.stateSp = statess
        #self.city = input("City name : ")
        self.city = cityss.lower()
        #self.state = input("State name : ")
        self.state = statess.lower()
        self.country = "india"
        # url format design below
        self.format = "https://www.msn.com/en-in/weather/today/" + self.city + self.state + self.country + "/we-city?q=" + self.city + "-" + self.state + "&form=PRWLAS&iso=IN&el"
        self.extracting_info_from_net(self.format)
        self.place = cityss + ', '+statess

    def is_float(self, input):
        try:
            num = float(input)
        except ValueError:
            return False
        return True

    def is_int(self, input):
        try:
            num = int(input)
        except ValueError:
            return False
        return True

    def extracting_info_from_net(self, url):
        self.response = urlopen(url)
        self.source = self.response.read()
        self.source_text = BeautifulSoup(self.source)
        self.temp = self.source_text.text
        self.source_text = self.temp
        self.length_source_text = len(self.source_text)
        search_class = "Places"
        # print("search class = " + search_class)
        length_class = len(search_class)
        # print(self.source_text)
        c = 0
        for i in range(0, self.length_source_text - length_class):
            sub = self.source_text[i:i + length_class]
            if sub == search_class:
                # print('working')
                self.pos_of_temp = i + length_class

        # print("self.pos_of_temp : "+ str(self.pos_of_temp))
        # finding the first number after the statename
        for i in range(0, 30):
            if self.is_int(self.source_text[i + self.pos_of_temp]):
                self.pos2 = i + self.pos_of_temp
                break

        if self.source_text[self.pos2 + 1].isnumeric():
            # print("got it")
            self.temperature = int(self.source_text[self.pos2] + self.source_text[self.pos2 + 1])

        else:
            self.temperature = int(self.source_text[self.pos2])

    def further_info(self):
        # declaring and initializing

        self.feel = 0
        self.barometer = 0
        self.visibility = 0
        self.humidity = 0
        self.dew_point = 0
        l_feel = len("Feels")  # where all l_<feature> represents the length of various parameters
        l_barometer = len("Barometer")
        l_visibility = len("Visibility")
        l_humidity = len("Humidity")
        l_dew_point = len("Dew Point")
        count = self.pos2 + 2

        # working on these declared variables
        for i in range(count, count + 100):
            sub_1 = self.source_text[i:i + l_feel]
            sub_2 = self.source_text[i:i + l_barometer]
            sub_3 = self.source_text[i:i + l_visibility]
            sub_4 = self.source_text[i:i + l_humidity]
            sub_5 = self.source_text[i:i + l_dew_point]

            if sub_1 == "Feels":
                for j in range(0, 20):
                    if self.is_int(self.source_text[i + j]):
                        if self.source_text[i + j + 1].isnumeric():
                            self.feel = int(self.source_text[i + j] + self.source_text[i + j + 1])

                        else:
                            self.feel = int(self.source_text[i + j])
                        break

            '''if sub_2 == "Barometer":
                for j in range(0, 20):
                    if self.is_int(self.source_text[i + j]):
                        if self.source_text[i + j + 1].isnumeric() :
                            self.barometer = int(self.source_text[i + j] + self.source_text[i + j + 1])

                        else :
                            self.barometer = int(self.source_text[i + j])
                        break'''
            # for present, Barometer part is skipped.
            if sub_3 == "Visibility":
                for j in range(0, 20):
                    if self.is_int(self.source_text[i + j]):
                        if self.source_text[i + j + 1].isnumeric():
                            self.visibility = int(self.source_text[i + j] + self.source_text[i + j + 1])

                        else:
                            self.visibility = int(self.source_text[i + j])
                        break
            if sub_4 == "Humidity":
                for j in range(0, 20):
                    if self.is_int(self.source_text[i + j]):
                        if self.source_text[i + j + 1].isnumeric():
                            self.humidity = int(self.source_text[i + j] + self.source_text[i + j + 1])

                        else:
                            self.humidity = int(self.source_text[i + j])
                        break
            if sub_5 == "Dew Point":
                for j in range(0, 20):
                    if self.is_int(self.source_text[i + j]):
                        if self.source_text[i + j + 1].isnumeric():
                            self.dew_point = int(self.source_text[i + j] + self.source_text[i + j + 1])

                        else:
                            self.dew_point = int(self.source_text[i + j])
                        break

    def displaying(self):
        print('\n\n\nTime ' + str(datetime.datetime.now()))
        print("Temperature at that moment of " + self.city + " is : " + str(self.temperature))
        print("Feels Like :" + str(self.feel) + " C")
        print("Visibility :" + str(self.visibility) + " km")
        print("Humidity :" + str(self.humidity) + " %")
        print("Dew Point :" + str(self.dew_point) + " '")
        # print('\n\n'+self.source_text)
        self.splitting()

    def splitting(self):
        spilts = self.source_text
        tt = 'Hourly Forecast -'
        counter = 0
        pos = 0
        for i in range(0, len(self.source_text) - len(tt)):
            b = self.source_text[i: i + len(tt)]
            if b == tt:
                counter += 1
                pos = i + len(tt) + 19
        print('The counter of "Hourly Forecast -" is ' + str(counter))
        if counter == 1:
            #print(self.source_text[pos-3:pos+337])
            self.var = self.source_text[pos-3:pos + 337].split('\n\n\n')
            #print(self.var)
            print('\nHourly Forecast\n')
            for xx in self.var:
                xx.replace('\n', ' ')
            self.var.pop(len(self.var) - 1)
            self.var.pop(len(self.var) - 1)
            self.var.pop(len(self.var) - 1)
            print(self.var)
            self.other_general_information()
            self.temperature_and_rainfall_processing()
        else:
            print('\nHourly Forecast More than one available\n')
            exit(1)

    def other_general_information(self):

        #self.place = ''
        pos = 0
        self.day_checker = 'Places'
        for i in range(0, len(self.source_text) - len(self.day_checker)):
            word = self.source_text[i:len(self.day_checker)]
            if word == self.day_checker:
                pos = i + len(self.day_checker) + 1
                break
        rang = pos + 60
        placesArr = self.source_text[pos + 5: rang].split(' ')
        for p in range(0, len(placesArr) - 2):
            placesArr.pop(2)
        # print(placesArr)
        #self.place = placesArr[0] + ' ' + placesArr[1]
        print('\n' + self.place + '\n')

    def temperature_and_rainfall_processing(self):

        self.temps = []
        self.rains = []
        for i in self.var:
            j = i[2:]
            # print('J is '+j)
            num = ''
            num_rain = ''
            checker1 = False;
            checker2 = False;
            checker3 = False
            for x in j:
                if x.isdigit() and checker2 == False:
                    num += x
                    checker1 = True

                if x.isdigit() and checker2 == True:
                    num_rain += x
                    if len(num_rain) == 3:
                        break

                else:
                    checker2 = True

            # for rain calculations
            pos_percent = 0;
            got_percent = False
            for m in range(0, len(j)):
                if m == '%':
                    pos_percent = m
                    got_percent = True
                    break
            if got_percent == True:
                if j[m - 3].isdigit() :
                    num += j[m - 3]
                    print('third last from percent is digit')

                if j[m - 2].isdigit():
                    num += j[m - 2]
                    print('second last from percent is digit')
                if j[m - 1].isdigit():
                    num += j[m - 1]
                    print('last from percent is digit')

            num_rain = (num_rain[:-1])
            #print(num_rain)
            if num_rain.isdigit() :
                xx = float(num_rain)
            else:
                xx = num_rain
            #print('Rain is '+ num)
            # print('temp is '+ str(xx)) # mistakenly num_rain is the temperature scripted

            self.temps.append(xx)
            # print(i[8:10].replace('%',''))
            self.rains.append(float(i[8:10].replace('%', '')))

        print(self.rains)
        print(self.temps)

        self.continuing()

    def continuing(self):
        self.max_temp = self.temps[0];
        self.min_temp = self.temps[0]
        self.max_rain_probability = self.rains[0];
        self.min_rain_probability = self.rains[0]
        total_rains = 0;
        total_temp = 0
        for i in self.rains:
            if i > self.max_rain_probability:
                self.max_rain_probability = i
            if i < self.min_rain_probability:
                self.min_rain_probability = i
            total_rains += i
        self.avg_rain = total_rains / len(self.rains)
        for j in self.temps:
            if j > self.max_temp:
                self.max_temp = j
            if j < self.min_temp:
                self.min_temp = j
            total_temp += j
        self.avg_temp = total_temp / len(self.temps)

        print('\nMax rainfall ' + str(self.max_rain_probability) + '\t Max temp ' + str(self.max_temp))
        print('Min rainfall ' + str(self.min_rain_probability) + '\t Min temp ' + str(self.min_temp))
        print('Avg rainfall ' + str(self.avg_rain) + '\t Avg Temp ' + str(self.avg_temp))

'''
obj = Core_Base()
obj.asking()
obj.further_info()
obj.displaying()
'''