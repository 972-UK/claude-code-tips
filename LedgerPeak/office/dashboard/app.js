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

  // Floor plan: Parth's corner office plus nine desks
  const colours = ['#1f6f5c', '#7b4ea3', '#b5651d', '#2a6fb0', '#a83e5a', '#3f7f3a', '#c08a1a', '#5a5f6b', '#2f8f8f'];
  $('floorplan').innerHTML =
    `<div class="desk boss"><div class="avatar" style="background:#1f2430">PP</div><div class="who">Parth Prajapati</div>
     <div class="role">CEO and signing officer · corner office</div><div class="task">Approvals waiting live in each client's 12-review-log.md</div></div>` +
    D.agents.map((a, i) => {
      const initials = a.name.split(' ').map((w) => w[0]).join('');
      return `<div class="desk"><div class="avatar" style="background:${colours[i % colours.length]}">${esc(initials)}</div>
        <div class="who">${esc(a.name)}</div><div class="role">${esc(a.role)}</div>
        <div class="task">Last: ${esc(a.lastTask)}</div><span class="status ${esc(a.status)}">${esc(a.status)}</span></div>`;
    }).join('');

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
