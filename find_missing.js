const fs = require('fs');

const content = fs.readFileSync('caparks.html', 'utf-8');

// Find the PARK_DETAILS declaration
const startStr = 'const PARK_DETAILS = {';
const startIndex = content.indexOf(startStr);
if (startIndex === -1) {
  console.error("Could not find start of PARK_DETAILS");
  process.exit(1);
}

const endIndex = content.indexOf('};\n\nfunction', startIndex);
if (endIndex === -1) {
  console.error("Could not find end of PARK_DETAILS");
  process.exit(1);
}

const detailsStr = content.substring(startIndex + startStr.length, endIndex);

// We need to parse out the park blocks
const blocks = [];
let re = /\n\s*'([^']+)':\s*\{/g;
let match;
let lastIndex = 0;
let lastParkId = null;

while ((match = re.exec(detailsStr)) !== null) {
  if (lastParkId) {
    blocks.push({ id: lastParkId, content: detailsStr.substring(lastIndex, match.index) });
  }
  lastParkId = match[1];
  lastIndex = match.index;
}
if (lastParkId) {
  blocks.push({ id: lastParkId, content: detailsStr.substring(lastIndex) });
}

let missingParks = [];

for (const block of blocks) {
  const c = block.content;
  let missing = false;
  if (!c.includes('biking:')) missing = true;
  if (!c.includes('photography:')) missing = true;
  if (!c.includes('sunsetSpots:')) missing = true;
  if (!c.includes('googleRating:')) missing = true;
  if (!c.includes('googleReviews:')) missing = true;
  if (c.includes("gain:'—'")) missing = true;
  // Also check if gain is completely missing from any hike object?
  // Previous edits added 'gain' to all hikes! But some may have gain:'—', we need to replace those.
  
  if (missing && missingParks.length < 20) {
    missingParks.push({ id: block.id });
  }
}

console.log(JSON.stringify(missingParks.map(p => p.id), null, 2));
