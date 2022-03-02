"""
https://medium.com/jbennetcodes/how-to-rewrite-your-sql-queries-in-pandas-and-more-149d341fc53e
https://ourairports.com/data/
"""
import pandas as pd
import matplotlib.pyplot as plt


def main():
    airports = pd.read_csv('data/airports.csv')
    airport_freq = pd.read_csv('data/airport-frequencies.csv')
    runways = pd.read_csv('data/runways.csv')
    ##OK load_data()
    ##OK query1(airports)
    ##OK query2(airports)
    ##OK query3(airport_freq)
    ##OK query4(airports)
    ##OK query5(airports)
    ##NOTOK query6(airports)  # needs some work on type totals
    ##OK query7(runways)
    ##OK query8(airports,airport_freq)
    ##OK crud(airports)
    ##NOTOK plot_it(airports) # there is subtotal for type.


def query1(airports):
    print(airports)  # select * from airports
    print(airports.head(3))  # select * from airports limit 3
    print(airports[airports.ident == 'KLAX'].id)  # select id from airports where id = 'KLAX'
    print(airports.type.unique())  # select distinct type from airports


def query2(airports):
    """
    select with multiple conditions
    :param airports:
    :return:
    """

    '''
    select * from airports where iso_region = 'US-CA' and type = 'seaplane_base'
    '''
    print(airports[(airports.iso_region == 'US-CA') & (airports.type == 'seaplane_base')])

    '''
    select ident, name, municipality from airports where iso_region = 'US-CA' and type = 'large_airport'
    '''
    print(airports[(airports.iso_region == 'US-CA') & (airports.type == 'large_airport')][
              ['ident', 'name', 'municipality']])


def query3(airport_freq):
    """
    select with order by
    :param airports:
    :return:
    """

    '''
    select * from airport_freq where airport_ident = 'KLAX' order by type
    '''
    print(airport_freq[airport_freq.airport_ident == 'KLAX'].sort_values('type'))

    '''
    select * from airport_freq where airport_ident = 'KLAX' order by type desc
    '''
    print(airport_freq[airport_freq.airport_ident == 'KLAX'].sort_values('type', ascending=False))


def query4(airports):
    """
    select with in not in
    :return:
    """

    '''
    select * from airports where type in ('heliport', 'balloonport')
    '''
    print(airports[airports.type.isin(['heliport', 'balloonport'])])

    '''
    select * from airports where type not in ('heliport', 'balloonport')
    '''
    airports[~airports.type.isin(['heliport', 'balloonport'])]


def query5(airports):
    """
    select with group by, count, order by, having
    :param airports:
    :return:
    """

    '''
    select iso_country, type, count(*) from airports 
       group by iso_country, type order by iso_country, type
    '''
    print(airports.groupby(['iso_country', 'type']).size())

    '''
    select iso_country, type, count(*) from airports 
       group by iso_country, type order by iso_country, count(*) desc
    '''
    print(airports.groupby(['iso_country', 'type']).size().to_frame('size').reset_index().sort_values(['iso_country', 'size'],
        ascending=[True, False]))

    '''
    select iso_country, type, count(*) from airports group by iso_country, type order by iso_country, type
    '''
    print(airports.groupby(['iso_country', 'type']).size())

    '''
    airports.groupby(['iso_country', 'type']).size().to_frame('size').reset_index().sort_values(['iso_country', 'size'], 
        ascending=[True, False])
    '''
    print(airports.groupby(['iso_country', 'type']).size().to_frame('size').reset_index().sort_values(['iso_country', 'size'],
                                                                                                ascending=[True, False]))

    '''
    select type, count(*) from airports where iso_country = 'US' group by type having count(*) > 1000 order by count(*) desc
    '''
    print(airports[airports.iso_country == 'US'].groupby('type').filter(lambda g: len(g) > 1000).groupby('type').size().sort_values(ascending=False))


def query6(airports):
    """
    Top N records
    :param airports:
    :return:
    """

    by_country = airports.groupby(['iso_country', 'type']).size()
    print(by_country.head(3))

    '''
    select iso_country from by_country order by size desc limit 10;
    select iso_country from by_country order by size desc limit 10 offset 10;
    '''
    #print(by_country.nlargest(10, columns='airport_count'))
    #print(by_country.nlargest(20, columns='airport_count').tail(10))


def query7(runways):
    """
    Aggregate functions (min,max,mean)
    :param runways:
    :return:
    """

    '''
    select max(length_ft), min(length_ft), avg(length_ft), median(length_ft) from runways
    '''
    df = runways.agg({'length_ft': ['min', 'max', 'mean', 'median']})
    print(df)

    '''
    Transpose
    '''
    print(df.T)


def query8(airports,airport_freq):
    """
    join dataframes
    :param airport:
    :param airport_freq:
    :return:
    """

    '''
    select airport_ident, type, description, frequency_mhz 
        from airport_freq join airports 
          on airport_freq.airport_ref = airports.id 
       where airports.ident = 'KLAX'
    '''
    print(airport_freq.merge(airports[airports.ident == 'KLAX'][['id']], left_on='airport_ref', right_on='id', how='inner')[
        ['airport_ident', 'type', 'description', 'frequency_mhz']])


def query9(airports):
    """
    union all and union
    :param airports: 
    :return: 
    """

    '''
    select name, municipality from airports where ident = 'KLAX' 
        union all 
    select name, municipality from airports where ident = 'KLGB'
    '''
    print(pd.concat([airports[airports.ident == 'KLAX'][['name', 'municipality']],
               airports[airports.ident == 'KLGB'][['name', 'municipality']]]))

    '''
    To deduplicate things (equivalent of UNION), you’d also have to add .drop_duplicates().
    '''


def crud(airports):
    """
    insert, update, delete
    :return:
    """

    '''
    There’s no such thing as an INSERT in Pandas. Instead, you would create a new dataframe containing new records, and then concat the two:
    create table heroes (id integer, name text);
    insert into heroes values (1, 'Harry Potter');
    insert into heroes values (2, 'Ron Weasley');
    insert into heroes values (3, 'Hermione Granger');
    '''
    df1 = pd.DataFrame({'id': [1, 2], 'name': ['Harry Potter', 'Ron Weasley']})
    df2 = pd.DataFrame({'id': [3], 'name': ['Hermione Granger']})
    df3 = pd.concat([df1, df2]).reset_index(drop=True)
    print(df3)

    '''
    update airports set home_link = 'http://www.lawa.org/welcomelax.aspx' where ident == 'KLAX'
    '''
    airports.loc[airports['ident'] == 'KLAX', 'home_link'] = 'http://www.lawa.org/welcomelax.aspx'

    '''
    delete from lax_freq where type = 'MISC'
    '''
    data = []
    lax_freq = pd.DataFrame(data)
    lax_freq = lax_freq[lax_freq.type != 'MISC']
    lax_freq.drop(lax_freq[lax_freq.type == 'MISC'].index)
    lax_freq.reset_index(drop=True, inplace=True)
    print(lax_freq)

def load_data():
    airports = pd.read_csv('https://ourairports.com/data/airports.csv')
    airports.to_csv(r'data/airports.csv')
    airport_freq = pd.read_csv('https://ourairports.com/data/airport-frequencies.csv')
    airport_freq.to_csv(r'data/airport-frequencies.csv')
    runways = pd.read_csv('https://ourairports.com/data/runways.csv')
    runways.to_csv(r'data/runways.csv')
    countries = pd.read_csv('https://ourairports.com/data/countries.csv')
    countries.to_csv(r'data/countries.csv')


def export_to():
    """
    Several formats
    :return:
    """

    '''
    df.to_csv(...)  # csv file
    df.to_hdf(...)  # HDF5 file
    df.to_pickle(...)  # serialized object
    df.to_sql(...)  # to SQL database
    df.to_excel(...)  # to Excel sheet
    df.to_json(...)  # to JSON string
    df.to_html(...)  # render as HTML table
    df.to_feather(...)  # binary feather-format
    df.to_latex(...)  # tabular environment table
    df.to_stata(...)  # Stata binary data files
    df.to_msgpack(...)	# msgpack (serialize) object
    df.to_gbq(...)  # to a Google BigQuery table.
    df.to_string(...)  # console-friendly tabular output.
    df.to_clipboard(...) # clipboard that can be pasted into Excel
    '''


def plot_it(airports):
    plt =  airports.groupby(['iso_country', 'type']).size()
    print(plt)
    exit()
    plt.plot(
        x='iso_country',
        y='airport_count',
        kind='barh',
        figsize=(10, 7),
        title='Top 10 countries with most airports')

    plt.show()

if __name__ == '__main__':
    main()
