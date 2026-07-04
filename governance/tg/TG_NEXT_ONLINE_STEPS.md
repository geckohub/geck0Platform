# TG next online steps

When ThaiGreen is online, run:

scp -P 1991 lucy@192.168.1.244:/home/lucy/geck0Platform/governance/tg/bootstrap/geck0_tg_catchup_all.sh ~/
chmod +x ~/geck0_tg_catchup_all.sh
~/geck0_tg_catchup_all.sh

Then check:

ls -lh ~/geck0Platform_tg_updates/{incoming,extracted,applied,logs}
