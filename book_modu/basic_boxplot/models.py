import random

from book_modu.changed_temperatures_on_my_birthday.models import ChangedTemperaturesOnMyBirthday

import matplotlib.pyplot as plt


class BasicBoxplot(object):
    mybifthday = ChangedTemperaturesOnMyBirthday()

    def show_boxplot(self, month: str):
        mybifthday = self.mybifthday
        arr = mybifthday.highest_temperatures_my_birthday()
        plt.boxplot(arr)
        plt.show()

    def sorted_random_arr(self) -> []:
        arr = []
        [arr.append(random.randint(1, 1000)) for i in range(13)]
        return arr

    def show_boxplot_all_month(self):
        mybifthday = self.mybifthday
        arr = []
        [arr.append(mybifthday.highest_temperatures_my_birthday((str(i + 1)
                                                         if len(str(i+1)) == 2
                                                            else str('0'+str(i + 1)))))
                                                                for i in range(12)]
        plt.boxplot([i for i in arr])
        plt.show()


    def show_boxplot_per_date(self):
        arr = ChangedTemperaturesOnMyBirthday()
        arr.read_data()
        date = []
        [date.append([]) for i in range(31)]
        [date[int(i[0].split('-')[2])-1].append(float(i[-1])) for i in arr.data if i[-1] != '' if i[0].split('-')[1] == '08']
        plt.style.use('ggplot')
        plt.figure(figsize=(10, 5), dpi=300)
        plt.boxplot(date, showfliers=False)
        plt.show()