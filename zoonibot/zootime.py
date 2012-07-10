import datetime

# At APW's request, tried to do this without the pytz package so am
# using only Python standard library stuff.

class ZooST(datetime.tzinfo):
    """Defines the standard time of the Zooniverse server (currently
    EST).
    """

    # NB: datetime.tzinfo is an abstract base class.  To convert
    # timezones, the function datetime.astimezone() is called by other
    # basic datetime functions behind the scenes.  The astimezone()
    # function (read the python documentation) takes a tzinfo instance
    # as an argument and requires that the tzinfo instance implement
    # two methods: utcoffset() and dst().  Read the
    # datetime.astimezone() documentation for the explanation about
    # the argument structure of these methods and what they should
    # return.

    def utcoffset(self, dt):
        # Zooniverse server lives in Eastern time zone (UTC - 5)
        return datetime.timedelta(hours=-5)

    def dst(self, dt):
        # TODO: no daylight savings right now.  Should find a way to
        # incorporate this correctly.
        return datetime.timedelta(0)


def zoo_yesterday():
    """
    Returns yesterday's date (as measured at the Zooniverse server) as
    a string in format "yyyy-mm-dd".

    TODO: Should generalize the function to take kwargs and return any
    amount of time before today as measured at the server.  Then maybe
    rename this zootime().
    """

    # Define a one day time interval
    one_day = datetime.timedelta(days=1)

    zoonow = datetime.datetime.now(ZooST())
    zooyest = zoonow - one_day

    return str(zooyest.date())

