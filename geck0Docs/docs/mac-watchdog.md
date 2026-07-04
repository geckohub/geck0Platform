# Mac Watchdog

The Mac watchdog watches:

- `/Users/phildonachie/Out/Jellied Eel`
- `/Users/phildonachie/Out/Thai Green`

and sends files to the matching Pi.

It prefers `rsync` because it supports partial transfers, resumes, and avoids re-sending unchanged files.

`scp` is simpler but less efficient.
