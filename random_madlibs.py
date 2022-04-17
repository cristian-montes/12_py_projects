from sample_madlibs import zoombie, code
import random

if __name__ == "__main__":
    mad = random.choice([zoombie, code])
    mad.madlib()