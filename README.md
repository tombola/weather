# Weather

To run on boot add the following to `/etc/rc.local` (above `exit 0`)

```
/boot/secrets.sh
python3 /home/pi/weather/log_samples.py
```

Create the file `/boot/secrets.sh` with

```
export SUPABASE_KEY=thekeyfromsupabasedashboard
export SUPABASE_URL=theurlfromsupabasedashboard
```
