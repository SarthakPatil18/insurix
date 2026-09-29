const fs = require('fs');
const readline = require('readline');

async function extract() {
  const fileStream = fs.createReadStream('C:/Users/Rehan/.gemini/antigravity-ide/brain/8aa508c9-6e83-4171-9a93-6321cc5d0662/.system_generated/logs/transcript.jsonl');
  const rl = readline.createInterface({ input: fileStream, crlfDelay: Infinity });

  let fullContent = '';
  for await (const line of rl) {
    if (line.includes('design%20%281%29.md')) {
      try {
        const obj = JSON.parse(line);
        if (obj.content) {
          fullContent += obj.content + '\n';
        }
      } catch (e) {}
    }
  }

  const lines = fullContent.split('\n');
  const cleanLines = [];
  const seenLineNums = new Set();
  for (const l of lines) {
    const match = l.match(/^(\d+):\s(.*)$/);
    if (match) {
      const num = parseInt(match[1]);
      if (!seenLineNums.has(num)) {
        seenLineNums.add(num);
        cleanLines.push({ num, text: match[2] });
      }
    }
  }
  cleanLines.sort((a,b) => a.num - b.num);
  const out = cleanLines.map(c => c.text).join('\n');
  fs.writeFileSync('docs/DESIGN_SPEC.md', out, 'utf-8');
  console.log('Saved docs/DESIGN_SPEC.md with ' + cleanLines.length + ' lines.');
}
extract();
