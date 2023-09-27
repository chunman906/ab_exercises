from q1_max_mfr import max_mfr
from max_mfr_combined import max_mfr_combined
from q2_top_average import top_average
from q3_good_bad_fe import good_bad_fe
from df_combined_year import *
from good_bad_fe_combined import good_bad_fe_combined

class Router:
    def __init__(self):
        self.running = True

    def run(self):
        self.logo()
        self.command_view()
        while self.running:
            choice = str(input('Please choose the option from the <main menu> above. Input the option number: '))
            if choice == '1':
                print('Please select the period for your choice. \n')
                print('<option 1>: Year 2015 figures \n<option 2>: Year 2015 to Year 2023 (9 years) figures \n')
                option = str(input('Input the option number: \n'))
                if option == '1':
                    max_mfr()
                elif option == '2':
                    max_mfr_combined()
                else:
                    print('You have input wrong number.')
            elif choice == '2':
                top_average()
            elif choice == '3':
                print('Please select the period for your choice. \n')
                print('<option 1>: Year 2015 figures \n<option 2>: Year 2015 to Year 2023 (9 years) figures \n')
                option = str(input('Input the option number: \n'))
                if option == '1':
                    good_bad_fe()
                elif option == '2':
                    good_bad_fe_combined(df_all_years)
                else:
                    print('You have input wrong number.')
            else:
                print('See you next time!')
                self.running = False



    def command_view(self):
        print('1. Find the car manufacturer which contains most quantity of car models. ')
        print('2. Find the top average fuel economy for the city and highway driving from the given dataset. ')
        print('3. Find good and bad average fuel economy cars from all transmission types. ')
        print('4. ')

    def logo(self):
        print('---------------------------------------------------------------------------------')
        print('')
        print('Welcome to explore the data analysis for the automobile research company.')
        print('')
        print('---------------------------------------------------------------------------------')


app = Router()
app.run()
