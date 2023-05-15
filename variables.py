from datetime import datetime as dt, timedelta as td

import settings


SESSION_STAGE = ''
# START_MENU, ABOUT, INPUT_DATA, GUIDE,
# START_TRAIN, PRE_EXAM, START_EXAM, STOP_STAGE, RESULT

lp_name = ''
rp_name = ''
group_name = ''

score = 0

dwall_amount = settings.dwall_amount
dwall_speed = settings.dwall_speed
acc_dwall_speed = dwall_speed * 2
dwall_difficulty = settings.difficulty
dwall_changed = False

is_warmuped = False
debug_activated = False

start_stage_time = dt.now()
stage_time = td()

lp_active_time = td()
lp_left_time = dt.now()
lp_right_time = dt.now()
lp_accelerate_time = dt.now()
lp_active_acc_time = td()
lp_key_pushes = 0

rp_active_time = td()
rp_left_time = dt.now()
rp_right_time = dt.now()
rp_accelerate_time = dt.now()
rp_active_acc_time = td()
rp_key_pushes = 0

accelerate = False
accelerate_started = False
accelerate_time = td()
start_accelerate_time = dt.now()

conflict = False
conflict_started = False
conflict_time = td()
start_conflict_time = dt.now()

cooperation = False
coop_started = False
cooperative_time = td()
start_cooperative_time = dt.now()

active_p = ''
active_acc_p = ''
active_kpush_p = ''

pl_pos_log = False
