import pandas as pd
from sqlalchemy import create_engine

# read data from GitHub
url = 'https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/'
case_malaysia = pd.read_csv(url+'cases_malaysia.csv')
case_state = pd.read_csv(url+'cases_state.csv')
death_malaysia = pd.read_csv(url+'deaths_malaysia.csv')
death_state = pd.read_csv(url+'deaths_state.csv')



# MySQL database connection
# format(user:password@host:port/database)
engine = create_engine('mysql://doadmin:AVNS_5UnWLVRf7IthjnMd_kP@covid-malaysia-dashboard-do-user-13633772-0.b.db.ondigitalocean.com:25060/defaultdb?ssl-mode=REQUIRED')

# write DataFrame to MySQL database
# name - table name
case_malaysia.to_sql(name='case_malaysia', con=engine, if_exists='replace', index=False)
case_state.to_sql(name='case_state', con=engine, if_exists='replace', index=False)
death_malaysia.to_sql(name='death_malaysia', con=engine, if_exists='replace', index=False)
death_state.to_sql(name='death_state', con=engine, if_exists='replace', index=False)

# close the database connection
engine.dispose()
