# Backup policy

Include the source/configuration tree in the Tuesday architecture backup, but exclude `geck0Verse/data/`, Android build outputs, APK/AAB files and client assets. `.geck0backupignore` lists the intended exclusions. Domain client sites and large media should use separate backup policies.
