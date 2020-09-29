"""readphotfits.py - Adds SNIDs to SNANA photometry.

An example of using this function can be seen in savephotfits.py.

Authors: Dillon Brout, Ben Rose

Changelog:
- < 2020-09-29 - Dillon's initial
- 2020-09-29 - Ben update to python3 and astropy.io.fits
"""
import numpy as np
import os
from astropy.io import fits
import glob


def getphotdict(fitsdir,max=None):
    fitsdir = fitsdir.replace('@','*')
    headfiles = []
    photfiles = []
    for fall in glob.glob(fitsdir):
        fs = os.listdir(fall)
        for f in fs:
            if '_PHOT.FITS' in f:
                headfiles.append(fall+'/'+f.replace('PHOT','HEAD'))
                photfiles.append(fall+'/'+f)
    
    photdict = {}


    for headfile,photfile in zip(headfiles,photfiles):
        #headfile = fitsdir+'/'+prefix+'_HEAD.FITS'
        #photfile = fitsdir+'/'+prefix+'_PHOT.FITS'

        if not os.path.exists(headfile):
            os.system('gunzip '+headfile)
        if not os.path.exists(photfile):
            os.system('gunzip '+photfile)
                
    
        headdata = fits.open(headfile)[1].data
        for key in headdata.dtype.names:
            if not key in photdict.keys():
                photdict[key] = []
        if not 'FIELD' in photdict.keys():
            photdict['FIELD'] = []

        photdata = fits.open(photfile)[1].data
        snids = np.array(list(map(str.strip,headdata['SNID'])))
        tot = len(snids)
        if max is None:
            max = tot
        for i,snid in enumerate(snids[:max]):
        
            print('Reading in SNID:',snid,',',i,'of',tot)
            ww = (str(snid) == snids)

            arrstart = int(headdata['PTROBS_MIN'][ww][0])
            arrend = int(headdata['PTROBS_MAX'][ww][0])


            photdict[snid] = photdata[arrstart-1:arrend]
            for key in headdata.dtype.names:
                photdict[key].append(headdata[key][ww][0])
        
            photdict['FIELD'].append(photdata['FIELD'][arrstart])
            
        for key in photdict.keys():
            if not key in snids:
                if not key in photdict.keys():
                    photdict[key] = np.array(photdict[key])

    return photdict

#getphotdict(fakesphotdir)
