// LedgerPeak dashboard. Reads window.LP_DATA from data/data.js (built by scripts/refresh_dashboard.py).
(function () {
  const D = window.LP_DATA;
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);
  if (!D) {
    document.querySelector('main').innerHTML = '<p>No data yet. Run <code>scripts/refresh-dashboard.sh</code> and reload.</p>';
    return;
  }
  $('generated').textContent = 'Data refreshed ' + D.generated;

  const k = D.kpi;
  const gbp = (n) => '£' + Number(n).toLocaleString('en-GB', { maximumFractionDigits: 0 });
  $('kpis').innerHTML = [
    ['Paying clients', k.payingClients], ['Monthly recurring revenue', gbp(k.mrr)],
    ['Leads in pipeline', k.leadsInPipeline], ['Overdue invoices', k.overdueInvoices],
    ['AAT progress', k.aatProgress], ['Compliance items done', k.complianceDone],
  ].map(([l, v]) => `<div class="kpi"><div class="v">${esc(v)}</div><div class="l">${esc(l)}</div></div>`).join('');

  // Live office: department rooms, one character per desk, driven by data/live.js (written by scripts/office_hook.py)
  const DEPTS = ['Leadership', 'Growth', 'Client Services', 'Bookkeeping & Reporting', 'Legal & Compliance', 'Innovation & Learning Lab'];
  const person = (p) => `<div class="person" style="--hair:${p.hair};--skin:${p.skin};--shirt:${p.shirt}">
      <div class="hair"></div><div class="head"></div><div class="body"><i class="arm l"></i><i class="arm r"></i></div></div>`;
  const deskHtml = (a) => `<div class="seat idle" id="seat-${esc(a.id)}">
      <div class="bubble"></div>
      <div class="monitor"><div class="screen"></div></div>${person(a)}<div class="tabletop"></div>
      <div class="who">${esc(a.name)}</div><div class="role">${esc(a.role)}</div>
      <div class="task" data-last="${esc(a.lastTask)}">Last: ${esc(a.lastTask)}</div></div>`;
  $('floorplan').innerHTML =
    `<div class="room boss"><div class="roomname">Parth's corner office · CEO and signing officer</div>
      <div class="seat idle" id="seat-parth"><div class="bubble"></div><div class="monitor"><div class="screen"></div></div>
      ${person({ hair: '#1d1a18', skin: '#b07a52', shirt: '#1f2430' })}<div class="tabletop"></div>
      <div class="who">Parth Prajapati</div><div class="role">Approves everything before it leaves the office</div>
      <div class="task" data-last="">Approvals live in each client's 12-review-log.md</div></div></div>` +
    DEPTS.map((d) => `<div class="room"><div class="roomname">${esc(d)}</div><div class="desks">` +
      D.agents.filter((a) => a.dept === d).map(deskHtml).join('') + '</div></div>').join('');

  const nameOf = (id) => id === 'parth' ? 'Parth' : (D.agents.find((a) => a.id === id) || { name: id }).name;
  function paint(L) {
    if (!L) return;
    let busy = 0;
    D.agents.forEach((a) => {
      const seat = $('seat-' + a.id);
      const s = (L.agents || {})[a.id];
      const status = s ? s.status : 'idle';
      if (status === 'working') busy++;
      seat.className = 'seat ' + status;
      seat.querySelector('.bubble').textContent = status === 'working' ? s.task : status === 'done' ? '✔ done' : '';
      const t = seat.querySelector('.task');
      t.textContent = s ? (status === 'working' ? 'Now: ' : 'Last: ') + s.task : 'Last: ' + t.dataset.last;
    });
    const p = L.parth || { status: 'idle' };
    const ps = $('seat-parth');
    ps.className = 'seat ' + (p.status === 'giving task' ? 'working' : p.status === 'reviewing' ? 'done' : 'idle');
    ps.querySelector('.bubble').textContent = p.status === 'giving task' ? 'New task!' : p.status === 'reviewing' ? 'Review time' : '';
    $('liveDot').className = 'dot' + (busy ? ' on' : '');
    $('liveText').textContent = busy ? `${busy} working now · updated ${L.updated || ''}` : `Office quiet · last update ${L.updated || 'never'}`;
    $('liveFeed').innerHTML = (L.feed || []).slice().reverse().slice(0, 15)
      .map((f) => `<li><span class="todo">${esc(f.time.slice(11))}</span><b>${esc(nameOf(f.who))}</b> ${esc(f.text)}</li>`).join('') ||
      '<li>Nothing yet. Give the office a task in Claude Code, e.g. <code>/task prepare the DEMO café September close</code>.</li>';
  }
  paint(window.LP_LIVE || { agents: {}, feed: [] });

  // Re-read data/live.js every 3 seconds (a fresh <script> tag works offline from file://)
  let demo = false;
  setInterval(() => {
    if (demo) return;
    const s = document.createElement('script');
    s.src = 'data/live.js?t=' + Date.now();
    s.onload = () => { paint(window.LP_LIVE); s.remove(); };
    s.onerror = () => s.remove();
    document.body.appendChild(s);
  }, 3000);

  // Demo: plays a typical /task so Parth can see the workflow without running anything
  $('demoBtn').addEventListener('click', () => {
    demo = true;
    const L = { agents: {}, feed: [], parth: { status: 'giving task' } };
    const t = () => new Date().toLocaleTimeString('en-GB');
    const steps = [
      ['parth', null, 'New task: onboard a new café client and prepare their first VAT return'],
      ['grace-whitmore', 'working', 'Planning: split into onboarding, books, VAT, compliance check'],
      ['theo-ashford', 'working', 'Checking current VAT rules on GOV.UK'],
      ['theo-ashford', 'done', 'Briefed James on latest VAT guidance'],
      ['sophie-bennett', 'working', 'AML due diligence and risk rating'],
      ['leo-hartley', 'working', 'Categorising bank lines with double entry'],
      ['sophie-bennett', 'done', 'Engagement letter drafted'],
      ['leo-hartley', 'done', 'Bank reconciled, 1 query raised'],
      ['james-whitfield', 'working', 'VAT boxes 1 to 9 with workings'],
      ['victor-hale', 'working', 'Checking engagement terms'],
      ['james-whitfield', 'done', 'VAT draft ready, check-before-filing list added'],
      ['victor-hale', 'done', 'Terms OK, no solicitor needed'],
      ['grace-whitmore', 'done', 'Quality check passed, handed to Parth'],
      ['parth', 'review', 'Results ready for your review'],
    ];
    let i = 0;
    const tick = () => {
      if (i >= steps.length) { setTimeout(() => { demo = false; }, 6000); return; }
      const [who, st, text] = steps[i++];
      if (who === 'parth') L.parth = { status: st === 'review' ? 'reviewing' : 'giving task' };
      else L.agents[who] = { status: st, task: text };
      L.feed.push({ time: '00/00/0000 ' + t(), who, text });
      L.updated = t() + ' (demo)';
      paint(L);
      setTimeout(tick, 1600);
    };
    tick();
  });

  const stages = ['lead', 'contacted', 'call booked', 'proposal', 'won', 'lost'];
  $('board').innerHTML = stages.map((s) => {
    const cards = D.leads.filter((l) => (l.status || '').toLowerCase() === s)
      .map((l) => `<div class="card">${esc(l.name)}<small>${esc(l.trade)} · ${esc(l.area)}</small><small>${esc(l['next step'])}</small></div>`).join('');
    return `<div class="col"><h3>${s}</h3>${cards}</div>`;
  }).join('');

  $('clientTable').innerHTML = '<tr><th>Client</th><th>Package</th><th>Status</th><th>Next deadline</th><th>Risk</th></tr>' +
    (D.clients.map((c) => `<tr><td>${esc(c.name)}</td><td>${esc(c.package)}</td><td>${esc(c.status)}</td>
      <td>${esc(c.nextDeadline)}</td><td><span class="pill ${esc(c.risk)}">${esc(c.risk)}</span></td></tr>`).join('') ||
      '<tr><td colspan="5">No clients yet. Run /new-client.</td></tr>');

  $('deadlineList').innerHTML = D.deadlines.map((d) => {
    const cls = d.days < 0 ? 'overdue' : d.days <= 14 ? 'soon' : '';
    const when = d.days < 0 ? `${-d.days} days overdue` : d.days === 0 ? 'today' : `in ${d.days} days`;
    return `<li><span class="pill ${cls}">${esc(d.date)}</span><span>${esc(d.item)} <small class="todo">· ${esc(d.who)} · ${esc(d.owner)} · ${when}</small></span></li>`;
  }).join('') || '<li>Nothing due in the next 30 days.</li>';

  $('unitTable').innerHTML = '<tr><th>Level</th><th>Unit</th><th>Status</th><th>Score</th><th>Weak topics</th></tr>' +
    D.units.map((u) => `<tr><td>${esc(u.level)}</td><td>${esc(u.unit)}</td>
      <td><span class="pill ${esc(u.status.toLowerCase())}">${esc(u.status)}</span></td><td>${esc(u.score)}</td><td>${esc(u.weak)}</td></tr>`).join('');

  $('checkList').innerHTML = D.checklist.map((c) =>
    `<li><span class="${c.done ? 'done' : 'todo'}">${c.done ? '✔' : '○'}</span><span>${esc(c.item)}</span></li>`).join('');

  $('logList').innerHTML = D.log.map((l) => `<li>${esc(l)}</li>`).join('');

  const tabs = document.querySelectorAll('#tabs button');
  const show = (id) => {
    tabs.forEach((b) => b.classList.toggle('on', b.dataset.tab === id));
    document.querySelectorAll('.tab').forEach((t) => t.classList.toggle('on', t.id === id));
    try { localStorage.setItem('lp-tab', id); } catch (e) { /* storage blocked */ }
  };
  tabs.forEach((b) => b.addEventListener('click', () => show(b.dataset.tab)));
  try { const t = localStorage.getItem('lp-tab'); if (t && $(t)) show(t); } catch (e) { /* storage blocked */ }
})();
