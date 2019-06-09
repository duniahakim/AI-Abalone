# With initial weights:
def getBlackWeights():
    w = {}
    w['num_black_Off_grid'] = -10
    w['num_white_Off_grid'] = 12
    w['num_black_on_edge'] = -1
    w['num_white_on_edge'] = 2
    w['black_average_pos'] = -1
    w['white_average_pos'] = 2
    w['black_coherence'] = 2
    w['white_coherence'] = -1
    w['black_break'] = 2
    w['white_break'] = 0
    return w

def getWhiteWeights():
    w = {}
    w['num_black_Off_grid'] = 12
    w['num_white_Off_grid'] = -10
    w['num_black_on_edge'] = 2
    w['num_white_on_edge'] = -1
    w['black_average_pos'] = 2
    w['white_average_pos'] = -1
    w['black_coherence'] = -1
    w['white_coherence'] = 2
    w['black_break'] = 0
    w['white_break'] = 2
    return w

# eta = 0.01, gamma = 0.2, black side, 100 iteration
w = {'num_black_Off_grid': -10.0, 'num_white_Off_grid': 12.0, 'num_black_on_edge': 0.30318448519043223, 'num_white_on_edge': -0.31274758422605664, 'black_average_pos': -0.7970888100306505, 'white_average_pos': 0.757907389195527, 'black_coherence': 0.5772122672283362, 'white_coherence': -0.4091975433900944, 'black_break': 1.0611657699106711, 'white_break': -0.9388342300893435}

# eta = 0.01, gamma = 0.2, white side, 100 iteration
w = {'num_black_Off_grid': -4.675391879266451, 'num_white_Off_grid': -9.908359414916804, 'num_black_on_edge': 1.5621919929982317, 'num_white_on_edge': -2.893937238564445, 'black_average_pos': -2.8753560719300104, 'white_average_pos': 1.1275938408324637, 'black_coherence': 3.901718387833519, 'white_coherence': 0.505289860426182, 'black_break': -1.500114656033892, 'white_break': 2.276846733938931}


# eta = 0.001, gamma = 0.2, black side, 100 iteration
w = {'num_black_Off_grid': -10.0, 'num_white_Off_grid': 12.0, 'num_black_on_edge': -1.4220548966813016, 'num_white_on_edge': 1.0906714795992967, 'black_average_pos': -1.4156226804858798, 'white_average_pos': 1.3894678700263614, 'black_coherence': 1.7941345394011496, 'white_coherence': -0.8928301228450835, 'black_break': 1.849963784226139, 'white_break': -0.15003621577402654}


# eta = 0.001, gamma = 0.2, white side, 100 iteration
w = {'num_black_Off_grid': 4.064473652825573, 'num_white_Off_grid': -9.680834562323339, 'num_black_on_edge': -2.0583450359162354, 'num_white_on_edge': -0.4065981325795769, 'black_average_pos': -5.531513535858458, 'white_average_pos': -1.8560605418747451, 'black_coherence': 7.848915341521202, 'white_coherence': 1.4670132679335386, 'black_break': -3.0592234951019552, 'white_break': 0.10543878982155203}


# eta = 0.0001, gamma = 0.2, black side, 100 iteration
w = {'num_black_Off_grid': -10.0, 'num_white_Off_grid': 12.0, 'num_black_on_edge': -1.6237421109537182, 'num_white_on_edge': 1.3226838016288591, 'black_average_pos': -1.5041972408381528, 'white_average_pos': 1.4743731241948772, 'black_coherence': 1.8482482136464093, 'white_coherence': -1.1167225393067912, 'black_break': 1.9349357508492813, 'white_break': -0.0650642491507218}


# eta = 0.0001, gamma = 0.2, white side, 100 iteration
w = {'num_black_Off_grid': 11.622712460338024, 'num_white_Off_grid': -9.476337597924067, 'num_black_on_edge': 1.3089819093532071, 'num_white_on_edge': -0.18712317451057772, 'black_average_pos': 2.0062569948903897, 'white_average_pos': -0.061458291448646035, 'black_coherence': -0.006068921392942536, 'white_coherence': 1.85159872562587, 'black_break': 0.5038203759354308, 'white_break': 2.7659631373543543}


# eta = 0.00001, gamma = 0.2, black side, 100 iteration
w = {'num_black_Off_grid': -10.0, 'num_white_Off_grid': 12.0, 'num_black_on_edge': -1.6427445522089623, 'num_white_on_edge': 1.3521981691435976, 'black_average_pos': -1.5149370357930996, 'white_average_pos': 1.4830400527479268, 'black_coherence': 1.8448162633876133, 'white_coherence': -1.151930735565754, 'black_break': 1.947373237031491, 'white_break': -0.05262676296852011}


# eta = 0.00001, gamma = 0.2, white side, 100 iteration
w = {'num_black_Off_grid': 12.0, 'num_white_Off_grid': -9.842586031190512, 'num_black_on_edge': 2.0243706055408963, 'num_white_on_edge': -0.670657024651636, 'black_average_pos': 2.2481484545782187, 'white_average_pos': -0.5295828680269841, 'black_coherence': -0.5944043604580814, 'white_coherence': 2.147822452997462, 'black_break': 0.18939778431453905, 'white_break': 2.2352921333749975}




# For eta = 0.01, gamma = 0.2, black side, 1 iteration
# w['num_black_Off_grid'] = 100
#   w['num_white_Off_grid'] = -100
#   w['num_black_on_edge'] = 100
#   w['num_white_on_edge'] = -100
#   w['black_average_pos'] = 100
#   w['white_average_pos'] = -100
#   w['black_coherence'] = -100
#   w['white_coherence'] = 100
#   w['black_break'] = -100
#   w['white_break'] = 100
w = {'num_white_Off_grid': 12.619348456190396, 'num_white_on_edge': 3.1488994429705066, 'black_break': 2.857962452598955, 'num_black_Off_grid': -10.0, 'black_coherence': 2.8637717236477016, 'white_coherence': -0.4740966727316621, 'white_break': 1.042129028946902, 'white_average_pos': 3.918577000282171, 'num_black_on_edge': 0.33348825286889183, 'black_average_pos': 0.5794191606665251}


# For eta = 0.001, gamma = 0.2 and black side, 1 iteration
# w['num_black_Off_grid'] = 100
#   w['num_white_Off_grid'] = -100
#   w['num_black_on_edge'] = 100
#   w['num_white_on_edge'] = -100
#   w['black_average_pos'] = 100
#   w['white_average_pos'] = -100
#   w['black_coherence'] = -100
#   w['white_coherence'] = 100
#   w['black_break'] = -100
#   w['white_break'] = 100

w = {'num_black_Off_grid': -10.0, 'num_white_Off_grid': 12.056096796842606, 'num_black_on_edge': -1.0080698486776856, 'num_white_on_edge': 2.0904219653014957, 'black_average_pos': -0.9177340829897825, 'white_average_pos': 2.1572019380167227, 'black_coherence': 2.1540516790798963, 'white_coherence': -0.9654831755106922, 'black_break': 2.0763207329497124, 'white_break': 0.09334653603949986}

# For eta = 0.001, gamma = 0.2 and white side, 1 iteration
# w['num_black_Off_grid'] = 12
# w['num_white_Off_grid'] = -10
# w['num_black_on_edge'] = 2
# w['num_white_on_edge'] = -1
# w['black_average_pos'] = 2
# w['white_average_pos'] = -1
# w['black_coherence'] = -1
# w['white_coherence'] = 2
# w['black_break'] = 0
# w['white_break'] = 2

w = {'num_black_Off_grid': 12.0, 'num_white_Off_grid': -9.838700530701312, 'num_black_on_edge': 2.0422668564407758, 'num_white_on_edge': -0.6614323172236901, 'black_average_pos': 2.272661061466584, 'white_average_pos': -0.5059960126085488, 'black_coherence': -0.5666191005121458, 'white_coherence': 2.1590475367578774, 'black_break': 0.19654327711591962, 'white_break': 2.243561057001353}
