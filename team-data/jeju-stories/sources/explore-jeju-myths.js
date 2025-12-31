const { chromium } = require('playwright');

async function exploreJejuMyths() {
  const browser = await chromium.launch({
    headless: false  // 브라우저 보이게 해서 구조 파악
  });

  const context = await browser.newContext();
  const page = await context.newPage();

  console.log('🔍 제주도청 설화 페이지 탐색 중...\n');

  await page.goto('https://jeju.go.kr/culture/myth/list.htm', {
    waitUntil: 'networkidle',
    timeout: 60000
  });

  // 페이지 구조 파악
  console.log('📄 페이지 타이틀:', await page.title());

  // 카테고리/메뉴 찾기
  const categories = await page.$$eval('a, button, .menu, .tab, .category', elements =>
    elements.slice(0, 50).map(el => ({
      text: el.innerText?.trim().slice(0, 50),
      href: el.href || null,
      class: el.className
    })).filter(e => e.text && e.text.length > 0)
  );

  console.log('\n📂 발견된 링크/버튼:');
  categories.forEach((c, i) => {
    if (c.text.includes('신화') || c.text.includes('전설') || c.text.includes('민담') || c.text.includes('설화')) {
      console.log(`  [${i}] "${c.text}" -> ${c.href || '(no href)'}`);
    }
  });

  // 리스트 아이템 찾기
  const listItems = await page.$$eval('li a, .list-item, tr td a, .title a', elements =>
    elements.slice(0, 30).map(el => ({
      text: el.innerText?.trim().slice(0, 100),
      href: el.href || null
    })).filter(e => e.text && e.text.length > 2)
  );

  console.log('\n📜 발견된 설화 목록 (상위 30개):');
  listItems.forEach((item, i) => {
    console.log(`  [${i}] ${item.text}`);
    if (item.href) console.log(`      -> ${item.href}`);
  });

  // 테이블 구조 확인
  const tables = await page.$$('table');
  console.log(`\n📊 테이블 개수: ${tables.length}`);

  // 페이지 HTML 일부 저장
  const html = await page.content();
  require('fs').writeFileSync('page-structure.html', html);
  console.log('\n💾 페이지 HTML 저장됨: page-structure.html');

  // 10초 대기 (수동 확인용)
  console.log('\n⏳ 10초 대기 중... 브라우저에서 구조 확인하세요');
  await page.waitForTimeout(10000);

  await browser.close();
  console.log('\n✅ 탐색 완료');
}

exploreJejuMyths().catch(console.error);
