const form = document.querySelector('form');
const progressBar = document.querySelector('#progressBar');
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(form);
  const response = await fetch('/', {
    method: 'POST',
    body: formData,
  });
  const reader = response.body.getReader();
  const contentLength = response.headers.get('Content-Length');
  let receivedLength = 0;
  while (true) {
    const { done, value } = await reader.read();
    if (done) {
      break;
    }
    receivedLength += value.length;
    progressBar.value = (receivedLength / contentLength) * 100;
  }
});
