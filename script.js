async function loadPage(page) {
  const res = await fetch(`pages/${page}.html`);
  const text = await res.text();
  document.getElementById("content").innerHTML = text;
}
