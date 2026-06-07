// Consistent stderr logging. stdout is reserved for the JSON result so the
// caller (Claude via Bash) can parse it cleanly.

const LEVELS = { debug: 0, info: 1, warn: 2, error: 3 };
const CURRENT = LEVELS[process.env.THINK_ENGINE_LOG_LEVEL || 'info'];

function fmt(level, args) {
  const ts = new Date().toISOString().slice(11, 19);
  return `[${ts}] ${level.toUpperCase().padEnd(5)} ${args.map(String).join(' ')}`;
}

export const log = {
  debug: (...a) => CURRENT <= LEVELS.debug && process.stderr.write(fmt('debug', a) + '\n'),
  info:  (...a) => CURRENT <= LEVELS.info  && process.stderr.write(fmt('info', a)  + '\n'),
  warn:  (...a) => CURRENT <= LEVELS.warn  && process.stderr.write(fmt('warn', a)  + '\n'),
  error: (...a) => CURRENT <= LEVELS.error && process.stderr.write(fmt('error', a) + '\n'),
};
