# --------------
import json

data=json.load(open(path,'r'))
print(type(data['innings'][0]['1st innings']['deliveries']))
#print(data)
lstinnings=data['innings'][0]['1st innings']['deliveries']
#print(lstinnings)
#print([d.values() for d in lstinnings ])
dictdeliveries=[d for d in lstinnings ]
def get_batsman_deliveries():
    lstinnings=data['innings'][0]['1st innings']['deliveries']
    for lstdelivery in lstinnings:
        valdel=(lstdelivery.values())
        for deldata in valdel:
            return list([deldata['batsman'] for cnt in deldata if deldata['batsman']=='SC Ganguly'])
print('Total deliveries for SC Ganguly is ' + str(len(get_batsman_deliveries())))
#print(data['innings'][1])e
print('Man of the match ' + str(data['info']['player_of_match']))

def gettotal_runs(batsmman):
    
    lstinnings=data['innings'][0]['1st innings']['deliveries']
    total_run=0;
    for lstdelivery in lstinnings:
        valdel=(lstdelivery.values())
        for deldata in valdel:
             if(deldata['batsman']==batsmman):
                  total_run+=int(deldata['runs']['total'])
    return total_run       
        
print('Total run of BB McCullum is '+ str(list(map(gettotal_runs,list(data['info']['player_of_match'])))))

def first_innings_data():
    firstinningsbats=[]
    lstinnings=data['innings'][0]['1st innings']['deliveries']
    for lstdelivery in lstinnings:
        valdel=(lstdelivery.values())
        for deldata in valdel:
            if deldata['batsman'] not in firstinningsbats:
                firstinningsbats.append(deldata['batsman'])
                
    return firstinningsbats


print('Played batsman in first innings -' + str(first_innings_data()))
def getbatsman_bymaxruns(batsmman):
    lstinnings=data['innings'][0]['1st innings']['deliveries']
    max_run=0
    for lstdelivery in lstinnings:
        valdel=(lstdelivery.values())
        for deldata in valdel:
             if(batsmman in deldata['batsman']):
                    if (int(deldata['runs']['batsman']) == 6):
                        max_run+=int(deldata['runs']['batsman'])
                        
    return max_run  
totalrunsofbatsman=list(filter(getbatsman_bymaxruns,first_innings_data()))
print('Most 6s batsman is '+ str(totalrunsofbatsman[1]))

secondinnings=data['innings'][1]['2nd innings']['deliveries']
#print(secondinnings)
def getBowledOutPlayers():
    lstbowledout_players=[]
    secondinnings=data['innings'][1]['2nd innings']['deliveries']
    for scnddelivery in secondinnings:
        valdel=scnddelivery.values()
        for deldata in valdel:
            for batsman_out in deldata.items():
               lstbowledout_players.append([  b for b in batsman_out[1:] if('kind' in b) if str(b['kind'])=='bowled' ])
    return filter(None,lstbowledout_players)  

lstplayersout=tuple(getBowledOutPlayers())
lstplayersout=  [item[-1] for item in lstplayersout]
print('Names of players out by bowler are ' +str( [item['player_out'] for item in lstplayersout]))

def getFirstInnExtras(batsmman):
    lstinnings=data['innings'][0]['1st innings']['deliveries']
    total_run=0;
    for lstdelivery in lstinnings:
        valdel=(lstdelivery.values())
        for deldata in valdel:
             if(deldata['batsman']==batsmman):
                    total_run+=int(deldata['runs']['extras'])
    return total_run  

def second_innings_data():
    firstinningsbats=[]
    lstinnings=data['innings'][1]['2nd innings']['deliveries']
    for lstdelivery in lstinnings:
        valdel=(lstdelivery.values())
        for deldata in valdel:
            if deldata['batsman'] not in firstinningsbats:
                firstinningsbats.append(deldata['batsman'])
    return firstinningsbats
def getSecondInnExtras(batsmman):
    lstinnings=data['innings'][1]['2nd innings']['deliveries']
    total_run=0;
    for lstdelivery in lstinnings:
        valdel=(lstdelivery.values())
        for deldata in valdel:
             if(deldata['batsman']==batsmman):
                    total_run+=int(deldata['runs']['extras'])
    return total_run  

totalFirstInnExtras=list(map(getFirstInnExtras,first_innings_data()))
print(sum(totalFirstInnExtras))
totalSecondInnExtras=list(map(getSecondInnExtras,second_innings_data()))
print(sum(totalSecondInnExtras))
print('how many extra runs in 2nd Innings compare to 1st innings are '+str(sum(totalSecondInnExtras)-sum(totalFirstInnExtras)))
#print(lstinnings)
#print(lstinnings[0.1]['batsman'])
#print(lstinnings[0.1]['bowler'])
#print(len(data['innings'][0]['1st innings']['deliveries']))



