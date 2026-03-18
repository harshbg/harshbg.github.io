const fs = require('fs');
const content = fs.readFileSync('caparks.html', 'utf-8');
const scriptStart = content.indexOf('<script>');
const scriptEnd = content.lastIndexOf('</script>');
const jsCode = content.substring(scriptStart + 8, scriptEnd);
try {
  // We can't eval easily because it depends on DOM or other things, but we can syntax check it
  new Function(jsCode);
  console.log("Syntax is valid!");
} catch (e) {
  console.error("Syntax Error:", e.message);
}
