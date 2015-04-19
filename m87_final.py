default("simobserve")                   # Reset params to default values
default("simanalyze")                   # ...for both tasks

overwrite          =  True              # clobber files
verbose            =  True              # talk to me

project            =  "m87_final_co32"             # name this simulation run (will be filename root)
configspec         =  'ALMA_1.0arcsec'  # lazy way to fix a filenaming issue - no quantitative effect

outfitsfile        =  "simulation_result.fits"

skymodel           =  "co32_m87_in.fits"
#modifymodel        = True
#indirection       =  "J2000 12h30m49.416 +12d23m28.09"
#inbright          =   "1.1mJy/pixel" # Rescale (leave blank for none)
incell             =  ""
incenter           =  "345.0GHz" # CO(2-1) @ M87's z
inwidth            =  '20MHz'
#innchan            =  0

setpointings       =  False           # don't make poingints for me, I'll specify them
ptgfile            =  "32mosaic.ptg"
integration        =  "600s"           # sampling time - correct one is ~10sec, but takes very long to process
totaltime          =  "10800s"         # total time on source (evenly divided among indiv. mosaic pointings)
direction          =  ''
mapsize            =  ['','']
maptype            = 'ALMA'

predict            =  True
complist           =  ""
refdate            =  '2014/03/30'
hourangle          =  'transit'                          # make M87 cross meridian @ obs. midpoint
antennalist        =  'ALMA;1.0arcsec'                   # Don't list a config, list desired resolution


# Add noise
thermalnoise       =  "tsys-atm"
user_pwv           =  0.5
t_ground           =  269.0
leakage            =  0.0

# Create fake obs. 
simobserve()

#project+'/'+project +'.'+ configuration + '.noisy.image'

vis                =  project +'.'+ configspec + '.noisy.ms'
modelimage         =  ''
#imsize             =  
#cell               =  '0.1arcsec'     #'0.1arcsec'
niter              =  1000
threshold          =  '0.001 mJy'
weighting          =  "briggs"
robust             = 0.5
outertaper         =  []
stokes             =  "I"

analyze            =  False        #  (If true, only first 6 selected outputs will be displayed)
showarray          =  False        #  like plotants
showuv             =  True         #  display uv coverage
showpsf            =  True         #  display synthesized (dirty) beam
showmodel          =  True         #  display sky model at original resolution
showconvolved      =  True         #  display sky model convolved with output beam
showclean          =  True         #  display the synthesized image
showresidual       =  True         #  display the clean residual image
showdifference     =  True         #  display difference image
showfidelity       =  True         #  display fidelity

graphics           = 'both'      # 'both' will make hardcopies while printing to screen

# Analyze fake obs. 
simanalyze()

#Export the image and lets look at it
getsimout         =  project+'/'+project +'.'+ configspec + '.noisy.image'
exportfits(imagename=getsimout,fitsimage=outfitsfile,overwrite=True)
viewer(infile=getsimout)


