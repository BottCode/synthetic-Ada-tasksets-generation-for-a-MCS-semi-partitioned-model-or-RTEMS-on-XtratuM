import math
import utils
import itertools

fake_system = {'c1': {'HIGH': [
    # {'ID': 7, 'HI': True, 'C(HI)': 18, 'D': 42, 'P': {'c1': 1, 'c2': -1}}, 
    {'ID': 5, 'HI': True, 'C(HI)': 15, 'D': 36, 'P': {'c1': 2, 'c2': -1}}, 
    {'ID': 4, 'HI': True, 'C(HI)': 9, 'D': 30, 'P': {'c1': 3, 'c2': -1}}]}
}

fake_scheduling_plan = {'c1': {'HIGH': {'U': 0.5689675603354601, 'S': 26, 'W': 13}, 'LOW': {'U': 0.5689675603354601, 'S': 26, 'W': 14}, 'slot_size': 6, 'IWRR_list': ['HIGH', 'LOW', 'HIGH', 'LOW', 'HIGH', 'LOW', 'LOW', 'LOW']}}

##############
# analyze_system
##############

def analyze_system (system, scheduling_plan):
    # for each partition, verify if its inner tasks are schedulable according to RTA for Fixed Priority scheduling.
    are_partitions_schedulable = check_inner_partition_schedulability (system)
    print ("RTA: ", are_partitions_schedulable)
    # if so, the check the partion scheduling
    if are_partitions_schedulable:
        return check_intra_partition_scheduling (system, scheduling_plan)
    else:
        return False

def check_intra_partition_scheduling (system, scheduling_plan):
    for core in system:
        most_loaded_partition = 'HIGH' if scheduling_plan[core]['HIGH']['W'] > scheduling_plan[core]['LOW']['W'] else 'LOW'
        for partition in system[core]:
            scheduling_plan_starting_from_critical_instant = scheduling_plan[core]['IWRR_list'] if partition == most_loaded_partition else list (reversed (scheduling_plan[core]['IWRR_list']))
            # print (scheduling_plan_starting_from_critical_instant)
            for task in system[core][partition]:
                time_passed = 0
                response_time = task['Ri']
                print ("PS analysis on task ", task)
                for minor_frame in itertools.cycle (scheduling_plan_starting_from_critical_instant):
                    diff = 0
                    if minor_frame == partition:
                        print ("My turn :) ", response_time)
                        print("|")
                        print ("v")
                        if response_time >= scheduling_plan[core]['slot_size']:
                            response_time -= scheduling_plan[core]['slot_size']
                        else:
                            diff = scheduling_plan[core]['slot_size'] - response_time
                            response_time = 0
                        print (response_time)
                    else:
                        print ("interference!!!")
                    print ("tp", time_passed)
                    print("|")
                    print ("v")
                    time_passed += scheduling_plan[core]['slot_size'] if diff == 0 else diff
                    task['PS_Ri'] = time_passed
                    print (time_passed)
                    if time_passed > task['D']:
                        print ("\nOUCH!!", time_passed, task)
                        return False
                    if response_time <= 0:
                        # this task is schedulable on partitioned scheduling!
                        break
    return True

def check_inner_partition_schedulability (system):
    for core in system:
        for partition in system[core]:
            for task in system[core][partition]:
                # select tasks with priority higher than the current one
                higher_priority_tasks = list (filter (lambda t: t['P'][core] > task['P'][core], system[core][partition]))
                print_hp (task['P'][core], higher_priority_tasks)
                # task['Ri'] = task['C(HI)'] if task['HI'] else task['C(LO)']
                task['Ri'] = calcRi (task, higher_priority_tasks)
                if task['Ri'] == None:
                    return False
                # for hp_task in higher_priority_tasks:
                #    hp_C = hp_task['C(HI)'] if hp_task['HI'] else hp_task['C(LO)']
                #    # compute response time for current task
                #    task['Ri'] += math.ceil (task['Ri'] / hp_task['D']) * hp_C
                #    if task['Ri'] > task['D']:
                #        return False
                
    return True

def print_hp (starting_p, hp_tasks):
    print ("Priorities higher than", starting_p)
    for t in hp_tasks:
        print (t['P']['c1'])

# Vestal's algorithm (classic version)
def calcRi (task, hp):
  start_Ri = task['C(HI)']
  Ri = start_Ri
  while True:
    newRi = start_Ri
    for hp_task in hp:
      hp_C = hp_task['C(HI)']
      newRi += math.ceil(Ri / hp_task['D']) * hp_C
    if newRi > task['D']:
      return None
    if newRi == Ri:
      return newRi
    Ri = newRi

fake_system['c1']['HIGH'] = sorted (fake_system['c1']['HIGH'], key = lambda t: t['P']['c1'], reverse = True)
print ("PS: ", analyze_system (fake_system, fake_scheduling_plan))
print (fake_system)