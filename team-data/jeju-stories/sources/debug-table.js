const { chromium } = require('playwright');

async function debugTable() {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  await page.goto('https://jeju.go.kr/culture/myth/list/all.htm', {
    waitUntil: 'networkidle',
    timeout: 60000
  });

  // 테이블 구조 상세 분석
  const tableInfo = await page.evaluate(() => {
    const table = document.querySelector('table');
    if (!table) return { error: 'No table found' };

    // 헤더 확인
    const headers = Array.from(table.querySelectorAll('thead th, tr:first-child th')).map(th => th.innerText.trim());

    // 첫 5개 행 데이터
    const rows = Array.from(table.querySelectorAll('tbody tr')).slice(0, 5).map(row => {
      const cells = Array.from(row.querySelectorAll('td'));
      return cells.map((cell, i) => ({
        index: i,
        text: cell.innerText?.trim().slice(0, 100),
        html: cell.innerHTML?.slice(0, 200),
        hasLink: !!cell.querySelector('a'),
        linkHref: cell.querySelector('a')?.href
      }));
    });

    return { headers, rows, rowCount: table.querySelectorAll('tbody tr').length };
  });

  console.log('📊 테이블 구조 분석:\n');
  console.log('헤더:', tableInfo.headers);
  console.log('행 개수:', tableInfo.rowCount);
  console.log('\n첫 5개 행 데이터:');
  tableInfo.rows.forEach((row, i) => {
    console.log(`\n--- 행 ${i + 1} ---`);
    row.forEach(cell => {
      console.log(`  [${cell.index}] ${cell.text}`);
      if (cell.hasLink) console.log(`       링크: ${cell.linkHref}`);
    });
  });

  await browser.close();
}

debugTable().catch(console.error);
