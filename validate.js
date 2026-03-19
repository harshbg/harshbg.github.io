const fs = require('fs');
try {
  const content = fs.readFileSync('caparks.html', 'utf-8');
  const startStr = 'const PARK_DETAILS = {';
  const startIdx = content.indexOf(startStr);
  const endIdx = content.indexOf('};\n\nfunction', startIdx) + 1;
  const objectStr = content.substring(startIdx + startStr.length - 1, endIdx);
  
  // Try evaluating it
  const evalFunc = new Function('return ' + objectStr);
  const obj = evalFunc();
  console.log(`Successfully parsed ${Object.keys(obj).length} park details objects.`);
} catch (e) {
  console.error("Syntax Error!! " + e);
  process.exit(1);
}
