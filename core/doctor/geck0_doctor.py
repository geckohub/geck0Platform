from pathlib import Path
home=Path.home(); root=home/'geck0Platform'; bins=['geck0','ped0na','m0nkey','li0n','crumble','breadcrumbs','travelsheep','sealife','greengeck0','geck0earth','geck0record','blackgeck0','cyberx']
print('🦎 GECK0 DOCTOR v2.2')
for p in [root, root/'config', root/'knowledge', root/'updates', root/'apps']:
    print(('✅' if p.exists() else '⚠️'), p)
for b in bins:
    print(('✅' if (home/'bin'/b).exists() else '❌'), b)
