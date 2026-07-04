import sys,pathlib,datetime,json
root=pathlib.Path.home()/'geck0Platform/apps/greengeck0'; runs=root/'runs'; runs.mkdir(parents=True,exist_ok=True)
args=sys.argv[1:]
if args and args[0]=='ingest':
 url=args[1] if len(args)>1 else 'https://example.com'
 run=runs/datetime.datetime.utcnow().strftime('%Y%m%d_%H%M%S'); run.mkdir()
 (run/'test_plan.md').write_text(f'# GreenGeck0 Test Plan\n\nTarget: {url}\n\n- Smoke\n- Regression\n- Accessibility\n- API checks\n- Load/stress placeholder\n- Handoff to BlackGeck0/GeckoScan after QA\n')
 (run/'playwright_example.spec.ts').write_text(f"import {{ test, expect }} from '@playwright/test';\ntest('homepage loads', async ({{ page }}) => {{ await page.goto('{url}'); await expect(page).toHaveTitle(/.+/); }});\n")
 print('🟢 GreenGeck0 created test scaffold:', run)
else: print('🟢 GreenGeck0 ready. Try: greengeck0 ingest https://example.com --type smoke --framework playwright')
