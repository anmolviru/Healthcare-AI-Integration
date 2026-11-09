import { useEffect, useState } from 'react';

const API = 'http://127.0.0.1:8000';

function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch(`${API}/api/overview`)
      .then(r => { if (!r.ok) throw new Error('Backend response was not successful'); return r.json(); })
      .then(setData)
      .catch(() => setError('Backend is not connected. Start the FastAPI server and refresh this page.'));
  }, []);

  return <div className="app">
    <header><div><p className="eyebrow">STRATEGIC PLANNING PROTOTYPE</p><h1>Healthcare AI Integration</h1><p className="sub">A dashboard for responsible AI adoption planning in healthcare</p></div><span className="status">Educational demo</span></header>
    {error && <div className="notice">{error}</div>}
    {!data ? <p className="loading">Loading dashboard data…</p> : <>
      <section className="stats">{data.kpis.map(k => <article className="stat" key={k.name}><p>{k.name}</p><strong>{k.value}</strong><small>{k.note}</small></article>)}</section>
      <section className="panel"><div className="section-head"><div><p className="eyebrow">01 / OPPORTUNITIES</p><h2>Healthcare AI use cases</h2></div></div><div className="table-wrap"><table><thead><tr><th>Use case</th><th>Area</th><th>Potential benefit</th><th>Readiness</th></tr></thead><tbody>{data.use_cases.map(x => <tr key={x.id}><td>{x.name}</td><td>{x.area}</td><td>{x.benefit}</td><td><span className="tag">{x.readiness}</span></td></tr>)}</tbody></table></div></section>
      <section className="panel"><p className="eyebrow">02 / GOVERNANCE</p><h2>Risk register</h2><div className="risk-grid">{data.risks.map(x => <article className="risk" key={x.risk}><div className="risk-top"><h3>{x.risk}</h3><span className="tag">{x.likelihood} likelihood</span></div><p><b>Impact:</b> {x.impact}</p><p>{x.mitigation}</p></article>)}</div></section>
      <section className="panel"><p className="eyebrow">03 / EXECUTION</p><h2>Implementation roadmap</h2><div className="roadmap">{data.roadmap.map((x,i) => <article className="phase" key={x.phase}><span className="number">{String(i+1).padStart(2,'0')}</span><div><h3>{x.phase}</h3><small>{x.duration}</small><p>{x.tasks}</p></div></article>)}</div></section>
      <section className="panel"><p className="eyebrow">04 / STRATEGY</p><h2>SWOT analysis</h2><div className="swot">{Object.entries(data.swot).map(([key,items]) => <article className="swot-card" key={key}><h3>{key}</h3><ul>{items.map(item => <li key={item}>{item}</li>)}</ul></article>)}</div></section>
    </>}
    <footer><b>Important disclaimer:</b> This is an educational planning prototype, not a clinical decision-support system. It must not be used to diagnose or treat patients. Do not enter real patient data.</footer>
  </div>;
}

export default App;
