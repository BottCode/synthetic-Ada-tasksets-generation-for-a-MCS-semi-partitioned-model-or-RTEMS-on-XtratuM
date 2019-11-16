import unittest
import rta
import copy

# Unit tests for the RTA algorithms

# NOTATION USED IN THE COMMENTS

# TASKSETS: Tasks are defined according to the logic of the rta scripts
# every taskset is preceded by a description of the tasks in which
# each taskset is represented by a 4-uple (T, Cis, L, P) in which
# T is the period/deadline, Cis is an array of WCETs (first LO-crit, then HI-crit),
# L is the criticality, P is the priority.

# All tests are supposed to be for core c1

# UTILITY FUNCTIONS

# Vestal's classic algorithm
def testVestal (tasks):
  for i in range(len(tasks)):
    if not rta.audsley_rta_no_migration(i, tasks, 'c1'):
      return False
  return True

# Ri(LO)
def testRiLO (tasks):
  for i in range(len(tasks)):
    if not rta.audsley_rta_steady(i, tasks, 'c1'):
      return False
  return True

# Ri(MIX)
def testRiMIX (tasks):
  for i in range(len(tasks)):
    if not rta.audsleyRiMIX(i, tasks, 'c1'):
      return False
  return True

# Ri(LO')
def testRiLO_1 (tasks):
  for i in range(len(tasks)):
    if not rta.audsleyRiLO_1(i, tasks, 'c1'):
      return False
  return True

# Ri(HI')
def testRiHI_1 (tasks):
  for i in range(len(tasks)):
    if not rta.audsleyRiHI_1(i, tasks, 'c1'):
      return False
  return True

# Taskset 1:
# t1: (4, [2, 4], HI, 2)
# t2: (5, [1, 2], HI, 1)
# t3: (5, [1], LO, 0)
TASKSET_1 = [
  {'HI': True, 'C(LO)': 2, 'C(HI)': 4, 'D': 4, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 2}},
  {'HI': True, 'C(LO)': 1, 'C(HI)': 2, 'D': 5, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 1}},
  {'HI': False, 'C(LO)': 1, 'C(HI)': -1, 'D': 5, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 0}}
]

# Taskset 2
# t1: (4, [2, 3], HI, 1)
# t2: (5, [1], LO, 2) migrating
# t3: (5, [1], LO, 0)
TASKSET_2 = [
  {'HI': True,  'C(LO)': 2, 'C(HI)': 3, 'D': 4, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 1}},
  {'HI': False, 'C(LO)': 1, 'C(HI)': -1, 'D': 5, 'J': 0, 'migrating': True, 'migration_route': ['c2', 'c3'], 'P': {'c1': 2}},
  {'HI': False, 'C(LO)': 1, 'C(HI)': -1, 'D': 5, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 0}}
]

# Taskset 3: same as Taskset 2 but task t1 has lower HI-crit WCET
# t1: (4, [2, 2], HI, 1)
# t2: (5, [1], LO, 2) migrating
# t3: (5, [1], LO, 0)
TASKSET_3 = [
  {'HI': True,  'C(LO)': 2, 'C(HI)': 2, 'D': 4, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 1}},
  {'HI': False, 'C(LO)': 1, 'C(HI)': -1, 'D': 5, 'J': 0, 'migrating': True, 'migration_route': ['c2', 'c3'], 'P': {'c1': 2}},
  {'HI': False, 'C(LO)': 1, 'C(HI)': -1, 'D': 5, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 0}}
]

# Taskset 4
# t1: (5, [2], LO, 0)
# t2: (2, [1], LO, 1) migrated from another core
TASKSET_4 = [
  {'HI': False, 'C(LO)': 2, 'C(HI)': -1, 'D': 5, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 0}},
  {'HI': False, 'C(LO)': 1, 'C(HI)': -1, 'D': 1, 'D1': 2, 'J': 0, 'migrating': True, 'migration_route': ['c1', 'c4'], 'P': {'c1': 1}}
]

# Taskset 5: same as Taskset 4 but task t2 has increased deadline and WCET
# t1: (5, [2], LO, 0)
# t2: (3, [2], LO, 1) migrated from another core
TASKSET_5 = [
  {'HI': False, 'C(LO)': 2, 'C(HI)': -1, 'D': 5, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 0}},
  {'HI': False, 'C(LO)': 2, 'C(HI)': -1, 'D': 1, 'D1': 3, 'J': 0, 'migrating': True, 'migration_route': ['c1', 'c4'], 'P': {'c1': 1}}
]

# Taskset 6
# t1: (5, [2, 4], HI, 0)
# t2: (2, [1], LO, 1) migrated from another core
TASKSET_6 = [
  {'HI': True, 'C(LO)': 2, 'C(HI)': 4, 'D': 5, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 0}},
  {'HI': False, 'C(LO)': 1, 'C(HI)': -1, 'D': 1, 'D1': 2, 'J': 0, 'migrating': True, 'migration_route': ['c1', 'c4'], 'P': {'c1': 1}}
]

# Taskset 7
# t1: (5, [2, 4], HI, 0)
# t2: (3, [1], LO, 1) migrated from another core
TASKSET_7 = [
  {'HI': True, 'C(LO)': 2, 'C(HI)': 4, 'D': 5, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 0}},
  {'HI': False, 'C(LO)': 1, 'C(HI)': -1, 'D': 1, 'D1': 3, 'J': 0, 'migrating': True, 'migration_route': ['c1', 'c4'], 'P': {'c1': 1}}
]

# Taskset 8: this is an unschedulable edge case
# t1: (1, [2, 4], HI, 0)
TASKSET_8 = [
  {'HI': True, 'C(LO)':2, 'C(HI)': 4, 'D': 1, 'J': 0, 'migrating': False, 'migration_route': [], 'P': {'c1': 0}}
]

class TestRTA(unittest.TestCase):

  # TASKSET_1 should be schedulable according to Ri(LO)
  # We only use C(LO)
  def test_RiLO_TASKSET_1(self):
    tasks = copy.deepcopy(TASKSET_1)
    # t1: (4, [2, 4], HI, 2)
    # t2: (5, [1, 2], HI, 1)
    # t3: (5, [1], LO, 0)
    # R1(LO) = 2 + 0 = 2 (OK)
    # R2(LO) = 1 + ceiling(1/4) * 2 = 3 ==> 1 + math.ceil(3/4) * 2 = 3 (OK)
    # R3(LO) = 1 + ceiling(1/5) * 1 + ceiling(1/4) * 2 = 4 ==> 1 + ceiling(4/5) * 1 + ceiling(4/4) * 2 = 4 (OK)
    self.assertEqual(testRiLO(tasks), True)

  # TASKSET_1 should not be schedulable according to Vestal's algorithm
  # Task t1 C(HI) creates too much interference for task t2
  def test_Vestal_TASKSET_1(self):
    tasks = copy.deepcopy(TASKSET_1)
    # t1: (4, [2, 4], HI, 2)
    # t2: (5, [1, 2], HI, 1)
    # t3: (5, [1], LO, 0)
    # R1 = 4 + 0 = 4 (OK)
    # R2 = 2 + ceiling(2/4) * 4 = 6 > 5 (!!! KO)
    self.assertEqual(testVestal(tasks), False)

  # TASKSET_2 should be schedulable according to Ri(LO)
  def test_RiLO_TASKSET_2(self):
    tasks = copy.deepcopy(TASKSET_2)
    # t1: (4, [2, 3], HI, 1)
    # t2: (5, [1], LO, 2) migrating
    # t3: (5, [1], LO, 0)
    # R1(LO) = 2 + ceiling(2/5) * 1 = 3 ==> 2 + ceiling(3/5) * 1 = 3 (OK)
    # R2(LO) = 1 + 0 = 1 (OK)
    # R3(LO) = 1 + ceiling(1/4) * 2 + ceiling(1/5) * 1 = 4 ==> 1 + ceiling(4/4) * 2 + ceiling(4/5) * 1 = 4 (OK)
    self.assertEqual(testRiLO(tasks), True)

  # TASKSET_2 should not be schedulable according to Ri(MIX)
  # Task t3 receives too much interference from task t1
  def test_RiMIX_TASKSET_2(self):
    tasks = copy.deepcopy(TASKSET_2)
    # Run steady mode test in order to calculate Ri(LO)
    testRiLO(tasks)
    # t1: (4, [2, 3], HI, 1)
    # t2: (5, [1], LO, 2) migrating
    # t3: (5, [1], LO, 0)
    # R1(LO) = 3
    # R2(LO) = 1
    # R3(LO) = 4
    # R1(MIX) = 3 + 0 + ceiling(3/5) * 1 = 4 (OK)
    # R3(MIX) = 1 + ceiling(1/4) * 3 + ceiling(1/5) * 1 = 5 ==> 1 + ceiling(5/4) * 3 + ceiling(1/5) * 1 = 8 > 5 (!!! KO)
    self.assertEqual(testRiMIX(tasks), False)

  # TASKSET_3 should be schedulable according to Ri(MIX)
  # We reduced task t1 HI-crit WCET so that task t3 has less interference
  def test_RiMIX_TASKSET_3(self):
    tasks = copy.deepcopy(TASKSET_3)
    # Run steady mode test in order to calculate Ri(LO)
    testRiLO(tasks)
    # t1: (4, [2, 2], HI, 1)
    # t2: (5, [1], LO, 2) migrating
    # t3: (5, [1], LO, 0)
    # R1(LO) = 3
    # R2(LO) = 1
    # R3(LO) = 4
    # R1(MIX) = 2 + 0 + ceiling(2/5) * 1 = 3 (OK)
    # R3(MIX) = 1 + ceiling(1/4) * 2 + ceiling(1/5) * 1 = 4 ==> 1 + ceiling(4/4) * 2 + ceiling(4/5) * 1 = 4 (OK)
    self.assertEqual(testRiMIX(tasks), True)

  # TASKSET_4 should be schedulable according to Ri(LO')
  def test_RiLO1_TASKSET_4(self):
    tasks = copy.deepcopy(TASKSET_4)
    # t1: (5, [2], LO, 0)
    # t2: (2, [1], LO, 1) migrated from another core
    # R1(LO') = 2 + ceiling(2/2) * 1 = 3 ==> 2 + ceiling(3/2) * 1 = 4 ==> 2 + ceiling(4/2) * 1 = 4 (OK)
    # R2(LO') = 1 + 0 = 1 (OK)
    self.assertEqual(testRiLO_1(tasks), True)

  # TASKSET_5 should not be schedulable according to Ri(LO')
  # The interference from task t2 becomes too much for task t1
  def test_RiLO1_TASKSET_5(self):
    tasks = copy.deepcopy(TASKSET_5)
    # t1: (5, [2], LO, 0)
    # t2: (3, [2], LO, 1) migrated from another core
    # R1(LO') = 2 + ceiling(2/3) * 2 = 4 ==> 2 + ceiling(4/3) * 2 = 6 > 5 (!!! KO)
    self.assertEqual(testRiLO_1(tasks), False)

  # TASKSET_6 should not be schedulable according to RI(HI')
  def test_RiHI_1_TASKSET_6(self):
    tasks = copy.deepcopy(TASKSET_6)
    testRiLO_1(tasks)
    # t1: (5, [2, 4], HI, 0)
    # t2: (2, [1], LO, 1) migrated from another core
    # R1(LO') = 4
    # R1(HI') = 4 + ceiling(4/2) * 2 = 6 > 5 (!!! KO)
    self.assertEqual(testRiHI_1(tasks), False)

  # TASKSET_7 should be schedulable according to RI(HI')
  def test_RiHI_1_TASKSET_7(self):
    tasks = copy.deepcopy(TASKSET_7)
    testRiLO_1(tasks)
    # t1: (5, [2, 4], HI, 0)
    # t2: (3, [1], LO, 1) migrated from another core
    # Ri(LO') = 3
    # Ri(HI') = 4 + ceiling(3/3) * 1 = 5 (OK)
    self.assertEqual(testRiHI_1(tasks), True)

  # No algorithm should be able to schedule TASKSET_7
  def test_TASKSET_8(self):
    tasks = copy.deepcopy(TASKSET_8)
    self.assertEqual(testVestal(tasks), False)
    self.assertEqual(testRiLO(tasks), False)
    self.assertEqual(testRiMIX(tasks), False)
    self.assertEqual(testRiLO_1(tasks), False)
    self.assertEqual(testRiHI_1(tasks), False)





if __name__ == '__main__':
  unittest.main()