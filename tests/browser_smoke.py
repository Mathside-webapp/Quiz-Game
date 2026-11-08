from playwright.sync_api import sync_playwright
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1440,'height':1100},device_scale_factor=1)
 errors=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:5173')
 page.screenshot(path='/tmp/quiz-desktop.png',full_page=True)
 page.get_by_role('link',name='Try the Demo').click()
 page.get_by_role('link',name='Quiz Library',exact=True).click()
 page.get_by_role('link',name='New Quiz').click()
 page.locator('#title').fill('Test planets')
 page.locator('#prompt').fill('Which planet is blue?')
 for i,v in enumerate(['Earth','Mars','Venus','Mercury']):page.locator(f'input[name="option{i}"]').fill(v)
 page.get_by_role('button',name='Save Quiz',exact=True).click()
 page.reload()
 page.get_by_role('searchbox').fill('Test planets')
 assert page.locator('tbody tr').count()==1
 page.get_by_role('button',name='Preview',exact=True).click()
 assert page.get_by_role('dialog').get_by_text('Which planet is blue?',exact=False).count()==1
 page.get_by_role('button',name='Close dialog').click()
 page.get_by_role('button',name='Duplicate Test planets').click()
 assert page.locator('tbody tr').count()==2
 page.get_by_role('button',name='Delete Test planets (copy)',exact=True).click()
 page.get_by_role('button',name='Delete Quiz',exact=True).click()
 assert page.locator('tbody tr').count()==1
 page.get_by_role('link',name='Classroom Sessions',exact=True).click()
 page.locator('#session-quiz').select_option(label='Test planets (1 questions)')
 page.get_by_role('button',name='Start Quiz Rehearsal').click()
 page.get_by_role('button',name='A Earth').click()
 page.get_by_role('button',name='Finish rehearsal').click()
 assert page.get_by_text('1 / 1',exact=True).count()==1
 page.goto('http://127.0.0.1:5173/#dashboard')
 page.screenshot(path='/tmp/quiz-dashboard.png',full_page=True)
 page.set_viewport_size({'width':390,'height':844})
 for route in ['home','dashboard','games','quizzes','create','sessions','results','settings']:
  page.goto('http://127.0.0.1:5173/#'+route)
  page.wait_for_timeout(100)
  assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),route+' overflow'
 page.goto('http://127.0.0.1:5173/#home')
 page.screenshot(path='/tmp/quiz-mobile.png',full_page=True)
 assert not errors,errors
 print('PASS: create/reload/search/preview/duplicate/delete/rehearsal/results; eight mobile routes; no page errors')
 b.close()
