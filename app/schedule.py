mport heapq
from collections import defaultdict
# (inc, serv, alert) sum() = total people that day
NUM_PEOPLE = 35

people = []
counts = dict()
for i in range(NUM_PEOPLE):
  people.append('Person ' + str(i))
  counts['Person ' + str(i)] = dict()
  counts['Person ' + str(i)]['incident'] = 0
  counts['Person ' + str(i)]['service'] = 0
  counts['Person ' + str(i)]['alert'] = 0

# ignore
incidents = [(0, p) for p in people]
alerts = [(0, p) for p in people]
services = [(0, p) for p in people]

heapq.heapify(incidents)
heapq.heapify(alerts)
heapq.heapify(services)

# people = array of indices
def getSchedule(ninc, nserv, nalert, people):
  # loop thru heapq incidents:def getMember(mems, selected, day):
  selection = defaultdict(list)
  
  taken = []
  putBackInc = []
  putBackServ = []
  putBackAlert = []

  while ninc > 0 or nserv > 0 or nalert > 0:
    if ninc > 0:
      incidentPotentialMember = heapq.heappop(incidents)
      while incidentPotentialMember[1] in taken or incidentPotentialMember[1] not in people:
        putBackInc.append(incidentPotentialMember)
        incidentPotentialMember = heapq.heappop(incidents)
      selection['incident'].append(incidentPotentialMember[1])
      counts[incidentPotentialMember[1]]['incident'] += 1
      taken.append(incidentPotentialMember[1])
      putBackInc.append((incidentPotentialMember[0] + 1, incidentPotentialMember[1]))
      ninc -= 1
      # print("selecting incident")
    # for putBackMember in putBackInc:
      # heapq.heappush(incidents, putBackMember)


  # service
    if nserv > 0:
      servicePotentialMember = heapq.heappop(services)
      while servicePotentialMember[1] in taken or servicePotentialMember[1] not in people:
        putBackServ.append(servicePotentialMember)
        servicePotentialMember = heapq.heappop(services)
      selection['service'].append(servicePotentialMember[1])
      counts[servicePotentialMember[1]]['service'] += 1
      putBackServ.append((servicePotentialMember[0] + 1, servicePotentialMember[1]))
      taken.append(servicePotentialMember[1])
      nserv -= 1

      # print("selecting service")
      # for putBackMember in putBack:
        # heapq.heappush(services, putBackMember)

  # alerts
    if nalert > 0:
      alertPotentialMember = heapq.heappop(alerts)
      while alertPotentialMember[1] in taken or alertPotentialMember[1] not in people:
        putBackAlert.append(alertPotentialMember)
        alertPotentialMember = heapq.heappop(alerts)
      selection['alert'].append(alertPotentialMember[1])
      counts[alertPotentialMember[1]]['alert'] += 1
      putBackAlert.append((alertPotentialMember[0] + 1, alertPotentialMember[1]))
      taken.append(alertPotentialMember[1])
      nalert -= 1
      # print('selecting alert')
      # for putBackMember in putBack:
        # heapq.heappush(alerts, putBackMember)
  for putBackMember in putBackInc:
    heapq.heappush(incidents, putBackMember)
  for putBackMember in putBackServ:
    heapq.heappush(services, putBackMember)
  for putBackMember in putBackAlert:
    heapq.heappush(alerts, putBackMember)
  return selection


def printSchedule(sch, dayidx):
  print("=== Day {} ===".format(dayidx))
  print('incident: {}'.format(', '.join(sch['incident'])))
  print('services: {}'.format(', '.join(sch['service'])))
  print('alerts: {}'.format(', '.join(sch['alert'])))

def printCounts():
  print("=== Counts ===")
  for k,v in counts.items():
    s = v['incident'] + v['service'] + v['alert']
    print(k, ': ', v, ', total: ', s )

def getDailySchedule(i, r, a, l):
    peeps = [people[idx] for idx in l]
    return getSchedule(i, r, a, peeps)

# getSchedule (i, r, a, [])
# day1
# g1 = [5] # mon - fri (16-20)
# g2 = [15] # tues - sat (21-35)
# g3 = [15] # sun - thurs ( 1-15)
# dailyAttendance = [(0, 15), (0,20), (0, 35), (0, 35), (0,35), (15, 35), (20, 35)]
# dailySplit = [(6,6,3), (8,8,4), (14, 14, 7), (14, 14, 7), (14, 14, 7), (8,8,4), (6,6,3)]
# dailySplitRough = [(7,3,5), (9,3,8), (20, 10, 5), (15, 16, 4), (10, 10, 15), (5,5,10), (6,6,3)]
# for tidx in range(80):
#   idx = tidx % len(dailyAttendance)
#   day = dailyAttendance[idx]
#   dsplit = dailySplitRough[idx]
#   peoplelist = [people[i] for i in range(day[0], day[1])]
#   sch = getSchedule(dsplit[0], dsplit[1], dsplit[2], peoplelist)
#   printSchedule(sch, idx)
# printCounts()
# 
