import sys

for line in sys.stdin:
    s = line.strip()
    events = s.split()

    RmAppAttempts = set()
    for e in events:
        RmAppAttempts.add(e.split('|')[1])
    
    Results = []
    RmAppAttemptStates = {raa: None for raa in RmAppAttempts}
    for e in events:
        src, obj, act = e.split('|')
        if RmAppAttemptStates[obj] in ('submitted', 'scheduled', 'allocated', 'running') and src == 'RmApp' and act == 'kill':
            RmAppAttemptStates[obj] = 'killed'
            Results.append('|'.join([obj, RmAppAttemptStates[obj]])+';')
        elif RmAppAttemptStates[obj] is None and src == 'RmApp' and act == 'start':
            RmAppAttemptStates[obj] = 'submitted'
            Results.append('|'.join([obj, RmAppAttemptStates[obj]])+';')
        elif RmAppAttemptStates[obj] is 'submitted' and src == 'ResourceScheduler' and act == 'app_accepted':
            RmAppAttemptStates[obj] = 'scheduled'
            Results.append('|'.join([obj, RmAppAttemptStates[obj]])+';')
        elif RmAppAttemptStates[obj] is 'scheduled' and src == 'RmContainer' and act == 'container_allocated':
            RmAppAttemptStates[obj] = 'allocated'
            Results.append('|'.join([obj, RmAppAttemptStates[obj]])+';')
        elif RmAppAttemptStates[obj] is 'scheduled' and src == 'ApplicationMasterLauncher' and act == 'launched':
            RmAppAttemptStates[obj] = 'running'
            Results.append('|'.join([obj, RmAppAttemptStates[obj]])+';')
        elif RmAppAttemptStates[obj] is 'running' and src == 'ResourceScheduler' and act == 'finished':
            RmAppAttemptStates[obj] = 'finished'
            Results.append('|'.join([obj, RmAppAttemptStates[obj]])+';')
    print(''.join(Results))
