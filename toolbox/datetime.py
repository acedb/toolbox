'''Functions dealing with datetime types'''

def round_six_hours(period):
  '''Round datetime to closest 6h unit.

  Period should be a df column which is already in datetime format.
  '''
  if period.hour < 6:
      period = period.replace(hour = 0)

  elif period.hour < 12 :
      period = period.replace(hour = 6)

  elif period.hour < 18 :
      period = period.replace(hour = 12)

  else:
      period = period.replace(hour = 18)

  return period


def to_date_format(dataframe):
  ''' Keep only complete years and create datetime column.

  Create new column 'period' out of columns 'date' and 'time'.
  Drop columns 'date' and 'time'.
  Filter dataframe to show only complaints dated >= 2007.

  N.B. NEEDS TO BE ADAPTED TO NEW USE!
  '''
  df = dataframe.copy()

  # New period column out of concatenated 'date' and 'time'
  df['period'] = df['date'] + ' ' + df['time']

  # Converts 'period' to datetime format
  df['period'] = df['period'].apply(lambda x: \
                        datetime.strptime(x, '%m/%d/%Y %H:%M:%S'))

  # Trims 'period' to hour
  df['period'] = df['period'].apply(lambda x: \
                        x.replace(minute = 0, second = 0))

  # Filters dataframe to exclude crimes older than 2007
  df = df[df['period'] > datetime(2006, 12, 31, 23, 59, 0)]

  # Drops columns 'date' and 'time'
  df.drop(columns = ['date', 'time'], inplace = True)

  return df
