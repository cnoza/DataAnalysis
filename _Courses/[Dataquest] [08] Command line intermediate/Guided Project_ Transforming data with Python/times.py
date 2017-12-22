import read
from dateutil import parser

def get_hour(time):
    return parser.parse(time).hour

if __name__ == '__main__':
    df = read.load_data()
    print(df['submission_time'].apply(get_hour).value_counts().head())