# -*- coding: utf-8 -*-


def viterbi(obs, states, start_p, trans_p, emit_p):
    
    ### sets the network (#1 step)
    V = [{}]
    
    ### sets the first step in the netwrok for each inital state
    for st in states:
        V[0][st] = {"prob": start_p[st] * emit_p[st][obs[0]], "prev": None}
    
    # Run Viterbi when t > 0

    ### for each observation (exculding the first step)
    for t in range(1, len(obs)):
        
        ### add a step
        V.append({})
       

        for st in states:
            ### takes the highest trans prob for  each current state
            max_tr_prob = max(V[t - 1][prev_st]["prob"] * trans_p[prev_st][st]
                              for prev_st in states)

            for prev_st in states:

                ### takes the hgihest trans probs and calc its actual probs (inclusing trans prob) and adds it to V
                if V[t - 1][prev_st]["prob"] * trans_p[prev_st][st] == max_tr_prob:
                    max_prob = max_tr_prob * emit_p[st][obs[t]]
                    V[t][st] = {"prob": max_prob, "prev": prev_st}
                    break
    
    ### prints the network
    for line in dptable(V):
        print line



    opt = []
    # The highest probability
    ### bigest value end step
    max_prob = max(value["prob"] for value in V[-1].values())
    previous = None

    # Get most probable state and its backtrack
    ### 
    for st, data in V[-1].items():
        if data["prob"] == max_prob:
            opt.append(st)
            previous = st
            break
    # Follow the backtrack till the first observation
    for t in range(len(V) - 2, -1, -1):
        opt.insert(0, V[t + 1][previous]["prev"])
        previous = V[t + 1][previous]["prev"]

    print 'The steps of states are ' + ' '.join(
        opt) + ' with highest probability of %s' % max_prob


def dptable(V):
    # Print a table of steps from dictionary
    yield " ".join(("%9s" % i) for i in range(len(V)))
    for state in V[0]:
        yield "%.9s: " % state + " ".join("%.9s" % ("%.3E" % v[state]["prob"])
                                          for v in V)


states = 'abcdr'
observations = ('/a/', '/b/', '/r/', '/ã/', '/k/', '/a/', '/d/', '/d/', '/b/', '/r/', '/ã/')
start_probability = {'a': 0.4, 'b': 0.1, 'c': 0.1, 'd': 0.3, 'r': 0.1}

transition_probability = {'a': {'a': 0,
                                'b': 0.3,
                                'c': 0.3,
                                'd': 0.3,
                                'r': 0.1},
                          'b': {'a': 0.2,
                                'b': 0,
                                'c': 0.2,
                                'd': 0.1,
                                'r': 0.5},
                          'c': {'a': 0.5,
                                'b': 0.1,
                                'c': 0.1,
                                'd': 0.1,
                                'r': 0.1},
                          'd': {'a': 0.5,
                                'b': 0.2,
                                'c': 0.2,
                                'd': 0.0,
                                'r': 0.1},
                          'r': {'a': 0.7,
                                'b': 0.1,
                                'c': 0.1,
                                'd': 0.1,
                                'r': 0}}
emission_probability = {'a': {'/a/': 0.4,
                              '/ã/': 0.3,
                              '/b/': 0.05,
                              '/r/': 0.05,
                              '/d/': 0.15,
                              '/k/': 0.05},
                        'b': {'/a/': 0.05,
                              '/ã/': 0.05,
                              '/b/': 0.65,
                              '/r/': 0.05,
                              '/d/': 0.2,
                              '/k/': 0.05},
                        'c': {'/a/': 0.05,
                              '/ã/': 0.05,
                              '/b/': 0.05,
                              '/r/': 0.05,
                              '/d/': 0.05,
                              '/k/': 0.75},
                        'd': {'/a/': 0.05,
                              '/ã/': 0.05,
                              '/b/': 0.2,
                              '/r/': 0.05,
                              '/d/': 0.6,
                              '/k/': 0.05},
                        'r': {'/a/': 0.05,
                              '/ã/': 0.05,
                              '/b/': 0.05,
                              '/r/': 0.7,
                              '/d/': 0.05,
                              '/k/': 0.1}}

viterbi(observations, states, start_probability, transition_probability,
        emission_probability)




