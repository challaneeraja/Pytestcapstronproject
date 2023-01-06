import pytest
import datetime
import pytz
@pytest.mark.fixture(autouse=True)
def getdatetime():
    print(datetime.datetime.now(pytz.timezone('Asi/Kolkata')))