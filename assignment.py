from requests import get
import argparse

parser = argparse.ArgumentParser(prog='assignment')
parser.add_argument('--match', help='display only information about time zones whose values match the string supplied to this argument')
parser.add_argument('--offset', help='the program will only display time zones matching this offset. Note that this should work for time zones ahead of and behind UTC!')
args = parser.parse_args()

def find_timezone():
    if args.offset:
        try:
            offset = int(args.offset)
            if not offset:
                print("please insert offset value ahead or behind the UTC")
                return 0 
        except:
            print("Invalid offset value. please insert valid int value for offset")
            return 0
    url = 'https://raw.githubusercontent.com/dmfilipenko/timezones.json/master/timezones.json'
    time_zone_data = get(url)
    for i in time_zone_data.json():
        if i["offset"] == args.offset or i["value"].find(args.match)==0:
            print(i)

if __name__ == '__main__':
    find_timezone()
