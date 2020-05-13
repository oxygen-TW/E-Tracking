from etracking import ECTracker, VerifyError, CodeNotFound
import pprint

ECTRACKER = ECTracker(autoVerify=True)

_id = input("交貨便ID...> ")
pp = pprint.PrettyPrinter(indent=4)

try:
    pp.pprint(ECTRACKER.tracker(_id))
except VerifyError as e:
    print(str(e))

except CodeNotFound as e:
    print(str(e))