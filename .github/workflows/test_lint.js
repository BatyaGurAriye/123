const { exec } = require('child_process');
const assert = require('assert');

describe('Linting', function () {
  it('should pass ESLint without errors', function (done) {
    exec('npx eslint .', (error, stdout, stderr) => {
      assert.strictEqual(error, null, `ESLint failed:\n${stdout}\n${stderr}`);
      done();
    });
  });
});