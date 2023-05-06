import datetime as dt


SESSION_STAGE = ''
# START_MENU, START_TRAIN, START_EXAM, STOP_STAGE

start_stage_time = dt.datetime.now()
stage_time = dt.timedelta()

lp_active_time = dt.timedelta()
lp_left_time = dt.datetime.now()
lp_right_time = dt.datetime.now()
lp_accelerate_time = dt.datetime.now()
lp_active_acc_time = dt.timedelta()
lp_key_pushes = 0

rp_active_time = dt.timedelta()
rp_left_time = dt.datetime.now()
rp_right_time = dt.datetime.now()
rp_accelerate_time = dt.datetime.now()
rp_active_acc_time = dt.timedelta()
rp_key_pushes = 0

accelerate = False
accelerate_started = False
accelerate_time = dt.timedelta()
start_accelerate_time = dt.datetime.now()

conflict = False
conflict_started = False
conflict_time = dt.timedelta()
start_conflict_time = dt.datetime.now()

cooperation = False
coop_started = False
cooperative_time = dt.timedelta()
start_cooperative_time = dt.datetime.now()