"""Zoonibit's response functionality.
"""
from astropy.vo.client import conesearch
from astropy.vo.client.vos_catalog import VOSError
from astropy.io import ascii
import numpy as np
import os
import csv

sdss_typedefs = {0: 'unknowns',
                 1: 'cosmic rays',
                 3: 'galaxies',
                 4: 'ghosts',
                 6: 'stars'}

def phid_to_coordinates(phid):
    """Converts a Planet Hunter light curve id to coordinates.
    """
    zoonibot_root = os.getenv("ZOOHOME")
    fname = zoonibot_root + '/zoonibot/_data/IDcoords.csv'
    with open(fname, 'rb') as csvfile:
        ph_identifiers = csv.reader(csvfile)
        for entry in ph_identifiers:
            if entry[0] == phid:
                return float(entry[1]),float(entry[2])
    return None

def myconesearch(ra, dec, sr, catname="SDSS DR8 - Sloan Digital Sky Survey Data Release 8 2"):
    try:
        response = conesearch.conesearch(ra, dec, sr, catalog_db=catname)
    except VOSError:
        return None
    return response.array    

def count_unique(keys):
    """Identifies unique values and counts their occurences."""
    uniq_keys = np.unique(keys)
    bins = uniq_keys.searchsorted(keys)
    return uniq_keys, np.bincount(bins)

def galaxyzoo_response(ra, dec, sr=0.01):
    """ZooniBot's response to a GZ user who spots 'weird things'.
    """
    data = myconesearch(ra, dec, sr)

    if data == None:
        return "There's nothing in this part of the sky."
    # Which object from SDSS' PhotoObjAll do we want to include?
    mask = ((data['mode'] == 1)
             & (data['i'] < 20))
    # Count number of object per type
    mytypes, mycounts = count_unique(data[mask]['type'].data)
    contents = []
    for i in np.argsort(mycounts)[::-1]:
        mytype = sdss_typedefs[mytypes[i]]
        mycount = mycounts[i]
        if mytype == 'galaxies' and mycount == 1:
            mytype = 'galaxy'
        contents.append("{0} {1}".format(mycount,
                                         mytype))
    # Parse Zoonibot's response
    response = "This region contains about "
    result = response+" and ".join(contents)+"."

    if np.any(data[mask]['i'] < 14):
        result += ' One of the stars is bright and has saturated the camera, which causes weird-looking artefacts.'
    return result

def planethunters_response(ra, dec):
    """ZooniBot's response to a transit candidate.
    """
    result = """Thanks for identifying a possible transit!  Be aware however, that transits are sometimes caused by the contamination of nearby stars.  For starters, please check [a cut-out image of the area near the star](http://surveys.roe.ac.uk:8080/wsa/GetImage?ra={0}&dec={1}&database=wserv4v20101019&frameType=stack&obsType=object&programmeID=10209&mode=show&archive=%20wsa&project=wserv4) for nearby neighbours. #zoonibotans""".format(ra, dec)
    
#result = "http://skyview.gsfc.nasa.gov/cgi-bin/images?Position=60,50&Survey=DSS2R&Return=JPG&Invert=True"

    return result
    
if __name__ == '__main__':
    # Example: http://talk.galaxyzoo.org/#/subjects/AGZ00045p8
    print galaxyzoo_response(102.840897955775, 39.1928898447807, 0.01)
