from prop_hist import prop_hist

lines  = ['pcc_12', 'pcc_13']
vals   = ['mvir', 'vrms_k', 'mlumco', 'sigvir', 'alpha', 'mlte', 'siglte', 'siglum']

### automated outputs
for l in lines:
    for v in vals:
        prop_hist(label = l, val = v)

### original runs, specified bounds
#prop_hist(label = 'pcc_12', val = 'mvir'  , lims = [0, 4], bin_size = .25)
#prop_hist(label = 'pcc_12', val = 'mvir')
#prop_hist(label = 'pcc_12', val = 'vrms_k', lims = [-1.20, .15], bin_size = .01)
#prop_hist(label = 'pcc_12', val = 'vrms_k')    # most accurate, i believe
#prop_hist(label = 'pcc_12', val = 'mlumco', lims = [0, 3.75], bin_size = .25)
#prop_hist(label = 'pcc_12', val = 'sigvir', lims = [0, 2.5], bin_size = .125)
#prop_hist(label = 'pcc_12', val = 'alpha' , lims = [0, 1.5], bin_size = .1)
#prop_hist(label = 'pcc_12', val = 'mlte'  , lims = [0, 4], bin_size = .25)
#prop_hist(label = 'pcc_13', val = 'mvir'  , lims = [.5, 3], bin_size = .125)
#prop_hist(label = 'pcc_13', val = 'vrms_k', lims = [0, .5], bin_size = .02)
#prop_hist(label = 'pcc_13', val = 'mlumco', lims = [0, 2], bin_size = .1)
#prop_hist(label = 'pcc_13', val = 'sigvir', lims = [.85, 2.1], bin_size = .0625)
#prop_hist(label = 'pcc_13', val = 'alpha' , lims = [.5, 1.7], bin_size = .08)
#prop_hist(label = 'pcc_13', val = 'mlte'  , lims = [1.5, 3.75], bin_size = .125)



