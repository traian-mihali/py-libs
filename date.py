from datetime import datetime
from time import time

dt = datetime(2019, 1, 1)
dt1 = datetime.now()
dt = datetime.strptime("2019/01/01", "%Y/%m/%d")

dt = datetime.fromtimestamp(time())
print(f"{dt.year}/{dt.month}")

print(dt.strftime("%Y/%m/%d"))

print(dt > dt1)
