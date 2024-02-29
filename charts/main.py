from icecream import ic
from chart import get_data_of_csv, create_chart

def run():
    labels, values, dataframe = get_data_of_csv('assets/csv/world_population.csv', 'CCA3', 'World Population Percentage', ('Continent', 'South America'))
    create_chart(labels, values, 'South America Population Percentage', 'Countries', 'Population Percentage')
    ic(dataframe)
    
if __name__ == '__main__':
    run()