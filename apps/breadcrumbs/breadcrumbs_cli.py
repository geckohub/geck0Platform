import pathlib, sys
root=pathlib.Path.home()/'geck0Platform/apps/breadcrumbs'
for d in ['drop','requirements','generated','staging','published','brand_research','clients','logs']: (root/d).mkdir(parents=True,exist_ok=True)
print('🍞 BreadCrumbs ready. Drop requirements in:', root/'drop')
print('Brand discovery placeholder will enrich company colours/themes once web/API adapters are configured.')
